from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import datetime

db = SQLAlchemy()


class Alumnos(db.Model):
    __tablename__='alumnos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apepaterno = db.Column(db.String(50))
    #ape_materno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default= datetime.now)
