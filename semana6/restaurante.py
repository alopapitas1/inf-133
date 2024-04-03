# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Crear tabla de carreras
try:
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("LA TABLA PEDIDOS YA EXISTE")


# Insertar datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, 'categoria') 
    VALUES ('pizza',10.99, 'italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, 'categoria') 
    VALUES ('hamburgesa',8.99, 'americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, 'categoria') 
    VALUES ('sushi',12.99, 'japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, 'categoria') 
    VALUES ('ensalada',6.99, 'vegetariana')
    """
)

# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
    #1
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)


# CARRERAS:
# (1, 'Ingeniería en Informática', 5)
# (2, 'Licenciatura en Administración', 4)

##############################################################################

# Crear tabla de carreras

try:
    conn.execute(
        """
        CREATE TABLE MESA
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("LA TABLA PEDIDOS YA EXISTE")

# Insertar datos de platos
conn.execute(
    """
    INSERT INTO MESA (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESA (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESA (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESA (numero) 
    VALUES (4)
    """
)
# Consultar datos
print("\nMESA:")
cursor = conn.execute("SELECT * FROM MESA")
for row in cursor:
    print(row)





############################################################################

# Crear tablas de estudiantes
try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        platos_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (platos_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESA(id));
        """
    )
except sqlite3.OperationalError:
    print("LA TABLA PEDIDOS YA EXISTE")


# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesa_id, cantidad, fecha)
    VALUES (2,3,1, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesa_id, cantidad, fecha) 
    VALUES (3,1,3, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (platos_id, mesa_id, cantidad, fecha) 
    VALUES (4,4,1, '2024-04-02')
    """
)

print("\PEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)




#2
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 2
    """
)

#3
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)


#join
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESA.numero 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.platos_id = PLATOS.id 
    JOIN MESA ON PEDIDOS.mesa_id = MESA.id
    """
)
for row in cursor:
    print(row)



print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT MESA.numero, PEDIDOS.mesa_id
    FROM PEDIDOS
    LEFT JOIN MESA ON PEDIDOS.id = PEDIDOS.mesa_id
    LEFT JOIN PEDIDOS ON PEDIDOS.id = PEDIDOS.id;
    """
)
for row in cursor:
    print(row)




conn.commit()
conn.close()
