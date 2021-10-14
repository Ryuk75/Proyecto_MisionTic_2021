from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
class FormCreateUser(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    correo = StringField('Correo',validators=[validators.required(),validators.length(max=150)])
    enviar = SubmitField('Crear Usuario')