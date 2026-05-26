import csv

from sqlalchemy.orm import sessionmaker

from clases import engine, Continente, Pais, Jugador

# --- Continentes Data ---
PAIS_CONTINENTE = {
    "Alemania":      "Europa",
    "Argentina":     "América del Sur",
    "Australia":     "Oceanía",
    "Brasil":        "América del Sur",
    "Ecuador":       "América del Sur",
    "España":        "Europa",
    "Estados Unidos":"América del Norte",
    "Francia":       "Europa",
    "Inglaterra":    "Europa",
    "Japón":         "Asia",
    "Marruecos":     "África",
    "México":        "América del Norte",
    "Nigeria":       "África",
    "Portugal":      "Europa",
    "Senegal":       "África",
}

Session = sessionmaker(bind=engine)
session = Session()
# --- Insertar Continentes ---
paises_unicos = set()
with open("data/jugadores_futbol.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        paises_unicos.add(row["pais_nacimiento"])
        paises_unicos.add(row["pais_donde_juega"])

continentes_unicos = {PAIS_CONTINENTE.get(p, "Otro") for p in paises_unicos}
for nombre in sorted(continentes_unicos):
    session.add(Continente(nombre=nombre))
session.commit()

continente_map = {c.nombre: c for c in session.query(Continente).all()}

# --- Insertar países ---
for nombre in sorted(paises_unicos):
    nombre_continente = PAIS_CONTINENTE.get(nombre, "Otro")
    session.add(Pais(nombre=nombre, continente=continente_map[nombre_continente]))
session.commit()

pais_map = {p.nombre: p for p in session.query(Pais).all()}

# --- Insertar jugadores ---
with open("data/jugadores_futbol.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        jugador = Jugador(
            nombre                    = row["nombre_jugador"],
            posicion                  = row["posicion"],
            edad                      = int(row["edad"]),
            numero_partidos_seleccion = int(row["numero_partidos_seleccion"]),
            goles_seleccion           = int(row["goles_seleccion"]),
            pais_nacimiento           = pais_map[row["pais_nacimiento"]],
            pais_donde_juega          = pais_map[row["pais_donde_juega"]],
        )
        session.add(jugador)
session.commit()

print(f"Migración completa:")
print(f"  Continentes: {session.query(Continente).count()}")
print(f"  Países:      {session.query(Pais).count()}")
print(f"  Jugadores:   {session.query(Jugador).count()}")
