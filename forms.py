from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField,TextAreaField,PasswordField
from wtforms import IntegerField
from wtforms import SelectField

class FormCreateUser(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    correo = StringField('Correo',validators=[validators.required(),validators.length(max=150)])
    contraseña = PasswordField('Contraseña',validators=[validators.required(),validators.length(max=20)])
    tipoUsuario = SelectField(u'Tipo de Usuario',validators=[validators.required(),validators.length(max=20)],choices=[('uf','Usuario Final'),('admin','Administrador'),('root','Super Administrador')])
    enviar = SubmitField('Crear Usuario')

class FormContact(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    correo = StringField('Correo',validators=[validators.required(),validators.length(max=150)])
    mensaje = TextAreaField('Mensaje',validators=[validators.required(),validators.length(max=500)])
    enviar = SubmitField('Enviar mensaje')

class FormCreateProduct(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    descripcion = TextAreaField('Descripcion',validators=[validators.required(),validators.length(max=500)])
    cantBodega = IntegerField('Cantidad en Bodega',validators=[validators.required(),validators.length(max=100)])
    cantMinBodega = IntegerField('Cantidad Minima requerida en Bodega',validators=[validators.required(),validators.length(max=100)])

class FormLoginUser(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    contraseña = PasswordField('Contraseña',validators=[validators.required(),validators.length(max=20)])
    enviar = SubmitField('Loguear Usuario')