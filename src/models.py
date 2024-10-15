import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name=Column(String(250))
    first_name=Column(String(250))
    last_name=Column(String(250))
    email=Column(String(250))
    password=Column(String(250))

    # name = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Characters=Column(String(250))
    Planets=Column(String(250))
    Vechicles=Column(String(250))

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name=Column(String(250))
    height=Column(String(250))
    mass=Column(String(250))
    hair_color=Column(String(250))
    skin_color=Column(String(250))
    eye_color=Column(String(250))
    birth_year=Column(String(250))
    gender=Column(String(250))
    
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name=Column(String(250))
    rotation=Column(String(250))
    orbital=Column(String(250))
    diameter=Column(String(250))
    climate=Column(String(250))
    gravity=Column(String(250))
    terrain=Column(String(250))
    surface_water=Column(String(250))
    population=Column(String(250))

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250))
    model=Column(String(250))
    manufacturer=Column(String(250))
    cost_in_credits=Column(String(250))
    length=Column(String(250))
    max_atmosphering_speed=Column(String(250))
    crew=Column(String(250))
    passengers=Column(String(250))
    cargo_capacity=Column(String(250))
    consumables=Column(String(250))
    vehicle_class=Column(String(250))

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
