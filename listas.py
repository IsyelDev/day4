import random

friends= ["Alice"," Bob II" ,"Charlie", "David", "Emanuel"]
escogido = random.choice(friends)
escogido2 = random.randint(0,len(friends)-1)
print(escogido)
print(friends[escogido2])

fruits=["manzana","fresa","naranja","pera"]
frineds=["manuel","elmer","isabel"]
nuevalista=[friends,fruits]
print(nuevalista)

fruits.append([friends])
print(fruits)
fruits.extend([friends])
print(fruits)

fruits.insert(2,[friends])
print(fruits)


