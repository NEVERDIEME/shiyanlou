from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Base(db.Model):
    __abstract__=True
    created_time = db.Column(db.DateTime,default=datetime.utcnow)
    updated_time = db.Column(db.DateTime,
                            default=datetime.utcnow,
                            onupdate=datetime.utcnow)
class User(Base):
    __tablename__='user'
    id = db.Column(db.Integer,index=True,primary_key=True,nullable=False)

