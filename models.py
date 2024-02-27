from extensions import db
from flask_login import UserMixin
from uuid import uuid4

class User(UserMixin, db.Model):
    ___tablename__ ='users'
    
    id = db.Column(db.String(), unique=True, primary_key=True, default=str(uuid4()))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text(100), nullable = False)
    name = db.Column(db.String(1000), nullable= False)