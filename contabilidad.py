import requests

class Contabilidad:
    # URL para acceder al servicio web que provee información de ganancias.
    GANANCIAS_URL = "https://jalcon00.pythonanywhere.com/ganancias/balance"

    @staticmethod
    def obtener_resumen_financiero():
        """
        Obtiene el total de ganancias desde el servicio web.

        Este método realiza una solicitud GET a la URL especificada en la variable
        GANANCIAS_URL. Si la respuesta es exitosa (código 200), retorna el balance
        de ganancias obtenido. En caso contrario, imprime un mensaje de error
        y retorna None.

        Returns:
            float or None: El balance total de ganancias si la solicitud es exitosa,
                           de lo contrario, None.
        """
        response = requests.get(Contabilidad.GANANCIAS_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener el resumen financiero.")
            return None

    @staticmethod
    def mostrar_resumen_financiero():
        """
        Muestra las ganancias totales obtenidas desde el servicio web.

        Este método utiliza obtener_ganancias_totales para obtener el total de
        ganancias y luego lo imprime. Si no se pueden obtener las ganancias (el método
        retorna None), se imprime un mensaje de error.

        Este método no retorna ningún valor.
        """
        resumen = Contabilidad.obtener_resumen_financiero()
        if resumen:
            print("\n---------------------- RESUMEN ----------------------")
            print(f" Total Invertido:           {resumen.get('total_precio_compra'):>10}")
            print(f" Total Precio de Venta:     {resumen.get('total_precio_venta'):>10}")
            print("------------------------------------------------------")
            print(f" Ganancias Totales:         {resumen.get('balance_ganancias'):>10}")
            print("------------------------------------------------------\n")
        else:
            print("\nError al obtener el resumen financiero.")
