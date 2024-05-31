# main.py

from menu import mostrar_menu
import inventario

def main():
    productos = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            inventario.ingresar_producto(productos)
        elif opcion == '2':
            inventario.editar_producto(productos)
        elif opcion == '3':
            inventario.eliminar_producto(productos)
        elif opcion == '4':
            inventario.listar_productos(productos)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
