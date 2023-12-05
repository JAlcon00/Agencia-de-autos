class Almacen:
    def __init__(self):
        self._autos = []

    def agregar_auto(self, auto):
        self._autos.append(auto)

    def eliminar_auto(self, id_auto):
        self._autos = [auto for auto in self._autos if auto.obtener_id() != id_auto]

    def mostrar_stock(self):
        return "\n".join(auto.mostrar_detalle() for auto in self._autos)

    def valor_total_stock(self):
        return sum(auto.obtener_precio_venta() for auto in self._autos)
