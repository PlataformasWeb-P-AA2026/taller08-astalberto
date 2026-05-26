# Seleccionar una sola cadena de conexión (comentar la que no se use)

# SQLite (por defecto)

cadena_base_datos = 'sqlite:///paises.db'

# MariaDB/MySQL — requiere: pip install mysql-connector-python
# El contenedor debe estar corriendo (docker-compose up -d)
# Crear la base de datos una vez: CREATE DATABASE paises;
# docker exec orm_mariadb_uso mariadb -uroot -prootpassword -e "CREATE DATABASE IF NOT EXISTS paises CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
# cadena_base_datos = 'mysql+mysqlconnector://root:rootpassword@localhost:3310/paises'


