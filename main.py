from automovil import Automovil
from contabilidad import Contabilidad

def main():
    """
        Función principal que ejecuta el menú de gestión de automóviles.

        Esta función presenta un menú con diversas opciones relacionadas con la gestión
        de automóviles y contabilidad. Permite al usuario realizar acciones como listar,
        obtener detalles, añadir, actualizar, y eliminar automóviles, además de ver las
        ganancias totales. El programa continúa ejecutándose hasta que el usuario decide
        salir seleccionando la opción correspondiente.
    """
    while True:
        # Mostrar opciones del menú.
        print("\nMenú de Gestión de Automóviles")
        print("1. Listar todos los automóviles")
        print("2. Obtener detalles de un automóvil")
        print("3. Añadir un nuevo automóvil")
        print("4. Actualizar un automóvil")
        print("5. Vender un automóvil")
        print("6. Ver ganancias totales")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        # Procesar la opción seleccionada por el usuario.
        if opcion == '1':
            # Listar todos los automóviles.
            autos = Automovil.get_all()
            if autos:
                for auto in autos:
                    print(auto)
            else:
                print("No se pudieron obtener los datos de los automóviles.")

        elif opcion == '2':
            # Obtener detalles de un automóvil específico.
            id_auto = input("Ingrese el ID del automóvil: ")
            auto = Automovil.get_by_id(id_auto)
            if auto:
                print(auto)
            else:
                print("No se pudo obtener el detalle del automóvil.")

        elif opcion == '3':
            # Añadir un nuevo automóvil.
            data = {
                "id_auto": input("ID del automóvil: "),
                "nombre": input("Nombre del automóvil: "),
                "marca": input("Marca del automóvil: "),
                "precio_venta": float(input("Precio de venta: ")),
                "precio_compra": float(input("Precio de compra: "))
            }
            resultado = Automovil.create(data)
            if resultado:
                print("Automóvil añadido con éxito.")
            else:
                print("No se pudo añadir el automóvil.")

        elif opcion == '4':
            # Actualizar un automóvil existente.
            id_auto = input("Ingrese el ID del automóvil a actualizar: ")
            data = {
                "nombre": input("Nuevo nombre del automóvil: "),
                "marca": input("Nueva marca del automóvil: "),
                "precio_venta": float(input("Nuevo precio de venta: ")),
                "precio_compra": float(input("Nuevo precio de compra: "))
            }
            if Automovil.update_auto(id_auto, data):
                print("Automóvil actualizado con éxito.")
            else:
                print("No se pudo actualizar el automóvil.")

        elif opcion == '5':
            # Vender un automóvil.
            id_auto = input("Ingrese el ID del automóvil a eliminar: ")
            if Automovil.delete_auto(id_auto):
                print("Automóvil vendido con éxito.")
            else:
                print("No se pudo vender el automóvil.")

        elif opcion == '6':
            # Mostrar las ganancias totales.
            Contabilidad.mostrar_resumen_financiero()

        elif opcion == '7':
            # Salir del programa.
            print("Saliendo del programa.")
            break

        else:
            # Opción no válida.
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

