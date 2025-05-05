def mayor(edad):
    texto ="Puede ingresar su edad es"
    return f"{texto} {edad}" if edad>=18 else f"No {texto} {edad}"

def parPositivo(numero):
    return "Positivo" if numero%2==0 and numero>=0 else "Negativo"
 
def parPositivo2(numero):
    if numero >=0:
        if numero%2==0:
            return f"El numero ingresado es par y positivo{numero}"
        else: 
            return f"El numero ingresado es positivo pero impar {numero}"
    else:
        return f"El numero ingresado es negativo{numero}"

def validacion(contrasena):
    return "Correcto" if contrasena.strip().lower()=="admin123" else "Incorrecto"

def condicion(numero):
    return "Rango Correcto" if 10<=numero<=20  else "Rango Incorrecto"

def negativo(numero):
    return "Es positivo" if not numero<=0 else "Es negativo"
    

"""Nivel intermedio"""


def rango(numero):
    return "Rango Correcto" if 100<=numero<=200  else "Rango Incorrecto"

def validacion(letra):
    return "Mayuscula" if letra in "AEIOU" else "Minuscula" if letra in "aeiou" else "No es una vocal"


def combinacion(a,b,c):
    if(a==c):
        return   f"{a} es igual a {c}"
    elif a>b:
        if(b>c):
           return f"{a} es mayor {b} es mayor {c}"
        else:
           return f"{a} es mayor que {b} pero no es mayor {c}"
    else:
        return "Fuera de rango"

def usuariovalidacion(user,contrasena):
    return "Correcto" if  user.strip().lower()=="admin" and contrasena.lower()=="1234"  else "Incorrecto"

def valornulo(numero):
    if numero is not None:
        if numero >0:
           return f"{numero} es positivo y no es valor none"
        else:
           return f"{numero} es negativo y no es valor none"
    else:
        return f"Valor nulo"


"""
ADVANCED
"""

def evaluador(x,y):
    return f"Numero positivo x {x} y {y}" if x >=0 and y>=0  else( f"Numero x {x} es positivo" if x >=0
                                                                  else f"Numero positivo y {y}" if y >=0 else "Ninguno es positivo")

def validador(n):
    if n in range(30,90):
        if n%3==0 and  n%5!=0:
            return f"es divisible a 3"    
        else:
            return f"esta en el rango pero no es divisible a 3"    
    else:
        return f"no esta en el rango y no es divisible a 3"    
        
def rango_circular(n):
    if 0<= n<= 360:
        if 225<=n<=315:
            return "Se encuentra en el rango"
        elif 45<=n<=135:
            return "No Se encuentra en el rango"
    else:
        return "No esta en el numero dado"

def validacion_acceso(edad, tiene_ticket, es_invitado):
    if edad > 18 and (tiene_ticket,es_invitado):
        return "Ingreso"
    else:
        return "no puede ingresar"

def evaluacion(a,b,c):
    return "Tres son booleanos" if a and b and c  else("Dos son iguales" if a and b or b and c or c and a  else "No son valores iguales")


