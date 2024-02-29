from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, StringField, IntegerField, EmailField, validators
from config import DevelopmentConfig
from flask import g

import forms
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/index", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        try:
            alum = Alumnos(
                nombre=create_form.nombre.data,
                apepaterno=create_form.apepaterno.data,
                email=create_form.email.data
            )
            db.session.add(alum)
            db.session.commit()
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            db.session.rollback()
    return render_template('index.html', form=create_form)


@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCompleto():
    alumno_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    print(alumno)  
    return render_template("ABC_Completo.html", alumno=alumno)


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    print("Alumno: {}".format(g.nombre))
    nombre = ""
    apepaterno = ""
    amaterno = ""
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        nombre = alumno_clase.nombre.data
        apepaterno = alumno_clase.apepaterno.data
        amaterno = alumno_clase.amaterno.data

        print('Nombre: {}'.format(nombre))
        print('apepaterno: {}'.format(apepaterno))
        print('amaterno: {}'.format(amaterno))

        mensaje = 'Bienvenido {}'.format(nombre)
        flash(mensaje)

    return render_template("alumnos.html", form=alumno_clase, nombre=nombre, apepaterno=apepaterno, amaterno=amaterno)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()
