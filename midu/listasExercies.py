import random

# ------------------------- CREAR -------------------------

# Crear una lista de frutas
def listaFruta():
    return [random.randint(1, 100) for _ in range(10)]

# Crear lista vacía con nombres ingresados por el usuario
def ingresedata(msn):
    while True:
        try:
            nombre = input(msn).strip()
            if not nombre:
                raise ValueError("Nombre vacío") 
            if nombre.isdigit():
                raise ValueError("Es un valor numérico")
            return nombre
        except ValueError as e:
            print(f"Error: {e}")

def listavacia():
    listas = []
    for i in range(5):
        valor = ingresedata(f"Ingrese el nombre {i+1} \n")
        listas.append(valor.capitalize())
    return listas

# ------------------------- LEER -------------------------

# Lista original de nombres
nombres = [
    "Ana", "Luis", "María", "Carlos", "Elena", "Elena",
    "Pedro", "Lucía", "Javier", "Sofía", "Diego"
]

# Leer todos los elementos
def leer(lista):
    return [x for x in lista]

# Leer primero, medio y último
def elementos(lista):
    copy = lista[:]
    primero, *medio, ultimo = copy
    elemento_medio = medio[len(medio)//2] if medio else None
    return primero, elemento_medio, ultimo

# Buscar por nombre
def buscar(nombre, nombres):
    return nombres.index(nombre) if nombre in nombres else -1

# Contar ocurrencias de un nombre
def contar(nombre, nombres):
    return nombres.count(nombre) if nombre else "No encontrado"

# ------------------------- ACTUALIZAR -------------------------

# Cambiar nombre en posición 3
def cambiar(nombre, nombres):
    nombres[3] = nombre
    return nombres

# Cambiar todos los impares por 0
def actualizar(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            lista[i] = 0
    return lista

# Crear lista multiplicada por 2
def listaDos():
    result = [x * 2 for x in range(1, 10)]
    print(result)

# Invertir orden
def cambiarposicion(lista):
    return lista[::-1]

# ------------------------- ELIMINAR -------------------------

# Eliminar un nombre específico
def eliminar(nombres, nombre):
    if nombre in nombres:
        nombres.remove(nombre)
    return nombres

# Eliminar el último elemento
def ultimo(nombres):
    return nombres.pop(-1)

# Eliminar un rango de índices
def rango(nombres):
    del nombres[2:5]
    return nombres

# Limpiar toda la lista
def limpiar(nombres):
    nombres.clear()
    return nombres

# Filtrar valores mayores a 10
def mayores(lista):
    return [x for x in lista if x > 10]

# Ordenar y luego invertir
def reversoyordenado(nombres):
    nombres.sort()
    nombres.reverse()
    return nombres

# ------------------------- EJECUCIÓN -------------------------

if __name__ == "__main__":
    # Crear frutas aleatorias
    print("Lista de frutas aleatorias:", listaFruta())
    print("=" * 40)

    # Insertar al principio de lista de frutas
    listaFrutas = ["pera", "fresa", "melon", "sandia"]
    listaFrutas.insert(0, "manzana")
    print("Frutas:", listaFrutas)

    # Eliminar duplicados manualmente
    listasRepetidos = [x for x in range(1, 10)]
    listasRepetidos.append(1)
    listaSinRepetidos = []
    for x in listasRepetidos:
        if x not in listaSinRepetidos:
            listaSinRepetidos.append(x)
    print("Lista sin duplicados:", listaSinRepetidos)

    # Eliminar duplicados usando set
    listasRepeti = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 1, 1, 5, 6, 7, 4, 12, 5, 6, 1]
    listaNoRepetida = list(set(listasRepeti))
    print("Lista sin repetidos (set):", listaNoRepetida)
    print("=" * 40)

    # Lecturas
    print("Lista completa:", leer(nombres))
    print("Primer, medio y último:", elementos(nombres))
    print("Posición de 'Elena':", buscar("Elena", nombres))
    print("Cantidad de 'Elena':", contar("Elena", nombres))

    # Actualizaciones
    print("Cambio nombre en posición 3:", cambiar("Elmer", nombres))
    print("Actualizar impares a 0:", actualizar(listasRepeti))
    listaDos()

    # Eliminaciones
    print("Nombres actuales:", nombres)
    print("Invertido:", cambiarposicion(nombres))
    print("Eliminar 'Elmer':", eliminar(nombres, "Elmer"))
    print("Eliminar último:", ultimo(nombres))
    print("Eliminar rango 2 a 4:", rango(nombres))
    print("Valores mayores a 10:", mayores(listasRepeti))
    print("Ordenado inverso:", reversoyordenado(nombres))

    # Activar si querés limpiar toda la lista
    # print("Lista limpiada:", limpiar(nombres))

    # Crear lista vacía por input (activá si lo querés probar)
    # print("Nombres
