class Productos:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
class Detalle_venta:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = precio * cantidad
class Venta:
    def __init__(self):
        self.productos = []
    def añadir_producto_venta(self, nombre, cantidad, precio):
        detalle = Detalle_venta(nombre, cantidad, precio)
        self.productos.append(detalle)
    def calcular_total(self):
        return sum(n.subtotal for n in self.productos)
class Registro_venta:
    def __init__(self):
        self.ventas = []
    def añadir_venta(self, venta):
        self.ventas.append(venta)
informacion_de_productos = [("1", "Cafe Americano", 5.00, 20),("2", "Capuchino", 7.50, 15),("3", "Sandwich de Pollo", 8.00, 10),
("4", "Empanada de Carne", 4.50, 12),("5", "Frapuccino", 6.00, 8),("6", "Jugo Natural", 5.50, 14),("7", "Orejitas", 2.50, 20),
("8", "Alfajores", 3.00, 15),("9", "Empanadas de Pollo", 4.00, 10)
]
producto = [Productos(*n) for n in informacion_de_productos]
registro = Registro_venta()
def añadir_producto():
    id = input("Ingrese el ID del producto: ")
    while any(n.id == id for n in producto):
        print("El ID ya existe. Por favor, ingrese un ID único.")
        id =(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    while any(n.nombre.lower() == nombre.lower() for n in producto):
        print("El nombre del producto ya existe. Por favor, ingrese un nombre único.")
        nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock del producto: "))
    nuevo_producto = Productos(id, nombre, precio, stock)
    producto.append(nuevo_producto)
    print(f"Producto {nombre} agregado exitosamente.")
def mostrar_productos():
    print("Lista de productos:")
    for n in producto:
        print(f"ID: {n.id}, Nombre: {n.nombre}, Precio: ${n.precio:.2f}, Stock: {n.stock}")
def registrar_venta():
    nueva_venta = Venta()
    mostrar_productos()
    n_ordenes = int(input("¿Cuántos productos desea registrar?: "))
    for n in range(n_ordenes):
        id_producto = input("Ingrese el ID del producto a registrar: ")
        producto_encontrado = None
        for n in producto:
            if n.id == id_producto:
                producto_encontrado = n
                break
        if producto_encontrado is None:
            print("Producto no encontrado.")
            continue
        cantidad = int(input("Ingrese la cantidad que desea registrar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            continue
        if cantidad > producto_encontrado.stock:
            print("No hay suficiente stock.")
            continue
        nueva_venta.añadir_producto_venta(producto_encontrado.nombre,cantidad,producto_encontrado.precio)
        producto_encontrado.stock -= cantidad
    if nueva_venta.productos:
        registro.añadir_venta(nueva_venta)
        print("\nVenta registrada exitosamente.")
        print(f"Total de la compra: S/ {nueva_venta.calcular_total():.2f}")
    else:
        print("No se registró ninguna venta.")
def mostrar_historial():
    if not registro.ventas:
        print("No hay ventas registradas.")
        return
    print("\n========== HISTORIAL DE VENTAS ==========")
    for i, venta in enumerate(registro.ventas, start=1):
        print(f"\nVenta N.° {i}")
        print("----------------------------------------")
        for detalle in venta.productos:
            print(f"Producto: {detalle.nombre}")
            print(f"Cantidad: {detalle.cantidad}")
            print(f"Precio unitario: S/ {detalle.precio:.2f}")
            print(f"Subtotal: S/ {detalle.subtotal:.2f}")
            print("----------------------------------------")
        print(f"Total de la venta: S/ {venta.calcular_total():.2f}")
        print("========================================")
def menu():
    while True:
        print("\n========== SISTEMA DE CAFETERÍA ==========")
        print("1. Registrar venta")
        print("2. Mostrar productos")
        print("3. Añadir producto")
        print("4. Historial de ventas")
        print("5. Salir")
        print("==========================================")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrar_venta()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            añadir_producto()
        elif opcion == 4:
            mostrar_historial()
        elif opcion == 5:
            break
        else:
            print("Opción inválida")
menu()