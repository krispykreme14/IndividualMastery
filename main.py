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

#connects /knock path of server to render embed.html
@app.route('/Embed')
def Contact_route():
  return render_template("embed.html", projects=projects.setup())
  
#connects /iniyaa path of server to render iniyaa.html
@app.route('/iniyaa')
def iniyaa_route():
  return render_template("iniyaa.html", projects=projects.setup())

#connects /ketki path of server to render ketki.html
@app.route('/ketki')
def ketki_route():
  return render_template("ketki.html", projects=projects.setup())


#connects /lucas path of server to render lucas.html
@app.route('/lucas')
def lucas_route():
  return render_template("lucas.html", projects=projects.setup())




if __name__ == "__main__":
  #runs the application on the repl development server
  app.run(debug=True, port='3000', host='127.0.0.1')