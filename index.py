from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect
import json

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "3o2eyTnC5j5zNM_Tbvnslg"

@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('init.html')

@app.route('/card', methods=['GET'])
def card():
   # return redirect('/card_deck/default_deck/0')
   decks = []
   with open('db/db.json', 'r') as open_file:
      json_object = json.load(open_file)
        
      for label in json_object:
         decks.append(label)

   return render_template('choose_deck.html', 
                           len=len(decks),
                           decks=decks)

@app.route('/card_deck/<deck>/<id>', methods=['GET'])
def card_deck(deck, id):
   card, next_id = get_card(deck, id)
   title = 'Card ' + id

   return render_template('card.html', 
                           header_text=title,
                           flashcard_title=card['card_title'],
                           flashcard_text=card['card_text'],
                           next_id=str(next_id),
                           deck=deck)

def get_card(deck, id):
   cards = []
   with open('db/db.json', 'r') as open_file:
      json_object = json.load(open_file)
      cards = json_object[deck]

   id = int(id)
   next_id = id + 1
   next_id %= len(cards)

   return (cards[id], next_id)

@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
   if request.method == 'POST':    
      json_result = {
         "card_title": request.form["card_title"],
         "card_text": request.form["card_text"],
      }

      card_label = request.form["card_label"]

      with open('db/db.json', 'r') as open_file:
         json_object = json.load(open_file)

         if card_label in json_object:
            json_object[card_label].append(json_result)
         else:
            json_object[card_label] = []
            json_object[card_label].append(json_result)
         
         with open('db/db.json', 'w') as db_file:
            json.dump(json_object, db_file, indent=4)

      return redirect('/add_card')

   return render_template('add_card.html')

if __name__ == "__main__":
   app.run(debug=True, port=80)
