# inventario.py

def ingresar_producto(productos):
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    productos[nombre] = {'cantidad': cantidad, 'precio': precio}
    print("Producto ingresado exitosamente.")

def editar_producto(productos):
    nombre = input("Nombre del producto a editar: ")
    if nombre in productos:
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        productos[nombre] = {'cantidad': cantidad, 'precio': precio}
        print("Producto editado exitosamente.")
    else:
        print("Producto no encontrado.")

def eliminar_producto(productos):
    nombre = input("Nombre del producto a eliminar: ")
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado exitosamente.")
    else:
        print("Producto no encontrado.")

def listar_productos(productos):
    if productos:
        for nombre, detalles in productos.items():
            print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
    else:
        print("No hay productos en el inventario.")
