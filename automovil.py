import requests

class Automovil:
    # URL base para acceder al servicio web de automóviles.
    BASE_URL = "https://jalcon00.pythonanywhere.com/automoviles"

    @staticmethod
    def get_all():
        """
        Obtiene todos los automóviles disponibles desde el servicio web.

        Este método realiza una solicitud GET a la URL BASE_URL. Si la respuesta
        es exitosa (código 200), retorna un JSON con la lista de automóviles.
        En caso contrario, imprime un mensaje de error y retorna None.

        Returns:
            list or None: Una lista de automóviles si la solicitud es exitosa,
                          de lo contrario, None.
        """
        response = requests.get(Automovil.BASE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener los automóviles.")
            return None

    @staticmethod
    def get_by_id(id_auto):
        """
        Obtiene un automóvil específico por su ID desde el servicio web.

        Este método realiza una solicitud GET a la URL BASE_URL seguida del ID
        del automóvil. Si la respuesta es exitosa (código 200), retorna un JSON
        con los detalles del automóvil. En caso contrario, imprime un mensaje de
        error y retorna None.

        Args:
            id_auto (int): El ID del automóvil a obtener.

        Returns:
            dict or None: Un diccionario con la información del automóvil si la
                          solicitud es exitosa, de lo contrario, None.
        """
        response = requests.get(f"{Automovil.BASE_URL}/{id_auto}")
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener el automóvil.")
            return None

    @staticmethod
    def create(data):
        """
        Crea un nuevo automóvil en el servicio web.

        Este método realiza una solicitud POST a la URL BASE_URL con los datos
        del nuevo automóvil en formato JSON. Si la respuesta es exitosa (código 201),
        retorna el JSON con los detalles del automóvil creado. De lo contrario,
        imprime un mensaje de error y retorna None.

        Args:
            data (dict): Un diccionario con los datos del automóvil a crear.

        Returns:
            dict or None: Un diccionario con la información del automóvil creado si
                          la solicitud es exitosa, de lo contrario, None.
        """
        response = requests.post(Automovil.BASE_URL, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            print("Error al añadir el automóvil.")
            return None

    @staticmethod
    def update_auto(id_auto, data):
        """
        Actualiza la información de un automóvil específico en el servicio web.

        Este método realiza una solicitud PUT a la URL BASE_URL seguida del ID
        del automóvil, con los datos actualizados en formato JSON. Si la respuesta
        es exitosa (código 200), retorna True. En caso contrario, imprime un mensaje
        de error y retorna False.

        Args:
            id_auto (int): El ID del automóvil a actualizar.
            data (dict): Un diccionario con los datos actualizados del automóvil.

        Returns:
            bool: True si la actualización es exitosa, de lo contrario False.
        """
        response = requests.put(f"{Automovil.BASE_URL}/{id_auto}", json=data)
        if response.status_code == 200:
            return True
        else:
            print("Error al actualizar el automóvil.")
            return False

    @staticmethod
    def delete_auto(id_auto):
        """
        Elimina un automóvil específico del servicio web.

        Este método realiza una solicitud DELETE a la URL BASE_URL seguida del ID
        del automóvil. Si la respuesta es exitosa (código 200), retorna un JSON
        confirmando la eliminación. De lo contrario, imprime un mensaje de error
        y retorna None.

        Args:
            id_auto (int): El ID del automóvil a eliminar.

        Returns:
            dict or None: Un diccionario confirmando la eliminación si la solicitud
                          es exitosa, de lo contrario, None.
        """
        response = requests.delete(f"{Automovil.BASE_URL}/{id_auto}")
        if response.status_code == 200:
            return response
