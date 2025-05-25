def ingresar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria == "":
            print("La categoría no puede estar vacía.")
            continue
        
        try:
            precio = input("Ingrese el precio (sin centavos): ").strip()
            if precio == "":
                print("El precio no puede estar vacío.")
                continue
            precio = int(precio)
            if precio < 0:
                print("El precio debe ser un número positivo.")
                continue
        except ValueError:
            print("El precio debe ser un número entero válido.")
            continue
        
        return [nombre, categoria, precio]

def mostrar_productos(lista_productos):
    if not lista_productos:
        print("No hay productos registrados.")
        return
    
    print("\nProductos registrados:")
    for i, producto in enumerate(lista_productos, start=1):
        nombre, categoria, precio = producto
        print(f"{i}. Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")

def buscar_producto(lista_productos):
    busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    if busqueda == "":
        print("La búsqueda no puede estar vacía.")
        return
    
    encontrados = []
    for producto in lista_productos:
        nombre, categoria, precio = producto
        if busqueda in nombre.lower():
            encontrados.append(producto)
    
    if encontrados:
        print("\nProductos encontrados:")
        for i, producto in enumerate(encontrados, start=1):
            nombre, categoria, precio = producto
            print(f"{i}. Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
    else:
        print("No se encontraron productos con ese nombre.")

def eliminar_producto(lista_productos):
    if not lista_productos:
        print("No hay productos para eliminar.")
        return
    
    mostrar_productos(lista_productos)
    while True:
        num = input("Ingrese el número del producto que desea eliminar: ").strip()
        if num == "":
            print("La entrada no puede estar vacía.")
            continue
        
        try:
            num = int(num)
            if 1 <= num <= len(lista_productos):
                eliminado = lista_productos.pop(num - 1)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                break
            else:
                print(f"Ingrese un número entre 1 y {len(lista_productos)}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    lista_productos = []
    
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Ingresar un nuevo producto")
        print("2. Mostrar productos registrados")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto por número")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            producto = ingresar_producto()
            lista_productos.append(producto)
            print("Producto agregado correctamente.")
        elif opcion == "2":
            mostrar_productos(lista_productos)
        elif opcion == "3":
            buscar_producto(lista_productos)
        elif opcion == "4":
            eliminar_producto(lista_productos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
