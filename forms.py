from wtforms import Form
from wtforms import StringField,TelField,IntegerField
from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    x1= IntegerField('x1')
    y1= IntegerField('y1')
    x2= IntegerField('x2')
    y2= IntegerField('y2')
    distancia= IntegerField('distancia')
class ResistenciaForm(Form):
    primerBanda= IntegerField('primerBanda')
    segundaBanda= IntegerField('segundaBanda')
    terceraBanda= IntegerField('terceraBanda')
    tolerancia= StringField('tolerancia')
    valor= IntegerField('valor')
    valorMax= IntegerField('valorMax')
    valorMin= IntegerField('valorMin')

class archivoForm(Form):
    ingles = StringField('ingles',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa una palabra")])
    espanio = StringField('espanio',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa una palabra")])
    buscar = StringField('buscar',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Que buscamos")])
    
class UserForm2(Form):
    id=IntegerField('id',[validators.number_range(min=4,max=20, message='Ingresa nombre valido')])
    nombre= StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa nombre valido')
    ])
    apepaterno= StringField('apepaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    email= EmailField('email',[
        validators.Email(message='Ingresa un correo valido')
    ])