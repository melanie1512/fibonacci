from dataclasses import dataclass
from flask import Flask, jsonify,  request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@dataclass
class Fib(db.Model):
    id: int
    num: int
    
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer(100), nullable=False)

    def __repr__(self):
        return f'<Fib {self.name}>'
