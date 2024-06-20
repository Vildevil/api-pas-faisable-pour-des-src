from sqlalchemy import Column, Integer, String
from app import db

class Team(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
