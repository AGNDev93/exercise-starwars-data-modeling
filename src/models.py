import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    password = Column(String(250))
    subscription_date = Column(Integer)

    favorite=relationship("Favorite")

class Favorite(Base):

    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id')) 

    user_id=Column(Integer, ForeignKey('user.id')) 


class Character(Base):

    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

    favorite=relationship("Favorite")

class Planet(Base):

    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation = Column(String(250))
    orbital = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))

    favorite=relationship("Favorite")

class Vehicle(Base):

    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    vehicle_class = Column(String(250))

    favorite=relationship("Favorite")


# Generar diagrama
render_er(Base, 'diagram.png')
