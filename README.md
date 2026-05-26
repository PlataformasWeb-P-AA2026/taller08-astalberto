# taller08

## Integración de datos y uso de ORM

Integrar datos de un formato común y almacenarlos en sqlite / mysql / mariaDb


## Archivos proporcionados
* Fuente 1: jugadores_futbol.csv

## Acciones

1. Crear una base de datos en sqlite, llamada paises

2. Crear las siguientes entidades

2.1. Continente
2.2. Pais
2.3. Jugador

3. Leer la información de la fuente y migrar a las tablas de forma adecuada. Usar los conceptos de ORM

4. Generar app en Streamlit que permita visualizar un tabla con la siguiente información

En una tabla:

nombre_jugador  pais_nacimiento   pais_donde_juega  posicion  edad  numero_partidos_seleccion goles_seleccion continente

En una tabla

continente  número de jugadores de la base, número goles en función de los goles de cada jugador

En una tabla

paise número de jugadores de la base, número de goles en función de los goles de cada jugador

5. Probar el funcionamiento una base de datos mariaDB o mySQL

## Entregables

* Script(s) replicables (indicar el orden de ejecución)
* Script de frontend
* Evidencia de la base de datos sqlite
* Evidencia de la base de datos mariaDB o mySQL
* Evidencia del fronted funcionando

# Guia para la ejecucion 
Se Activa el entorno virtual:
   python -m venv .venv
   .venv\Scripts\activate

Se instalan las dependencias
 pip install -r requirements.txt

Se ejecuta clases.py
Se ejecuta ingreso_datos.py

Se ejecuta streamlit run app.py