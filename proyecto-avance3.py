import time

def generar_sku(nombre):
    timestamp = int(time.time())
    return f"{nombre[:3].upper()}{timestamp}"

def incluir_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    sku = generar_sku(nombre)
    producto_existente = next((item for item in inventario if item['nombre'] == nombre), None)
    if producto_existente:
        producto_existente['cantidad'] += cantidad
    else:
        inventario.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio, 'SKU': sku})
    print(f"Producto incluido con éxito. SKU: {sku}")

def consultar_inventario(inventario):
    for producto in inventario:
        print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, SKU: {producto['SKU']}")
        if producto['cantidad'] < 5:
            print(f"Alerta: El producto {producto['nombre']} está por debajo del mínimo establecido.")


def buscar_por_nombre(inventario, nombre_buscado):
    productos_encontrados = [producto for producto in inventario if nombre_buscado.lower() in producto['nombre'].lower()]
    if productos_encontrados:
        for producto in productos_encontrados:
            print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, SKU: {producto['SKU']}")
    else:
        print("No se encontraron productos con ese nombre.")

def buscar_por_sku(inventario, sku_buscado):
    producto_encontrado = next((producto for producto in inventario if producto['SKU'] == sku_buscado), None)
    if producto_encontrado:
        print(f"Producto: {producto_encontrado['nombre']}, Cantidad: {producto_encontrado['cantidad']}, Precio: {producto_encontrado['precio']}, SKU: {producto_encontrado['SKU']}")
    else:
        print("Producto no encontrado con ese SKU.")

def consultar_producto_especifico(inventario):
    print("Buscar por: 1. Nombre 2. SKU")
    opcion_busqueda = input("Seleccione una opción: ")
    if opcion_busqueda == '1':
        nombre_buscado = input("Ingrese parte del nombre del producto a buscar: ")
        buscar_por_nombre(inventario, nombre_buscado)
    elif opcion_busqueda == '2':
        sku_buscado = input("Ingrese el SKU del producto a buscar: ")
        buscar_por_sku(inventario, sku_buscado)
    else:
        print("Opción no válida.")


def modificar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a modificar: ")
    producto_encontrado = next((item for item in inventario if item['nombre'] == nombre), None)
    if producto_encontrado:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        producto_encontrado['cantidad'] = cantidad
        producto_encontrado['precio'] = precio
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
    inventario = []  # Lista para almacenar los productos
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
