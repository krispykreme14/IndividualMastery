import projects #projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  return render_template("home.html", projects=projects.setup())

#connects /hello path of server to render Pics.html
@app.route('/Pics/')
def Pics_route():
  return render_template("pics.html", projects=projects.setup())

#connects /historyofcomedy path of server to render AboutMe.html
@app.route('/AboutMe/')
def AboutMe_route():
  return render_template("AboutMe.html", projects=projects.setup())

#connects /Embed path of server to render embed.html
@app.route('/Embed')
def Contact_route():
  return render_template("embed.html", projects=projects.setup())
  





if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(debug=True, port='3000', host='127.0.0.1')