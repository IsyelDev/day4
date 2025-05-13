from random import randint

def genera_numero():
    return randint(0,1000)


nombres =["elmer","erika","isabel","juan","manuel"]


lista_nombres =[]

for i in range(len(nombres)):
    lista_nombres.append((nombres[i],nombres[i][0]+str(genera_numero())))

print(lista_nombres)


notas_grupo = ['Juan', 8.0, 9.0, 10.0,
               'Manuel', 9.0, 7.0, 6.0,
               'Erika', 3.4, 7.0, 7.0,
               'Claudia', 5.5, 6.6, 8.0,
               'Ana', 6.0, 10.0, 9.5]


nombres_alumnos =[]
notas=[]

for i in range(len(notas_grupo)):
    if i % 4==0:
        nombres_alumnos.append(notas_grupo[i])
    else:
        notas.append(notas_grupo[i])

notas_separadas=[]
for i in range(0,len(notas),3):
    notas_separadas.append([notas[i],notas[i+1],notas[i+2]])

print(nombres_alumnos)
print(notas_separadas)
print(notas)
print("="*40)



nombres_alumnosa = []
notas_separadasa = []
print (len(notas_grupo))
for i in range(0, len(notas_grupo), 4):
    nombres_alumnosa.append(notas_grupo[i])
    notas_separadasa.append(notas_grupo[i+1:i+4])

print(nombres_alumnosa)
print(notas_separadasa)


datos = ["Juan", 25, "Lucía", 30, "Carlos", 22, "Ana", 28]

# Tu objetivo:
# nombres = ["Juan", "Lucía", "Carlos", "Ana"]
# edades = [25, 30, 22, 28]
def descomponer(datos):
    nombres=[]
    edades=[]
    for i in range(0,len(datos),2):
        nombres.append([datos[i]])
        edades.append([datos[i+1]])
    return nombres , edades

print("="*40)
nombres , edades = descomponer(datos)
print(nombres)
print(edades)


lista = ["Pan", 1.2, "Leche", 0.99, "Queso", 2.5, "Jugo", 1.8]

# Resultado esperado:
# productos = ["Pan", "Leche", "Queso", "Jugo"]
# precios = [1.2, 0.99, 2.5, 1.8]

def productos(lista):
    x=[]
    y=[]
    for i in range(0,len(lista),2):
        x.append(lista[i]) 
        y.append(lista[i+1])
    return x , y

producto , precio = productos(lista)
print(producto)
print(precio)


materias = ["María", 7, 8, 9, 10, "Pedro", 6, 6, 7, 8, "Julia", 9, 9, 10, 10]

# Resultado esperado:
# alumnos = ["María", "Pedro", "Julia"]
# promedios = [8.5, 6.75, 9.5]
def promedio(materias):
    alumnos=[]
    promedios=[]
    
    for i in range(0, len(materias),5):
        alumnos.append(materias[i])
        notas.append(materias[i+1:i+5])
    
    for nota in notas:
        promedios.append(sum(nota)/len(nota))
    
    return alumnos , notas , promedios

print(promedio(materias))
if __name__=="__main__":
    print(f"Soy un numero generado {genera_numero()}")