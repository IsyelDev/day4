print(f"|{'Izq':<10}|{'Centro':^10}|{'Der':>10}|")
pi = 3.14159265
print(f"{pi:.2f}")

num = 1000000
print(f"{num:,}")

print("\033[94m Texto rojo\033[0m")

nombre= "erika"
edad=15
print("{}".format(nombre))
print("Nombre:",nombre, "Edad:", edad)
print("Nombre:" + nombre, "Edad:" + str(edad))

print("Edad: {a}, Nombre: {e}".format(a=nombre, e=edad))

frase ="nuevo","elmer","bebe"
print(*frase , sep="\n")
print(*frase,end="\n")

print("2025", "05", "07", sep="/")   # Fecha con barras
# Output: 2025/05/07

print("ID", 123, sep=": ")
# Output: ID: 123
