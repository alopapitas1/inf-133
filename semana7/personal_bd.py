import sqlite3

connect=sqlite3.connect("personal_bd.db")
try:
    connect.execute(
        """
        CREATE TABLE DEPARTAMENTOS(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
        )
        """
    )
except sqlite3.OperationalError:
    print("LA TABLA DEPARTAMENTOS YA EXISTE")
    

connect.execute(
    """
    INSERT INTO DEPARTAMENTOS('nombre','fecha_creacion')
    VALUES('ventas', '10-04-2020')
    """
)

connect.execute(
    """
    INSERT INTO DEPARTAMENTOS('nombre','fecha_creacion')
    VALUES('marketing', '11-04-2020')
    """
)






#------------------------------------------------------------
try:        
    connect.execute(
        """
        CREATE TABLE CARGOS(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            nivel TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )
        """
    )
except sqlite3.OperationalError:
    print("LA TABLA CARGOS YA EXISTE")
    
    
    

connect.execute(
    """
    INSERT INTO CARGOS('nombre','nivel','fecha_creacion')
    VALUES('gerente de ventas', 'senior','10-04-2020')
    """
)


connect.execute(
    """
    INSERT INTO CARGOS('nombre','nivel','fecha_creacion')
    VALUES('analista de marketing','junior','11-04-2020')
    """
)
    
    
connect.execute(
    """
    INSERT INTO CARGOS('nombre','nivel','fecha_creacion')
    VALUES('representantes de ventas','junior','12-04-2020')
    """
)
#------------------------------------------------------------

    
try:
    connect.execute(
        """
        CREATE TABLE EMPLEADOS(
        id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY  (cargo_id) REFERENCES CARGOS(id)
        );
        """
    )
    
except sqlite3.OperationalError:
    print("LA TABLA EMPLEADOS YA EXISTE")
    
    
    
connect.execute(
    """
    INSERT INTO EMPLEADOS('nombres','apellido_paterno','apellido_materno','fecha_contratacion','fecha_creacion','departamento_id','cargo_id')
    VALUES('juan','gonzales','perez','15-05-2023','15-05-2023','1','1')
    """
)

connect.execute(
    """
    INSERT INTO EMPLEADOS('nombres','apellido_paterno','apellido_materno','fecha_contratacion','fecha_creacion','departamento_id','cargo_id')
    VALUES('maria','lopez','martinez','20-06-2023','20-06-2023','2','2')
    """
)
    
    
#------------------------------------------------------------

try:
    connect.execute(
        """
        CREATE TABLE SALARIOS(
        id INTEGER PRIMARY KEY,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        empleado_id INTEGER NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
        );
        """
    )
    
except sqlite3.OperationalError:
    print("LA TABLA SALARIOS YA EXISTE")
    
connect.execute(
    """
    INSERT INTO SALARIOS('salario','fecha_inicio','fecha_fin','fecha_creacion','empleado_id')
    VALUES('3000','1-04-2024','30-04-2025','1-04-2024','1')
    """
)

connect.execute(
    """
    INSERT INTO SALARIOS('salario','fecha_inicio','fecha_fin','fecha_creacion','empleado_id')
    VALUES('3500','1-07-2023','30-04-2024','1-07-2023','2')
    """
)






connect.commit()
connect.close()
