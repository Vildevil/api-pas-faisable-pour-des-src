from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

class Player(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)
