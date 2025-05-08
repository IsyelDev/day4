import time

def enterData(msn):
    while True:
        try:
            value = input(msn)
            if not value:
                raise ValueError("La entrada está vacía.")
            if not value.isdigit():
                raise ValueError("Por favor ingrese un número válido.")
            number = int(value)
            if number <= 2:
                raise ValueError("Por favor ingrese un número mayor a 2.")
            return number
        except ValueError as e:
            print(e)

def contador():
    valormaximo = enterData("Ingrese un valor: ")
    for x in range(valormaximo, 1, -1):
        print(x)
        time.sleep(1)
    print("Cuenta regresiva terminada")

if __name__ == "__main__":
    contador()
