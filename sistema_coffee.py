import os

# Archivos de texto para persistencia de datos
ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"


def inicializar_archivos():
    """Crea los archivos con datos de prueba si no existen."""
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as f:
            f.write("1,Cafe Americano,5.00,20\n")
            f.write("2,Capuchino,7.50,15\n")
            f.write("3,Sandwich de Pollo,8.00,10\n")
            f.write("4,Empanada de Carne,4.50,12\n")

    if not os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as f:
            pass  # Crea el archivo vacío


def cargar_productos():
    """Lee el archivo productos.txt y retorna una lista con los productos."""
    productos = []
    if os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    # ID, Nombre, Precio, Stock
                    productos.append([partes[0], partes[1], float(partes[2]), int(partes[3])])
    return productos


def guardar_productos(productos):
    """Guarda la lista de productos actualizada en el archivo."""
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p[0]},{p[1]},{p[2]:.2f},{p[3]}\n")


def mostrar_inventario(productos):
    """Muestra la lista de productos y su stock disponible."""
    print("\n" + "=" * 55)
    print("        INVENTARIO CAFETERÍA COFFEE")
    print("=" * 55)
    print(f"{'ID':<5} {'Producto':<25} {'Precio (S/)':<12} {'Stock':<10}")
    print("-" * 55)
    for p in productos:
        print(f"{p[0]:<5} {p[1]:<25} {p[2]:<12.2f} {p[3]:<10}")
    print("-" * 55)


def registrar_venta(productos):
    """Procesa una venta, descuenta stock y registra la transacción."""
    mostrar_inventario(productos)
    id_prod = input("\nIngrese el ID del producto a vender: ").strip()

    encontrado = False
    for p in productos:
        if p[0] == id_prod:
            encontrado = True
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{p[1]}' a llevar: "))
            except ValueError:
                print("⚠️ Error: Debe ingresar un número entero válido.")
                return

            if cantidad <= 0:
                print("⚠️ La cantidad debe ser mayor a 0.")
                return

            if cantidad > p[3]:
                print(f"❌ Stock insuficiente. Solo quedan {p[3]} unidades.")
                return

            # Descontar stock
            p[3] -= cantidad
            total = cantidad * p[2]

            # Actualizar archivo de productos
            guardar_productos(productos)

            # Guardar registro en ventas.txt
            with open(ARCHIVO_VENTAS, "a", encoding="utf-8") as f:
                f.write(f"{p[0]},{p[1]},{cantidad},{total:.2f}\n")

            print(f"\n✅ ¡Venta registrada con éxito!")
            print(f"   Total a pagar: S/ {total:.2f}")
            break

    if not encontrado:
        print("❌ El ID ingresado no existe.")


def ver_ventas():
    """Muestra el historial acumulado de ventas."""
    print("\n" + "=" * 50)
    print("      HISTORIAL DE VENTAS REGISTRADAS")
    print("=" * 50)

    if not os.path.exists(ARCHIVO_VENTAS) or os.path.getsize(ARCHIVO_VENTAS) == 0:
        print("Aún no se han registrado ventas.")
        return

    print(f"{'ID':<5} {'Producto':<25} {'Cant.':<8} {'Total (S/)':<10}")
    print("-" * 50)
    total_general = 0.0
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split(",")
                cant = int(partes[2])
                tot = float(partes[3])
                total_general += tot
                print(f"{partes[0]:<5} {partes[1]:<25} {cant:<8} {tot:<10.2f}")
    print("-" * 50)
    print(f"INGRESOS TOTALES REGISTRADOS: S/ {total_general:.2f}")


def menu():
    """Menú principal del programa."""
    inicializar_archivos()

    while True:
        productos = cargar_productos()

        print("\n=================================")
        print("   SISTEMA CAFETERÍA COFFEE      ")
        print("=================================")
        print("1. Ver Inventario / Stock")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            mostrar_inventario(productos)
        elif opcion == "2":
            registrar_venta(productos)
        elif opcion == "3":
            ver_ventas()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()