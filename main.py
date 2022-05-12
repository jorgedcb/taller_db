from curses.ascii import CR
from re import S
from select import select
import mysql.connector
import random
import time
import datetime

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
    nombres = ["Alex","Andrea","Andy","Ariel","Akira","Azul","Billie","Charlie","Cris","Cruz","Dani","Denis","Eider","Gaby","Gael","Luján","Mel","Milán","Nicky","Noa"]
    apellidos = ["Pérez","Sánchez","Ramírez","Torres","Flores","Rivera","Gómez","Díaz","Reyes","Cruz","Morales","Ortiz","Gutiérrez","García","Rodríguez","Martínez","Hernández","López","González","Castilla"]
    direcciones = [("Cr 81 No. 32-60 AP 103", "Medellín"),("Cr 81 No. 32-60 AP 103","Medellín"),("Cr.86 45 aa59", "Medellín"),("Cl 47 No. 29-33 OF 508","Bucaramanga"),("Cr 28 No. 19-107","Cali"),("Cl 32 No. 25-43","Bucaramanga"),("Cl 73 No. 25-09","Bogotá"),("Av 3 No. 28-59","Cartagena"),("Cr 67 No. 167-61 OF 418","Bogotá"),("Cl 41 No. 7-05","Valledupar"),("Cr 57 No. 98-74","Barranquilla"),("Cl 14 No. 2-49 - Palacio Municipal","Santa marta"),("CRA 7N No. 131-99 MZ 15 T8 APTO 405","Barranquilla"),("CRA 38 N° 84-105 BLOQUE 1 APTO 303","Barranquilla"),("Cl 80 No. 8-44","Bogotá"),("Cr 82 No. 35-55 INT 202","Medellín"),("Cl 45 No. 1-06","Bucaramanga"),("Cl 7 No. 22-98 APTO. 2","Cali"),("Cr. 9 No. 10-41","Santa Marta"),("Cl 58 A No. 1-1","Cali")]
    var= []
    list1 = [1,2]
    random.choice(list1)
    for i in range(20):
        ciudad = direcciones[i][1]
        sql = "SELECT id_ciudad,id_departamento FROM ciudades WHERE ciudad ='{}'".format(ciudad)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        sex = random.choice(list1)
        tu = (nombres[i],apellidos[i],direcciones[i][0],myresult[0][0],myresult[0][1],sex)
        var.append(tu)    
    sql = "INSERT INTO clientes (nombre, apellido, direccion, id_ciudad, id_departamento,id_sexo) VALUES (%s, %s, %s,%s, %s, %s)"
    mycursor.executemany(sql, var)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


    

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
    
def ingresar_facturas(mycursor):
    sql = "INSERT INTO facturas (fecha, id_cliente) VALUES (%s, %s)"
    dias=list(range(1,30+1))
    clientes = list(range(1,20+1))
    
    val = []
    for i in range(20):
        dia = random.choice(dias)
        fecha = '2022-05-'+str(dia)
        print(fecha)
        tu = (fecha,random.choice(clientes))
        val.append(tu)
    
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

def informaciondelascompras(mycursor):
    mycursor.execute("CREATE TABLE informaciondelascompras (id INT AUTO_INCREMENT PRIMARY KEY,id_producto INT NOT NULL, cantidad INT NOT NULL, id_factura INT NOT NULL, FOREIGN KEY (id_producto) REFERENCES productos(id_producto), FOREIGN KEY (id_factura) REFERENCES facturas(id_factura))")
    
def ingresar_informaciondelascompras(mycursor):
    sql = "INSERT INTO informaciondelascompras (id_producto,cantidad,id_factura) VALUES (%s, %s, %s)"
    l =list(range(1,20+1))
    val = []
    for i in range(200):
        tu = (random.choice(l),random.choice(l),random.choice(l))
        val.append(tu)
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
    
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

#Listado de nombre producto de los productos cuyo precio es mayor a cierto rango.
def productos_mayor(mycursor,rango):
    sql = "SELECT nombre_producto FROM productos WHERE precio_unitario >{}".format(rango)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])

#Listado con todos los productos comprados por un cliente en particular. Se debe mostrar: fecha compra, Nombre y apellido del comprador, ciudad, departamento, producto comprado y cantidad. Ordenar por fecha y valor de compra.
def productos_cliente(mycursor,id):
    
    sql = "SELECT  clientes.nombre, clientes.apellido, ciudades.ciudad, departamentos.departamento FROM ((clientes INNER JOIN  ciudades ON clientes.id_ciudad = ciudades.id_ciudad)INNER JOIN departamentos ON clientes.id_departamento= departamentos.id_departamento) where id_cliente = {}".format(id)
    
    mycursor.execute(sql)
    cl = mycursor.fetchall()
    print("Nombre: ",cl[0][0])
    print("apellido: ",cl[0][1])
    print("Ciudad: ",cl[0][2])
    print("Departamento: ",cl[0][3])
    sql="SELECT facturas.fecha, productos.nombre_producto,informaciondelascompras.cantidad FROM ((informaciondelascompras INNER JOIN productos ON informaciondelascompras.id_producto=productos.id_producto) INNER JOIN facturas ON informaciondelascompras.id_factura=facturas.id_factura) WHERE facturas.id_cliente = {} ORDER BY  facturas.fecha,productos.precio_unitario  DESC;".format(id)
    mycursor.execute(sql)
    info = mycursor.fetchall()
    for x in info:
        print("Fecha: ",x[0])
        print("Producto : ",x[1])
        print("cantidad : ",x[2])
        print("")
#El nombre de la persona, nombre producto y precio de quién compró el producto comprado más caro
def producto_mas_caro(mycursor):
    sql="SELECT  facturas.id_cliente,productos.nombre_producto,productos.precio_unitario FROM ((informaciondelascompras INNER JOIN productos ON informaciondelascompras.id_producto=productos.id_producto) INNER JOIN facturas ON informaciondelascompras.id_factura=facturas.id_factura) WHERE productos.precio_unitario = (SELECT MAX(precio_unitario) FROM productos) GROUP BY facturas.id_cliente"
    mycursor.execute(sql)
    info = mycursor.fetchall()
    for x in info:
        sql="SELECT  nombre,apellido FROM clientes WHERE id_cliente={}".format(x[0])
        mycursor.execute(sql)
        cl = mycursor.fetchall()
        print("Nombre Cliente: ",cl[0][0])
        print("Apellido Cliente: ",cl[0][1])
        print("Producto: ",x[1])
        print("Precio: ",x[2])
        print("")

#Obtener los nombres, cédulas, sexo, nombre de producto, cantidad, precio unitario y precio total que se pagó por cada uno de los productos comprados.
def informacion_productos(mycursor):
    for i in range(1,20+1):
        sql="SELECT nombre_producto FROM productos WHERE id_producto={}".format(i)
        mycursor.execute(sql)
        p = mycursor.fetchall()
        print("")
        print("Producto: ",p[0][0])
        for j in range(1,20+1):
            sql="SELECT nombre,apellido,id_sexo FROM clientes WHERE id_cliente={}".format(j)
            mycursor.execute(sql)
            cl = mycursor.fetchall()
            print("Nombre Cliente: ",cl[0][0])
            print("Apellido Cliente: ",cl[0][1])
            sql="SELECT sexo FROM sexos WHERE id_sexo={}".format(cl[0][2])
            mycursor.execute(sql)
            se = mycursor.fetchall()
            print("Sexo Cliente: ",se[0][0])
    
            sql = "SELECT  sum(informaciondelascompras.cantidad), productos.precio_unitario, sum(informaciondelascompras.cantidad)* productos.precio_unitario AS precio_total FROM ((informaciondelascompras INNER JOIN productos ON informaciondelascompras.id_producto=productos.id_producto) INNER JOIN facturas ON informaciondelascompras.id_factura=facturas.id_factura) WHERE facturas.id_cliente = 13 and productos.id_producto = 1 GROUP BY productos.id_producto "

            
            mycursor.execute(sql)
            info = mycursor.fetchall()
            print("Cantidad: ",info[0][0])
            print("Precio unitario: ",info[0][1])
            print("Precio Total: ",info[0][2])

#Obtener los productos comprados por cierto cliente en un rango de fechas determinada. Se debe indicar: Nombre y apellido del comprador y nombre del producto y precio.
def productos_clientes(mycursor,id,inicio,final):
    sql="SELECT nombre,apellido,id_sexo FROM clientes WHERE id_cliente={}".format(id)
    mycursor.execute(sql)
    cl = mycursor.fetchall()
    print("Nombre Cliente: ",cl[0][0])
    print("Apellido Cliente: ",cl[0][1])
    sql="SELECT  facturas.fecha, productos.nombre_producto, productos.precio_unitario FROM ((informaciondelascompras INNER JOIN productos ON informaciondelascompras.id_producto=productos.id_producto) INNER JOIN facturas ON informaciondelascompras.id_factura=facturas.id_factura) WHERE facturas.fecha BETWEEN '{}' AND '{}' AND facturas.id_cliente = {}".format(inicio,final,id)
    mycursor.execute(sql)
    info = mycursor.fetchall()
    for x in info:
        print("")
        print("Fecha: ",x[0])
        print("Nombre del producto: ",x[1])
        print("Precio del producto: ",x[2])
#Obtener el nombre del producto más comprado (Mostrar nombre producto y cantidad de veces)
def producto_mas_comprado(mycursor):
    sql="SELECT  productos.nombre_producto, sum(informaciondelascompras.cantidad) as cantidad_total FROM ((informaciondelascompras INNER JOIN productos ON informaciondelascompras.id_producto=productos.id_producto) INNER JOIN facturas ON informaciondelascompras.id_factura=facturas.id_factura) GROUP BY productos.id_producto ORDER BY cantidad_total  DESC LIMIT 1;"
    mycursor.execute(sql)
    p = mycursor.fetchall()
    print("El producto mas comprado fue ",p[0][0],p[0][1]," veces")

#Desde un programa en JAVA/PYTHON realice un programa que muestre una tabla con el género y el valor total de las compras de cada género.Adicionalmente, un muestre un mensaje con el género que compró más: Hombres o Mujeres. 

def cantidad_genero(mycursor):
    sql="SELECT  clientes.id_sexo, sum(informaciondelascompras.cantidad) as cantidad_total FROM ((facturas INNER JOIN clientes ON facturas.id_cliente= clientes.id_cliente) INNER JOIN informaciondelascompras  ON facturas.id_factura=informaciondelascompras.id_factura)GROUP BY clientes.id_sexo ORDER BY cantidad_total  ASC"
    mycursor.execute(sql)
    s = mycursor.fetchall()
    for x in s:
        sql = "SELECT  sexo from sexos WHERE id_sexo = {}".format(x[0])
        mycursor.execute(sql)
        g = mycursor.fetchall()
        print("El sexo ",g[0][0],"realizo un total de compras de: ",x[1])
    print("El sexo que mas realizo compras fue: ",g[0][0])
# #1
# productos_mayor(mycursor,3000)
# #2
# productos_cliente(mycursor,13)
# #3
# producto_mas_caro(mycursor)
# #4 
# informacion_productos(mycursor)
# #5 
#productos_clientes(mycursor,13,'2022-01-01','2023-01-01')
# #6
# producto_mas_comprado(mycursor)
cantidad_genero(mycursor)

mydb.close()
mycursor.close()



