class Productos:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Venta_unica:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = self.producto.precio * self.cantidad

class Venta_total:
    def __init__(self,ventas_unicas):
        self.productos = ventas_unicas

class Registro_ventas:
    def __init__(self,ventas_totales):
        self.ventas = ventas_totales
    
informacion_de_productos = [["001", "Cafe Americano", 5.00, 20],["002", "Capuchino", 7.50, 15],["003", "Sandwich de Pollo", 8.00, 10],
["004", "Empanada de Carne", 4.50, 12],["005", "Frapuccino", 6.00, 8],["006", "Jugo Natural", 5.50, 14],["007", "Orejitas", 2.50, 20],
["008", "Alfajores", 3.00, 15],["009", "Empanadas de Pollo", 4.00, 10]]

producto = [Productos(*n) for n in informacion_de_productos]

registro = Registro_ventas([])

def añadir_producto():
    try:
        id = int(input("Ingrese el ID del producto: ").strip().upper())
        if any(n.id == id for n in producto):
            print("El ID ya existe")
            return
        nombre = input("Ingrese el nombre del producto: ").capitalize()
        if any(n.nombre.lower() == nombre.lower() for n in producto):
            print("El nombre del producto ya existe. Por favor, ingrese un nombre único")
            return
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("El precio debe ser mayor que cero")
            return
        stock = int(input("Ingrese la cantidad de stock del producto: "))
        if stock < 0:
            print("La cantidad de stock no puede ser negativa")
            return
    except ValueError:
        print("Error: Ingrese valores válidos")
        return
    nuevo_producto = Productos(id, nombre, precio, stock)
    producto.append(nuevo_producto)
    print(f"\n" + "-"*60)
    print(f"{"ID":<10}{"PRODUCTO":<20}{"PRECIO":>13}{"STOCK":>13}")
    print("-"*60)
    print(f"{nuevo_producto.id:<10}{nuevo_producto.nombre:<20}{nuevo_producto.precio:>12.2f}{nuevo_producto.stock:>12}")
    print("-"*60)
    print(f"\nProducto {nombre} agregado exitosamente")

def mostrar_productos():
    print("\nINVENTARIO DE PRODUCTOS")
    if len(producto)==0:
            print("no existen productos registrados")
            return
    print("-"*60)
    print(f"{"ID":<10}{"PRODUCTO":<20}{"PRECIO":>13}{"STOCK":>13}")
    print("-"*60)
    for n in producto:
        print(f"{n.id:<10}{n.nombre:<20}{n.precio:>12.2f}{n.stock:>12}")
        print("-"*60)

def eliminar_producto():
    id = input("Ingrese el ID del producto a eliminar: ").strip().upper()
    for n in producto:
        if n.id == id:
            producto.remove(n)
            print(f"Producto {n.nombre} eliminado exitosamente")
            return
    print("Producto no encontrado")

def registrar_venta():
    nueva_venta = Venta_total([])
    mostrar_productos()
    try:
        n_ordenes = int(input("¿Cuántos productos desea registrar?: "))
        if n_ordenes <= 0:
            print("La cantidad de productos a registrar debe ser mayor que cero")
            return
        for n in range(n_ordenes):
            id_producto = input("Ingrese el ID del producto a registrar: ").strip().upper()
            producto_encontrado = None
            for n in producto:
                if n.id == id_producto:
                    producto_encontrado = n
            if producto_encontrado is None:
                print("Producto no encontrado")
                return
            cantidad = int(input("Ingrese la cantidad que desea registrar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero")
                return
            if cantidad > producto_encontrado.stock:
                print(f"No hay suficiente stock. Stock disponible: {producto_encontrado.stock}")
                return
    except ValueError:
        print("Error: Ingrese valores válidos")
        return
    venta_unica = Venta_unica(producto_encontrado, cantidad)
    nueva_venta.productos.append(venta_unica)
    producto_encontrado.stock -= cantidad
    registro.ventas.append(nueva_venta)
    print("Venta registrada exitosamente")

def modificar_producto():
    print("-"*36)
    print(f"{"ID":<10}{"PRODUCTO":<20}")
    print("-"*36)
    for n in producto:
        print(f"{n.id:<10}{n.nombre:<20}")
        print("-"*36)
    id = input("Ingrese el ID del producto a modificar: ").strip().upper()
    for n in producto:
        if n.id == id:
            print(f"Producto encontrado: {n.nombre}")
            print(f"Precio actual: {n.precio} - Stock actual: {n.stock}")
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                if nuevo_precio <= 0:
                            print("El precio debe ser mayor que cero.")
                            return
                n.precio = nuevo_precio
                nueva_cantidad = int(input("Ingrese la nueva cantidad de stock del producto: "))
                if nueva_cantidad < 0:
                    print("La cantidad de stock no puede ser negativa")
                    return
                n.stock = nueva_cantidad
            except ValueError:
                print("Error: Ingrese valores válidos")
                return
            print(f"Producto {n.nombre} modificado exitosamente.")
            print(f"Precio actualizado: {n.precio} - Stock actualizado: {n.stock}")
            return
    print("Producto no encontrado.")

def mostrar_historial_ventas():
    total = 0
    if registro.ventas == []:
        print("No hay ventas registradas")
        return
    print("\nHISTORIAL DE VENTAS")
    for i, venta in enumerate(registro.ventas):
        print("-"*60)
        print(f"Venta N.° {i+1}")
        print("-"*60)
        for venta_p in venta.productos:
            print(f"Producto: {venta_p.producto.nombre} - Cantidad: {venta_p.cantidad} - Subtotal: ${venta_p.subtotal:.2f}")
            total += venta_p.subtotal
        print("-"*60)
        print(f"Total de la venta: ${total:.2f}")

def menu():
    while True:
        print("\n" + "-"*10 + " SISTEMA DE CAFETERÍA " + "-"*10)
        print("1. Registrar venta")
        print("2. Mostrar productos")
        print("3. Añadir producto")
        print("4. Eliminar producto")
        print("5. Modificar producto")
        print("6. Historial de ventas")
        print("7. Salir")
        print("-"*42)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrar_venta()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            añadir_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            modificar_producto()
        elif opcion == 6:
            mostrar_historial_ventas()
        elif opcion == 7:
            break
        else:
            print("Opción inválida")
menu()