def agregar(lista, producto):
    """Agrega un producto a la lista."""
    lista.append(producto)
    print(f"Producto '{producto}' agregado correctamente.")

def limpiar(lista):
    """Limpia toda la lista."""
    lista.clear()
    print("Lista limpiada correctamente.")

def remover(lista, producto):
    """Remueve un producto de la lista si existe."""
    try:
        lista.remove(producto)
        print(f"Producto '{producto}' eliminado correctamente.")
    except ValueError:
        print(f"El producto '{producto}' no se encuentra en la lista.")

def listar(lista):
    """Muestra todos los productos con su índice en la lista."""
    if lista:
        print("\nLista de productos:")
        for index, item in enumerate(lista):
            print(f"{index}: {item}")
    else:
        print("La lista está vacía.")

def editar(lista, index, nuevodato):
    """Edita un producto en la lista en base al índice dado."""
    if 0 <= index < len(lista):
        lista[index] = nuevodato
        print(f"Producto en el índice {index} actualizado a '{nuevodato}'.")
    else:
        print("Índice fuera de rango. No se pudo editar el producto.")


def ingresaData(msn, tipo='int'):
    """Solicita y valida la entrada de datos del usuario."""
    while True:
        try:
            opcion = input(msn).strip()
            if tipo == 'int':
                if opcion == "":
                    raise ValueError("Ingrese un valor")
                if not opcion.isdigit():
                    raise ValueError("Debe ingresar un número válido.")
                return int(opcion)
            elif tipo == 'str':
                if opcion == "":
                    raise ValueError("Ingrese un valor no vacío.")
                return opcion
        except ValueError as e:
            print(f"Error: {e}")

def shoppingList():
    """Función principal que maneja el menú y las operaciones de la lista de compras."""
    print("Bienvenido a la lista de compras")
    listaproducto = []

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Editar producto")
        print("3. Listar productos")
        print("4. Eliminar producto")
        print("5. Limpiar lista")
        print("6. Salir")
        
        opcion = ingresaData("Ingrese una opción: ")

        if opcion == 1:
            producto = ingresaData("Ingrese un producto: ", tipo='str')
            agregar(listaproducto, producto)
        elif opcion == 2:
            listar(listaproducto)
            index = ingresaData("Ingrese el índice del producto a editar: ")
            nuevodato = input("Ingrese el nuevo nombre del producto: ")
            editar(listaproducto, index, nuevodato)
        elif opcion == 3:
            listar(listaproducto)
        elif opcion == 4:
            producto = input("Ingrese el nombre del producto a eliminar: ")
            remover(listaproducto, producto)
        elif opcion == 5:
            limpiar(listaproducto)
        elif opcion == 6:
            print("Saliendo... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
if __name__=="__main__":
   shoppingList()

