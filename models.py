from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()
NOTE_TYPES = ['prescription', 'appointment']

class NoteType(Base):
    __tablename__ = "note_types"
    id = Column(Integer, primary_key=True)
    label = Column(String)
    color = Column(String)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    label = Column(String)
    color = Column(String)
    notes = Column(String)
    time = Column(DateTime)
    # time_str = Column(String)