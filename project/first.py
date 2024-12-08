from flask import Flask, render_template, url_for

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
def index():
    print(url_for("index"))
    print(url_for("hello", name = "print('dani)"))
    print(url_for("code", code = "print('Hola')"))
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
@app.route("/hello/<string:name>/<int:age>") 
@app.route("/hello/<string:name>/<int:age>/<email>") #variables en rutas
def hello(name = None, age = None, email = None):
   my_data = {
       "name": name,
       "age": age,
       "email": email
   } 
   return render_template('hello.html', data = my_data)


from markupsafe import escape

@app.route("/code/<path:code>")
def code(code):
    return f"<code>{escape(code)}</code>" # se anula la ejecución de código
