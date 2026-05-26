from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Continente(Base):
    __tablename__ = 'continente'
    id     = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)

    paises = relationship('Pais', back_populates='continente')

    def __repr__(self):
        return f"Continente: {self.nombre}"


class Pais(Base):
    __tablename__ = 'pais'
    id            = Column(Integer, primary_key=True, autoincrement=True)
    nombre        = Column(String(100), unique=True, nullable=False)
    continente_id = Column(Integer, ForeignKey('continente.id'), nullable=False)

    continente        = relationship('Continente', back_populates='paises')
    jugadores_nacidos = relationship('Jugador', foreign_keys='Jugador.pais_nacimiento_id',
                                     back_populates='pais_nacimiento')
    jugadores_jugando = relationship('Jugador', foreign_keys='Jugador.pais_donde_juega_id',
                                     back_populates='pais_donde_juega')

    def __repr__(self):
        return f"Pais: {self.nombre}"


class Jugador(Base):
    __tablename__ = 'jugador'
    id                        = Column(Integer, primary_key=True, autoincrement=True)
    nombre                    = Column(String(200), nullable=False)
    posicion                  = Column(String(100))
    edad                      = Column(Integer)
    numero_partidos_seleccion = Column(Integer)
    goles_seleccion           = Column(Integer)
    pais_nacimiento_id        = Column(Integer, ForeignKey('pais.id'))
    pais_donde_juega_id       = Column(Integer, ForeignKey('pais.id'))

    pais_nacimiento  = relationship('Pais', foreign_keys=[pais_nacimiento_id],
                                    back_populates='jugadores_nacidos')
    pais_donde_juega = relationship('Pais', foreign_keys=[pais_donde_juega_id],
                                    back_populates='jugadores_jugando')

    def __repr__(self):
        return f"Jugador: {self.nombre}"


Base.metadata.create_all(engine)
