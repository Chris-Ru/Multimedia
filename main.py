import projects
from flask import Flask, render_template, url_for, request, redirect, flash, render_template_string
import numpy as np
#from flask_sqlalchemy import SQLAlchemy

#create a Flask instance
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']
popular= []

#connects default URL to a function
@app.route('/', methods=['GET','POST'])
def home():
  if(request.method == 'POST'):
    form = request.form
    product = form['product']  
    open("products.txt", "a").write("\n" + product)
    a = open("products.txt", "r").read()
    popular = a.split("\n")
    if(len(popular) > 7):
      popular.pop(0)
      seperator = '\n'
      newContent = seperator.join(popular)
      open("products.txt", "w").write(newContent)
    return redirect("https://www.amazon.com/s?k=" + product +"&ref=nb_sb_noss")
  a = open("products.txt", "r").read()
  popular = a.split("\n")
  return render_template('home.html', projects=projects.setup(), popular=popular)

  return render_template("home.html", projects=projects.setup(), popular=popular)

    
@app.route('/youtube/', methods=['GET', 'POST'])
def youtube():
  if(request.method == 'POST'):
    form = request.form
    link = form['link']
    if not(link.startswith("https://youtube.com/embed/")):
      
      return render_template_string('<h1>please enter a valid link<br><p>If you have a "www." make sure to remove it</p><iframe frameborder="0" width="666px" height="375px" src="https://owo.whats-th.is/ARRGFC3.gif"</iframe>')
    else:
      open("youtube.txt", "a").write("\n" + link + '?controls=0')
  a = open("youtube.txt", "r").read()
  links = a.split("\n")
  return render_template("youtube.html", projects=projects.setup(), links=links)

  
@app.route('/spotify/', methods=['GET', 'POST'])
def spotify():
  if(request.method == 'POST'):
    form = request.form
    link = form['link']
    if not(link.startswith("https://open.spotify.com/embed/")):
      return render_template_string("<h1>Please enter a valid spotify playlist url</h1><br><p>Did you add the /embed between /playlist/ and the playlist id?</p>")
      return
    else:
      open("spotify.txt", "a").write("\n" +  link)
  a = open("spotify.txt", "r").read()
  links = a.split("\n")
  return render_template("spotify.html", projects=projects.setup(), links=links)


@app.route('/flask/')
def flask():
    #Flask import uses Jinga to render HTML
    return render_template("fseries.html", projects=projects.setup())


@app.route('/hello/')
def hello():
    #Flask import uses Jinga to render HTML
    return render_template("hseries.html", projects=projects.setup())


@app.route('/template1/')
def testing():
    return render_template("template1.html", projects=projects.setup())


@app.route('/selfgrade/')
def selfgrade():
    return render_template("selfgrade.html", projects=projects.setup())


@app.route('/videos/')
def videos():
    return render_template('videos.html', projects=projects.setup())


@app.route('/products/')
def products():
  return render_template('products.html')


@app.route('/popular-items/')
def popularitems():
  a = open("products.txt", "r").read()
  popular = a.split("\n")
  return render_template("popularitem.html", projects=projects.setup(), popular=popular)


@app.route('/week/')
def week():
  return render_template('week.html')

@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
  if(request.method == 'POST'):
    form = request.form
    a = form['type']
    b = form['num1']
    c = form['num2']
    if a == 1:
      addition = np.add(b,c)
      result = "\nAdded values: \n" + addition
    elif a == 2:
      subtraction = np.subtract(b,c)
      result = "\nSubtracted values: \n" + subtraction
    elif a == 3:
      multiply = np.multiply(b,c)
      result = "\nMultiplied values" + multiply
    elif a == 4:
      divide = np.divide(b,c)
      result = "\nDivided values" + divide
    elif a == 5:
      power = np.power(b,c)
      result = "\nPower values" + power
    elif a == 6:
      modulus = np.mod(b,c)
      result = "\nModulus values" + modulus
    # elif a == 7:
    #   in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
    #   print ("Input array : \n", in_array)
      
    #   tan_Values = np.tan(in_array)
    #   print ("\nTan values : \n", tan_Values)
    # elif a == 8:
    #   in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
    #   print ("Input array : \n", in_array)
      
    #   sin_Values = np.sin(in_array)
    #   print ("\nSin values : \n", sin_Values)
    # elif a == 9:
    #   in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
    #   print ("Input array : \n", in_array)
      
    #   cos_Values = np.cos(in_array)
    #   print ("\nCos values : \n", cos_Values)

    return render_template('calculator.html', result = result)
  return render_template('calculator.html')

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
