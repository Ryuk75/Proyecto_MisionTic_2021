import os
import yagmail as yagmail
from flask import Flask,request
from flask.templating import render_template
from forms import FormCreateUser

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/",methods={"GET","POST"})
def user():
    if request.method == "GET":
        formulario = FormCreateUser()
        return render_template('user.html',form = formulario)
    else:
        formulario = FormCreateUser(request.form)
        if formulario.validate_on_submit():
            yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
            yag.send(to=formulario.correo.data,subject="Usuario creado correctamente",contents="Hola {0}, hemos recibido tu mensaje, pronto nos contactaremos contigo, junto con tus credenciales.".format(formulario.nombre.data))
            return render_template('user.html',form = FormCreateUser(), errores="Su usuario a sido creado con éxito.")
            
        return render_template('user.html',form = formulario, errores="Todos los datos son obligatorios.")

@app.route("/product/",methods={"GET","POST"})
def product():
    return render_template('product.html')
    
@app.route("/provider/",methods={"GET","POST"})
def provider():
    return render_template('provider.html')

@app.route("/contact/",methods={"GET","POST"})
def contact():
    return render_template('contact.html')

