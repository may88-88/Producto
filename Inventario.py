# Sistema de Gestión de Inventarios
# Autor: Marilyn Intriago
# Este programa permite agregar, eliminar y mostrar productos
# usando un diccionario como estructura de datos.

# Clase que representa un producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Atributos del producto
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para mostrar el producto en pantalla
    def __str__(self):
        return f"ID:{self.id} | Nombre:{self.nombre} | Cantidad:{self.cantidad} | Precio:${self.precio}"


# Clase que gestiona el inventario
class Inventario:
    def __init__(self):
        # Diccionario donde:
        # Clave = ID del producto (único)
        # Valor = Objeto Producto
        self.productos = {}

    # Método para agregar un producto
    def agregar(self, producto):
        if producto.id in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado correctamente.")

    # Método para eliminar un producto por ID
    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Método para mostrar todos los productos
    def mostrar(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos.values():
                print(p)


# Crear objeto inventario
inv = Inventario()

# Menú interactivo
while True:
    print("\n1. Agregar")
    print("2. Eliminar")
    print("3. Mostrar")
    print("4. Salir")

    op = input("Seleccione una opción: ")

    if op == "1":
        id = input("ID: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))  # Se convierte a entero
        precio = float(input("Precio: "))    # Se convierte a decimal
        inv.agregar(Producto(id, nombre, cantidad, precio))

    elif op == "2":
        inv.eliminar(input("ID: "))

    elif op == "3":
        inv.mostrar()

    elif op == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
