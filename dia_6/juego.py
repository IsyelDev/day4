import os 
import random

os.system("cls")

def numbersecret(rangominimo=0,rangomaximo=10):
    return random.randint(rangominimo,rangomaximo)


def pedirNumero():
    while True:
        try:
            valor= input("INGRESA UN VALOR").strip()
            if not valor:
                raise ValueError("Valor vacio")
            valor =int(valor)
            return valor
        except ValueError as e:
            print(f"Entrada invalida {e}")

def jugarAdivinanzas(intentos=3):
    numerosecreto = numbersecret()
    print(numerosecreto)
    for intento_actual in range(1,intentos+1):
        print(f"\nIntento {intento_actual} de {intentos}")
        guess = pedirNumero()
        if guess==numerosecreto:
            print("Congratulation")
            break
        elif guess<numerosecreto:
            print("Tu numero es menor")
        else:
            print("Tu numero es mayor")
    else:
        print(f"\n😢 Te quedaste sin intentos. El número secreto era {numerosecreto}.")

def iniciar_juego():
    while True:
        jugarAdivinanzas()
        jugardenuevo=input("Quieres jugar de nuevo").strip().lower()
        if jugardenuevo !="s":
            print("Gracias")
            break


if __name__=="__main__":
    iniciar_juego()