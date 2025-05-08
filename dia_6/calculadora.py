def ingresoDatos(msn):
    while True:
        try:
            numero = input(msn).strip()
            if numero == "":
                raise ValueError("No se permiten valores vacíos.")
            if not numero.isdigit():
                raise ValueError("No es un número válido.")
            return int(numero)
        except ValueError as e:
            print(f"Error: {e}")

def operaciones():
    n1 = ingresoDatos("Ingrese el primer número (n1): ")
    n2 = ingresoDatos("Ingrese el segundo número (n2): ")
    while True:
        try:
            print("\nOperaciones disponibles:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Salir")
            opcion = int(input("Seleccione una opción (1-5): ")) 
            if opcion == 1:
                return n1 + n2
            elif opcion == 2:
                return n1 - n2
            elif opcion == 3:
                return n1 * n2
            elif opcion == 4:
                if n2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                return n1 / n2
            elif opcion == 5:
                return "Saliendo del programa..."
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
  
if __name__=="__main__":
    print(operaciones())