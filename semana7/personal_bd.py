import sqlite3

connect = sqlite3.connect("personal.db")

try:
    connect.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("la tabla DEPARTAMENTOS ya existe")


connect.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('ventas','10-04-2020')
    """
)
connect.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('marketing','11-04-2022')
    """
)


try:
    connect.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )

except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")


connect.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('gerente de ventas', 'senior', '10-04-2020')
    """
)

connect.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('analista de marketing', 'junior', '11-04-2020')
    """
)

connect.execute(
    """
    INSERT INTO CARGOS(nombre, nivel, fecha_creacion)
    VALUES('representante de ventas', 'junior', '12-04-2020')
    """
)



try:
    connect.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargos_id INTEGER NOT NULL,
        fecha_de_creacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargos_id) REFERENCES CARGOS(id));
        """
    )

except sqlite3.OperationalError:
    print("la tabla EMPLEADOS YA EXISTE")



connect.execute(
    """
    INSERT INTO EMPLEADOS('nombres', 'apellido paterno', 'apellido_materno', )
    VALUES ()

    """
)



try:
    connect.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        empleado_id INTEGER NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )

except sqlite3.OperationalError:
    print("la tabla SALARIOS YA EXISTE")




connect.commit()
connect.close()
