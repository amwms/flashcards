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
   return redirect('/card/0')

@app.route('/card/<id>', methods=['GET'])
def card_id(id):
   card, next_id = get_card(id)
   title = 'Card ' + id

   return render_template('card.html', 
                           header_text=title,
                           flashcard_title=card['card_title'],
                           flashcard_text=card['card_text'],
                           next_id=str(next_id))

def get_card(id):
   cards = []
   with open('db/db.json', 'r') as open_file:
      json_object = json.load(open_file)
      cards = json_object["card_data"]

   id = int(id)
   next_id = id + 1
   next_id %= len(cards)

   return (cards[id], next_id)

@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
   if request.method == 'POST':    
      # json_result = {
      #    "card_title": request.form["card_title"],
      #    # "card_label": request.form["card_text"],
      #    "card_text": request.form["card_text"],
      # }

      # with open('db.json', 'r') as open_file:
      #    json_object = json.load(open_file)
      #    json_object["card_data"].append(json_result)
         
      #    with open('db.json', 'w') as db_file:
      #       json.dump(json_object, db_file, indent=4)

      return redirect('/add_card')

   return render_template('add_card.html')

@app.route('/favorites', methods=['GET'])
def favorites():
   pass

# def make_favorite(id):
#    cards = []
#    with open('db/db.json', 'r') as open_file:
#       json_object = json.load(open_file)
#       cards = json_object["card_data"]

#    if card[id]['is_favorite'] == True:
#       card[id]['is_favorite']

if __name__ == "__main__":
   app.run(debug=True, port=80)
