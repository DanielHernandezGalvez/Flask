from flask import Flask, render_template

app = Flask(__name__)

# filtros personalizados
@app.add_template_filter
def today(date):
    return date.strftime("%d-%m-%Y")

# app.add_template_filter(today, "today") se puede registrar asi o como arriba

# funcion personalizada
@app.add_template_global # se registra en la aplicación y ya no es necesario enviar en el index
def repeat(string, number):
    return string * number

# app.add_template_global(repeat, "repeat") también se registra así

from datetime import datetime

@app.route("/")
@app.route("/index")
def index():
    name = "kramer"
    friends = ["Daniel", "Alexis", "Juan"]
    date = datetime.now()
    return render_template(
    "index.html",
    name = name,
    friends = friends,
    date = date,
    # repeat = repeat ya no es necesario por el decorador
    )

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
