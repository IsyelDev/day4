import os

os.system("cls")

"""1. Crear un set con los números del 1 al 5 e imprimir su longitud."""
def numeros(lista):
   return len(lista)

def crearSet():
   return{x for x in (1,2,3,4,5)}
conjuntos =crearSet()

"""2. Agregar el número 6 a un set ya creado."""
conjuntos.add(6)
print("Conjunto después de agregar el 6:", conjuntos)

"""3. Verificar si el número 3 está en un set."""
if 3 in conjuntos:
   print("Esta dentro del conjunto")
else:
   print("No esta")

"""4. Convertir una lista con elementos repetidos en un set."""
listasRepetidos=[1,2,3,4,5,6,4,7,8,5,2,4]
nueva_lista=set(listasRepetidos)
print("Set sin elementos repetidos:", nueva_lista)

"""5. Eliminar un elemento específico de un set."""
def eliminar(lista,n):
   return lista.remove(n)

setUno = {1,2,3,4,5,6}
setDos ={7,8,9,10,11,12}

setPrimera ={1,2,3}
setSegunda={1,2,3,5,8,6}

print("Intersección (con &):", setPrimera & setSegunda)
print("Diferencia (con -):", setPrimera - setSegunda)


texto = "programacion"
caracteres_unicos = set(texto)
print("Caracteres únicos:", caracteres_unicos)

es_subconjunto= setPrimera.issubset(setSegunda)
print("¿setA es subconjunto de setB?", es_subconjunto)


def union(setUno,setDos):
   return setUno |setDos


"""Avanzado
Usa sets para eliminar palabras repetidas de un texto.

Encuentra los elementos únicos entre tres sets.

Detecta si dos listas tienen algún elemento en común usando sets.

Ordena los elementos de un set (aunque no garantice orden).

Usa set comprehension para crear un set de cuadrados de números pares del 1 al 20.

"""
def eliminare(palabras):
   return set(palabras)

unicoUno={1,2,3,4}
unicoDos={2,6,7,5,1}
unicoTres={1,2,8}

def diferencias (a,b,c):
   return a ^ b ^ c

def unicos(a,b):
   return a & b

def orden(a):
   return sorted(a)



def cuadrados():
   return {x**2 for x in range(1,20)}

if __name__=="__main__":
   print(numeros(conjuntos))
   eliminar(nueva_lista,4)
   print("Conjunto después de eliminar el 4:", nueva_lista)  # Imprime el set actualizado
   print(union(setUno,setDos))
   print(eliminare("pedroso"))
   print(diferencias(unicoUno,unicoDos,unicoTres))
   print(unicos(unicoUno,unicoDos))
   print(orden(unicoDos))
   print(sorted(cuadrados()))