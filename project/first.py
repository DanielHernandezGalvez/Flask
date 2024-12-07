from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = "kramer"
    return render_template("index.html", name = name)

#string
#int
#float
#path
#uuid
@app.route("/hello/") 
@app.route("/hello/<string:name>") 
@app.route("/hello/<string:name>/<int:age>") #variables en rutas
def hello(name = None, age = None):
    if name == None and age == None:
        return "<h1>Hola, mundo!</h1>"
    elif age == None:
        return f"<h1>Hola, {name}!</h1>"
    else:
        return f"<h1>Hola {name}! el doble de tu edad es {age * 2}</h1>"

from markupsafe import escape

@app.route("/code/<path:code>")
def code(code):
    return f"<code>{escape(code)}</code>" # se anula la ejecución de código
