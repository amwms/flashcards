from flask import Flask,\
                  render_template,\
                  url_for,\
                  request,\
                  flash,\
                  redirect

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = "3o2eyTnC5j5zNM_Tbvnslg"

@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template('init.html')

if __name__ == "__main__":
   app.run(debug=True, port=80)
