print("Hola mundo")

def ingresedata(msn):
    return input(msn).strip()

respuesta = ingresedata("Hola como te llamas \n")

print("hola {} encantado de conocerte".format(respuesta))

pais , ciudad = input("en que pais y ciudad vives \n").split()
print(f"Vives en {ciudad} en el pais {pais}")