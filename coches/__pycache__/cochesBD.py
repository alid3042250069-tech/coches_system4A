from conexionBD import conexion, cursor

class CochesBD():
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def insertar(self):
        try:
            cursor.execute("insert into coches values (NULL, %s, %s, %s, %s, %s, %s);", (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos))
            conexion.commit()
            return True
        except:
            return False

    def consultar(self):
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    def eliminar(self, id):
        try:
            cursor.execute("delete from coches where id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update coches set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s where id=%s", (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id))
            conexion.commit()
            return True
        except:
            return False


