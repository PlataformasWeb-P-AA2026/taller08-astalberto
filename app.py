import streamlit as st
import pandas as pd

from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func

from clases import engine, Continente, Pais, Jugador

# =========================================================
# CONFIGURAR SESIÓN
# =========================================================

Session = sessionmaker(bind=engine)
session = Session()

st.title("Reporte de Jugadores")

# =========================================================
# TABLA 1
# =========================================================

st.header("TABLA 1 - INFORMACIÓN DE JUGADORES")

PaisNacimiento = aliased(Pais)
PaisJuega = aliased(Pais)

resultado1 = session.query(
    Jugador.nombre,
    PaisNacimiento.nombre.label("pais_nacimiento"),
    PaisJuega.nombre.label("pais_donde_juega"),
    Jugador.posicion,
    Jugador.edad,
    Jugador.numero_partidos_seleccion,
    Jugador.goles_seleccion,
    Continente.nombre.label("continente")
).join(
    PaisNacimiento,
    Jugador.pais_nacimiento
).join(
    Continente,
    PaisNacimiento.continente
).join(
    PaisJuega,
    Jugador.pais_donde_juega
).all()

# Convertir a DataFrame
df1 = pd.DataFrame(resultado1, columns=[
    "Jugador",
    "País Nacimiento",
    "País donde juega",
    "Posición",
    "Edad",
    "Partidos Selección",
    "Goles Selección",
    "Continente"
])

st.dataframe(df1)

# =========================================================
# TABLA 2
# =========================================================

st.header("TABLA 2 - JUGADORES Y GOLES POR CONTINENTE")

resultado2 = session.query(
    Continente.nombre,
    func.count(Jugador.id).label("numero_jugadores"),
    func.sum(Jugador.goles_seleccion).label("total_goles")
).join(
    Pais, Continente.paises
).join(
    Jugador, Pais.jugadores_nacidos
).group_by(
    Continente.nombre
).all()

df2 = pd.DataFrame(resultado2, columns=[
    "Continente",
    "Número Jugadores",
    "Total Goles"
])

st.table(df2)

# =========================================================
# TABLA 3
# =========================================================

st.header("TABLA 3 - JUGADORES Y GOLES POR PAÍS")

resultado3 = session.query(
    Pais.nombre,
    func.count(Jugador.id).label("numero_jugadores"),
    func.sum(Jugador.goles_seleccion).label("total_goles")
).join(
    Jugador,
    Pais.jugadores_nacidos
).group_by(
    Pais.nombre
).all()

df3 = pd.DataFrame(resultado3, columns=[
    "País",
    "Número Jugadores",
    "Total Goles"
])

st.dataframe(df3)

session.close()

