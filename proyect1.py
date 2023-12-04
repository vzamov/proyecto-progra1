import time

def generar_sku(nombre):
    timestamp = int(time.time())  # Obtiene el tiempo actual en segundos desde Epoch
    return f"{nombre[:3].upper()}{timestamp}"

def incluir_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    sku = generar_sku(nombre)
    if nombre in inventario:
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio, 'SKU': sku}
    print(f"Producto incluido con éxito. SKU: {sku}")

def consultar_inventario(inventario):
    for producto, detalles in inventario.items():
        print(f"Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}, SKU: {detalles['SKU']}")
        if detalles['cantidad'] < 5:  # Suponiendo que 5 es el mínimo
            print(f"Alerta: El producto {producto} está por debajo del mínimo establecido.")

def consultar_producto_especifico(inventario):
    nombre = input("Ingrese el nombre del producto a consultar: ")
    if nombre in inventario:
        detalles = inventario[nombre]
        print(f"Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
    else:
        print("Producto no encontrado.")

def modificar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a modificar: ")
    if nombre in inventario:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print("Producto modificado con éxito.")
    else:
        print("Producto no encontrado.")

def borrar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a borrar: ")
    if nombre in inventario:
        del inventario[nombre]
        print("Producto borrado con éxito.")
    else:
        print("Producto no encontrado.")
def vender_producto(inventario):
    nombre = input("Ingrese el nombre del producto a vender: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    if nombre in inventario:
        if inventario[nombre]['cantidad'] >= cantidad_vendida:
            inventario[nombre]['cantidad'] -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de {nombre}.")
            if inventario[nombre]['cantidad'] < 5:
                print(f"Alerta: Quedan pocas unidades de {nombre} (menos de 5).")
        else:
            print("No hay suficientes unidades para vender.")
    else:
        print("Producto no encontrado.")

def mostrar_menu():
    print("1. Incluir")
    print("2. Consultar Todo el Inventario")
    print("3. Consultar Producto Específico")
    print("4. Modificar")
    print("5. Borrar")
    print("6. Vender")
    print("7. Salir")

def main():
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            incluir_producto(inventario)
        elif opcion == '2':
            consultar_inventario(inventario)
        elif opcion == '3':
            consultar_producto_especifico(inventario)
        elif opcion == '4':
            modificar_producto(inventario)
        elif opcion == '5':
            borrar_producto(inventario)
        elif opcion == '6':
            vender_producto(inventario)
        elif opcion == '7':
            print("Salir del programa")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
