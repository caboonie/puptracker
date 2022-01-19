from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta 

engine = create_engine('sqlite:///notes.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# User Interactions

def create_note_type(label, color):
    note_type = NoteType(label=label, color = color)
    session.add(note_type)
    session.commit()
    return note_type

def get_note_types():
    return session.query(NoteType).all()

def get_note_type_label(label):
    return session.query(NoteType).filter_by(label=label).first()

def get_note_type_id(id):
    return session.query(NoteType).filter_by(id=id).first()

if get_note_type_label("Pee") == None:
    create_note_type("Pee", "#009688")
    create_note_type("Poo", "#009688")
    create_note_type("Pee Accident", "#f44336")
    create_note_type("Poo Accident", "#f44336")
    create_note_type("Food", "#2196F3")
    create_note_type("Training", "orange")

def create_note(note_type_id, time, notes):
    note_type = get_note_type_id(note_type_id)
    note = Note(label=note_type.label, color=note_type.color, time=time, notes=notes)
    session.add(note)
    session.commit()
    return note

def get_notes():
    return session.query(Note).all()

def get_note_id(id_num):
    return session.query(Note).filter_by(id=id_num).first()

def get_notes_day(date):
    return session.query(Note).filter_by(Note.time <= date + timedelta(days=1)).filter(Note.time >= date).all()

def get_notes_label(label):
    return session.query(Note).filter_by(label = label).all()


def get_notes_filters(filters):
    return session.query(Note).filter(*filters).all()

if get_notes()== []:
    print(get_notes())
    create_note(get_note_type_label("Pee").id, datetime.now(), "beef liver treat")
    create_note(get_note_type_label("Poo Accident").id, datetime.now()-timedelta(hours=2), "circled before")
    create_note(get_note_type_label("Training").id, datetime.now()-timedelta(hours=1), "successful sits")
    create_note(get_note_type_label("Poo Accident").id, datetime.now()-timedelta(hours=4), "circled before")
    create_note(get_note_type_label("Training").id, datetime.now()-timedelta(hours=5), "successful sits")
