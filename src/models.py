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
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'))
    owner = relationship('Characters', back_populates='starships')


class UserPlanetsFavorites(Base):
    __tablename__ = 'users_planets_favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class UserCharactersFavorites(Base):
    __tablename__ = 'users_characters_favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
