from coches.conexionBD import conectar

class CochesBD():
    def __init__(self, marca="", color="", modelo="", velocidad=0, potencia=0, asientos=0):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.asientos = asientos

    def insertar(self):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "INSERT INTO coches (marca, color, modelo, velocidad, potencia, asientos) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos)
                cursor.execute(sql, valores)
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    def eliminar(self, id_coche):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "DELETE FROM coches WHERE id = %s"
                cursor.execute(sql, (id_coche,))
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    def modificar(self, id_coche):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "UPDATE coches SET marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s WHERE id = %s"
                valores = (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos, id_coche)
                cursor.execute(sql, valores)
                conexionBD.commit()
                cursor.close()
                conexionBD.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    def consultar(self):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                cursor.execute("SELECT * FROM coches")
                registros = cursor.fetchall()
                cursor.close()
                conexionBD.close()
                return registros
            else:
                return []
        except Exception as e:
            return []

    def buscar(self, id_coche):
        conexionBD = conectar()
        try:
            if conexionBD is not None:
                cursor = conexionBD.cursor()
                sql = "SELECT * FROM coches WHERE id = %s"
                cursor.execute(sql, (id_coche,))
                registros = cursor.fetchall()
                cursor.close()
                conexionBD.close()
                return registros
            else:
                return []
        except Exception as e:
            return []