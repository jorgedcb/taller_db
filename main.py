from curses.ascii import CR
import mysql.connector

mydb = mysql.connector.connect(
  host="disenoe.cr8cosserlpi.us-east-1.rds.amazonaws.com",
  user="admin",
  password="castilla74",
  database="telematica"
)
mycursor = mydb.cursor()

def productos(mycursor):
        mycursor.execute("CREATE TABLE productos (id_producto INT AUTO_INCREMENT PRIMARY KEY, nombre_producto VARCHAR(255) NOT NULL, detalle_producto VARCHAR(255) NOT NULL, precio_unitario INT NOT NULL)")

def ingresar_productos(mycursor):
  
    productos = ["Club Colombia","Aguila","Club Colombia Negra", "Poker", "Cola y Pola","Pony Malta","Aguila Light","Costeñita","Pilsen","Redd's","Big Kola","Agua Cielo","Del Valle","Agua Brisa","Hipinto","Gatorade","H2O","Jugos Hit","Mr. Tea"]
    detalle = ["Botella 330ml 30 Unidades","Botella 225ml 38 Unidades","Botella 330ml 30 Unidades","Botella 330ml 30 Unidades","1.5 Litros Pet 6 unidades", "Pet 330ml 24 Unidades","Lata 330ml 24 Unidades", "Botella 225ml 38 Unidades","Lata 330ml 24 Unidades","330ml 30 Unidades","Botella 400ml 24 Unidades","500ml 24 Unidades","2 Litros 8 Unidades","Bolsa 330ml 20 Unidades","Mega 2.5 Litros 8 Unidades","12 unidades","Botella 600ml 15 Unidades","Botella 250ml 30 Unidades","Botella No Retornable 300ml 24 Unidades"]
    precios = [37800,30400,49800,31300,15000,24500,33300,30400,31300,37800,14000,16000,20500 ,8000,29600,22500,26500,19500,26500 ]
    for i in range(len(productos)):
        print(productos[i],"cuesta",precios[i])
        sql = "INSERT INTO productos (nombre_producto, detalle_producto, precio_unitario) VALUES (%s, %s, %s)"
        val = (productos[i], detalle[i], precios[i])
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

def clientes(mycursor):
    mycursor.execute("CREATE TABLE clientes (id_cliente INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, apellido VARCHAR(255) NOT NULL, direccion VARCHAR(255) NOT NULL, id_ciudad INT NOT NULL, id_departamento INT NOT NULL, id_sexo INT NOT NULL, FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad),FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento), FOREIGN KEY (id_sexo) REFERENCES sexos(id_sexo))")

def ingresar_clientes(mycursor):
    sql = "INSERT INTO productos (nombre, apellido, direccion, id_ciudad, id_departamento,id_sexo) VALUES (%s, %s, %s)"
    nombres = ["Alex","Andrea","Andy","Ariel","Akira","Azul","Billie","Charlie","Cris","Cruz","Dani","Denis","Eider","Gaby","Gael","Luján","Mel","Milán","Nicky","Noa"]
    print(len(nombres))
    apellidos = ["Pérez","Sánchez","Ramírez","Torres","Flores","Rivera","Gómez","Díaz","Reyes","Cruz","Morales","Ortiz","Gutiérrez","García","Rodríguez","Martínez","Hernández","López","González"]
    print(len(apellidos))
    direcciones = [("Cr 81 No. 32-60 AP 103", "Medellín"),("Cr 81 No. 32-60 AP 103","Medellín"),("Cr.86 45 aa59", "Medellín"),("Cl 47 No. 29-33 OF 508","Bucaramanga"),("Cr 28 No. 19-107","Cali"),("Cl 32 No. 25-43","Bucaramanga"),("Cl 73 No. 25-09","Bogotá"),("Av 3 No. 28-59","Cartagena"),("Cr 67 No. 167-61 OF 418","Bogotá"),("Cl 41 No. 7-05","Valledupar"),("Cr 57 No. 98-74","Barranquilla"),("Cl 14 No. 2-49 - Palacio Municipal","Santamarta"),("CRA 7N No. 131-99 MZ 15 T8 APTO 405","Barranquilla"),("CRA 38 N° 84-105 BLOQUE 1 APTO 303","Barranquilla"),("Cl 80 No. 8-44","Bogotá"),("Cr 82 No. 35-55 INT 202","Medellín"),("Cl 45 No. 1-06","Bucaramanga"),("Cl 7 No. 22-98 APTO. 2","Cali"),("Cr. 9 No. 10-41","Santa Marta"),("Cl 58 A No. 1-1","Cali")]
    
    

def ciudades(mycursor):
    mycursor.execute("CREATE TABLE ciudades (id_ciudad INT AUTO_INCREMENT PRIMARY KEY, ciudad VARCHAR(255) NOT NULL,id_departamento INT NOT NULL, FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento))")

def ingresar_ciudades(mycursor):
    sql = "INSERT INTO ciudades (ciudad, id_departamento) VALUES (%s, %s)"
    val = [("Bogotá",1),("Medellín",2),("Cali",3),("Barranquilla",4),("Cartagena",5),("Soledad",4),("Cúcuta",6),("Ibagué",7),("Soacha",1),("Villavicencio",8),("Bucaramanga",9),("Santa Marta",10),("Valledupar",11)]

    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

def departamentos(mycursor):
    mycursor.execute("CREATE TABLE departamentos (id_departamento INT AUTO_INCREMENT PRIMARY KEY, departamento VARCHAR(255) NOT NULL)")

def ingresar_departamentos(mycursor):
    departamentos = ["Antioquia","Valle del Cauca","Atlántico","Bolívar","Norte de Santander","Tolima","Meta","Santander","Magdalena","Cesar"]
    for departamento in departamentos:
        sql = "INSERT INTO departamentos (departamento) VALUES ('{}')".format(departamento)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")

def sexos(mycursor):
    mycursor.execute("CREATE TABLE sexos (id_sexo INT AUTO_INCREMENT PRIMARY KEY, sexo VARCHAR(255) NOT NULL)")

def ingresar_sexos(mycursor):
    sexos = ["Masculino","Femenino"]
    for sexo in sexos:
        sql = "INSERT INTO sexos (sexo) VALUES ('{}')".format(sexo)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")

def facturas(mycursor):
    mycursor.execute("CREATE TABLE facturas (id_factura INT AUTO_INCREMENT PRIMARY KEY, fecha DATE NOT NULL,id_cliente INT NOT NULL, FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente))")

def informaciondelascompras(mycursor):
    mycursor.execute("CREATE TABLE informaciondelascompras (id INT AUTO_INCREMENT PRIMARY KEY,id_producto INT NOT NULL, cantidad INT NOT NULL, id_factura INT NOT NULL, FOREIGN KEY (id_producto) REFERENCES productos(id_producto), FOREIGN KEY (id_factura) REFERENCES facturas(id_factura))")

def mostrar_tablas(mycursor):
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
def eliminar_tabla(mycursor,tabla):
    sql = "DROP TABLE "+tabla
    mycursor.execute(sql)

def rename_column(mycursor):
    #ALTER TABLE TableName RENAME COLUMN OldColumnName TO NewColumnName
    sql = "ALTER TABLE clientes RENAME COLUMN nombre_completo TO nombre"
    mycursor.execute(sql)



 

ingresar_clientes(mycursor)