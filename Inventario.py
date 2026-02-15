# Sistema de Inventario simple
# Se usa un diccionario para guardar los productos

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


# Diccionario {ID: Producto}
productos = {}

# Menú
while True:
    print("\n1. Agregar")
    print("2. Mostrar")
    print("3. Eliminar")
    print("4. Salir")

    opcion = input("Opción: ")

    # Agregar producto
    if opcion == "1":
        id = input("ID: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        if id in productos:
            print("El ID ya existe")
        else:
            productos[id] = Producto(id, nombre, cantidad, precio)
            print("Producto guardado")

    # Mostrar productos
    elif opcion == "2":
        if not productos:
            print("Inventario vacío")
        else:
            for p in productos.values():
                print(p.id, p.nombre, p.cantidad, p.precio)

    # Eliminar producto
    elif opcion == "3":
        id = input("ID a eliminar: ")
        if id in productos:
            del productos[id]   # Se elimina del diccionario
            print("Producto eliminado")
        else:
            print("Producto no encontrado")

    # Salir
    elif opcion == "4":
        print("Fin del programa")
        break

    else:
        print("Opción incorrecta")
