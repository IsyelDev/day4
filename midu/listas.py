frutas = [
    "Manzana", "Plátano", "Uva", "Naranja", "Fresa",
    "Pera", "Mango", "Piña", "Sandía", "Melón",
    "Kiwi", "Cereza", "Limón", "Durazno", "Papaya",
    "Mandarina", "Granadilla", "Frambuesa", "Arándano", "Mora"
]

# Para imprimir la lista de frutas
uno =frutas[0]
uno , dos ,*tres,cuatro = frutas
ultimo=frutas[-1]

print(uno)
print(cuatro)
print(ultimo)
indice = frutas.index("Mora")
print(indice)
print(indice)
copia = frutas[:]
print(copia)
invertida = frutas[::-1]
print(invertida)

facturas = [
    (1, 120.50, "pagada"),
    (2, 80.00, "no pagada"),
    (3, 200.75, "pagada"),
    (4, 50.00, "no pagada"),
    (5, 300.00, "pagada"),
]

i=0
while i < len(facturas):
    factura = facturas[i]
    i+=1
    if factura[2]=="pagada":
        continue
    print(factura)
    

# Ejercicio:
# - Imprime el segundo elemento
# - Cambia el último por 99
# - Invierte la lista

print("="*40)
def modificar_lista():   
    numeros = [10, 20, 30, 40, 50]
    print(numeros[3])
    numeros[-1]=99
    print(numeros)
    numerosInvertidos=numeros[::-1]
    print(numerosInvertidos)
colores = ("rojo", "verde", "azul", "amarillo")
print(colores[2])

for color in colores:
    print(color)

lista = list(colores)
lista[2]="negro"
print(tuple(lista))
print("="*40)
modificar_lista()

frutas = {"manzana", "pera", "naranja", "fresa"}

# Ejercicio:
# - Convierte el set a lista e imprime el primer elemento
# - Añade una fruta nueva
# - Elimina una fruta cualquiera

nuevalista =list(frutas)
nuevalista.append("uva")
print(nuevalista)
del nuevalista[-1]
print(nuevalista)


persona = {
    "nombre": "Luis",
    "edad": 30,
    "pais": "México"
}

# Ejercicio:
# - Imprime el valor de "nombre"
# - Cambia "edad" a 35
# - Añade la clave "profesion": "Ingeniero"


if "nombre" in persona:
    print(persona.get("nombre"))
    
if "edad" in persona:
    persona["edad"] =35

        
print(persona)

persona["profesion"]="Ingeniero"
        
print(persona)

cadena = "midudev"

for index,valor in enumerate(cadena):
    print(f"{index}{valor}")
    
numero =[1,2,3,4,5,6,7,8,9,10,11,12]
valores =[1,2,3,4,5,7,8,9,10,11,12]
for valor in valores:
    print("="*40)
    for num in numero:
        print(f"{num} * {valor} = {num*valor}")
    
numeros = range(10)
listasdenumeros = list(numeros)
print(listasdenumeros)


def restar(a,b):
    """resta dos numeros"""
    return a-b

help(restar)