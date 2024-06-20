from sqlalchemy import Column, Integer, String
from app import db

class Coach(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    team_id = Column(Integer, db.ForeignKey('team.id'), nullable=False)
