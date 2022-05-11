class Tables:
    def productos(mycursor):
        mycursor.execute("CREATE TABLE productos (id_producto INT AUTO_INCREMENT PRIMARY KEY, nombre_producto VARCHAR(255) NOT NULL, detalle_producto VARCHAR(255) NOT NULL, precio_unitario INT NOT NULL)")

    def clientes(mycursor):
        mycursor.execute("CREATE TABLE productos (id_cliente INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, apellido VARCHAR(255) NOT NULL, direccion VARCHAR(255) NOT NULL, nombre VARCHAR(255) NOT NULL, ciudad VARCHAR(255) NOT NULL, precio_unitario INT NOT NULL)")

    def ciudades(mycursor):
        mycursor.execute("CREATE TABLE ciudades (id_cuidad INT AUTO_INCREMENT PRIMARY KEY, ciudad VARCHAR(255) NOT NULL)")

    def ciudades(mycursor):
        mycursor.execute("CREATE TABLE ciudades (id_cuidad INT AUTO_INCREMENT PRIMARY KEY, ciudad VARCHAR(255) NOT NULL)")



