import random

def cpu():
    return random.randint(0,2)

def user(numero):
    return input(numero)

"""
rocka 0
papel 1
Tijera 2
"""

def jugada_a_texto(numero):
    opciones = ["Piedra", "Papel", "Tijera"]
    return opciones[numero]

def validacion():
    try:   
        usuario = int(user("Ingrese un valor\n"))
        usercpu = cpu()

        if usuario in range(0,3):
            texto_usuario = jugada_a_texto(usuario)
            texto_cpu = jugada_a_texto(usercpu)
         
            if usuario == usercpu:
                return f"usuario empata con cpu {texto_usuario}=={texto_cpu}"
            elif usuario==0 and usercpu ==2 or usuario==1 and usercpu==0 or usuario==2 and usercpu==1:
                return f"Gano usuario {usuario} le gana a {usercpu}"
            else:
                return  f"Gano cpu {usercpu} le gana a {usuario}"
        else:
           print("No esta en el rango")    
    except ValueError:
        return "Entrada inválida. Debes ingresar un número."

        
if __name__=="__main__":
    print(validacion())

