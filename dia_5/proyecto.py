
import string
import random

def letras():
    return list(string.ascii_letters)

def numeros():
    return list(string.digits)

def simbolos():
    return list('!@#$%^&*()-_=+[]{};:,.<>?')

def entrada(msn):
    return int(input(msn))  # Convertir la entrada a un número entero

def mostrar():
    listavacia=[]
    letras_count = entrada("How many letters would you like in your password?\n")
    simbolos_count = entrada("How many symbols would you like in your password?\n")
    numeros_count = entrada("How many numbers would you like in your password?\n")

    for _ in range(letras_count):
       listavacia.append(random.choice(letras()))
   
    for _ in range(numeros_count):
       listavacia.append(random.choice(numeros()))
    
    for _ in range(simbolos_count):
        listavacia.append(random.choice(simbolos()))  # Añadir un símbolo aleatorio
    
    random.shuffle(listavacia)   
    return "".join(listavacia)
    

if __name__=="__main__":
    letras = letras()
    numero = numeros()
    simb = simbolos()
    print(letras)
    print(numero)
    print(simb)
    print(mostrar())