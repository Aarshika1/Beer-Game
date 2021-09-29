"""Defines database models for our game's classes in Flask"""

from main import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Game(db.Model):
    """Class for a Beer Game individual game"""

    __tablename__ = "Game"

    id = db.Column(db.Integer, primary_key=True)
    session_length = db.Column(db.Integer, nullable=False)
    distributor_present = db.Column(db.Boolean, nullable=False)
    wholesaler_present = db.Column(db.Boolean, nullable=False)
    holding_cost = db.Column(db.Integer, nullable=False)
    backlog_cost = db.Column(db.Integer, nullable=False)
    session_id = db.Column(db.Integer, nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('Instructor.id'))
    instructor = db.relationship("Instructor", backref=db.backref("Instructor", uselist=True), foreign_keys=[instructor_id])
    active = db.Column(db.Integer, nullable=False)
    info_sharing = db.Column(db.Integer, nullable=False)
    info_delay = db.Column(db.Integer, nullable=False)
    demand_id = db.Column(db.Integer, db.ForeignKey('DemandPattern.id'))
    demand_pattern = db.relationship("DemandPattern", backref=db.backref("DemandPattern", uselist=False), foreign_keys=[demand_id])
    rounds_complete = db.Column(db.Integer, nullable=False)
    is_default_game = db.Column(db.Boolean, nullable=False)
    starting_inventory = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Game {}>'.format(self.id)
class DemandPattern(db.Model):
    """Class for a Beer Game demand pattern"""

    __tablename__ = "DemandPattern"
    id = db.Column(db.Integer, primary_key=True)
    weeks = db.Column(db.Integer, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))
    game = db.relationship("Game", backref=db.backref("game_demand", uselist=False), foreign_keys=[game_id])
    name = db.Column(db.String(64), nullable=False)

class Instructor(db.Model):
    """Class for a Beer Game instructor"""

    __tablename__ = "Instructor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    default_game = db.Column(db.Integer, db.ForeignKey('Game.id'))
    game = db.relationship("Game", backref=db.backref("game_instructor", uselist=False), foreign_keys=[default_game])


class Student(db.Model):
    """Class for a Beer Game instructor"""

    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)


