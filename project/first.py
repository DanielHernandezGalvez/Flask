from flask import Flask, render_template, url_for, request

app = Flask(__name__)
# clave secreta para el formulario
app.config.from_mapping(
    SECRET_KEY = "dev"
)

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

# Crear formulario con wtf form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class Register_Form(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators = [DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Contraseña: ", validators = [DataRequired(), Length(min=6, max=40)])
    submit = SubmitField("Registrar: ")

# registrar usuario
@app.route("/auth/register", methods = ["GET", "POST"])
def register():
    form = Register_Form()
    print(request.form)
    if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            return f"Nombre de usuario { username }, Contraseña: {password}"
            
    # if request.method == 'POST':
    #     username = request.form["username"]
    #     password = request.form["password"]
        
    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:   
    #         return f"Nombre de usuario { username }, Contraseña: {password}"
    #     else:
    #         error = """
    #         El nombre de usuario debe tener entre 4 y 25 caracteres y la contraseña entre 6 y 40
    #         """
    #         return render_template('auth/register.html', form = form, error = error)
    return render_template('auth/register.html', form = form)