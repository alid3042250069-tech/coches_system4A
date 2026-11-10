import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='bd_coches',
        )
        return conexion
    except Exception as e:
        print("....Por el momento no es posible conectarse con la Base de Datos ¡intentelo mas tarde!")
        return None

#git branch, git branch -M main