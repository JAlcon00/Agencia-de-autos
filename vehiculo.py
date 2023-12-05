class Vehiculo:
    def __init__(self, nombre, marca, id_vehiculo):
        self._nombre = nombre
        self._marca = marca
        self._id_vehiculo = id_vehiculo

    def mostrar_detalle(self):
        return f"Vehiculo: {self._nombre} - Marca: {self._marca} - ID: {self._id_vehiculo}"

    def obtener_id(self):
        return self._id_vehiculo
