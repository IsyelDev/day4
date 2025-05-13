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

if __name__=="__main__":
    print(genera_numero())