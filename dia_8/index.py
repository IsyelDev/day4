contacto={
    "name":"Elmer",
    "phone":"12345",
    "email":"emdelapaz@gmail.com"
}


print(contacto["name"])
print(contacto.get("name"))
"""Modificar"""
contacto["phone"]="956901024"
print(contacto)
"""AÑADIR"""
contacto["edad"]=25
print(contacto)
"""Eliminar"""
del contacto["edad"]
print(contacto)

for key , item in contacto.items():
    print(f"{key},{item}")

resultado ="Encontrado" if "name" in contacto else "No encontrado"
print(resultado)

"""Proyecto"""


def menu():
    print("=" * 40)
    print("     📇 Bienvenido a tu Agenda de Contactos     ")
    print("=" * 40)
    print("1️⃣  - Añadir contacto")
    print("2️⃣  - Editar contacto")
    print("3️⃣  - Eliminar contacto")
    print("4️⃣  - Listar contactos")
    print("5️⃣  - Salir")
    print("=" * 40)


def enterData(msn, tipo="int"):
    try:
        valor = input(msn)
        if not valor.strip():
            raise ValueError("⚠️ El valor ingresado está vacío.")
        
        if tipo == "str":
            return str(valor)
        elif tipo == "int":
            return int(valor)
        else:
            raise  ValueError(f"⚠️ Tipo no reconocido: '{tipo}'")
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
            
def listar(listaContacto):
    if not listaContacto:
        print("⚠️  Datos vacíos")
    else:
        for nombre, telefono in listaContacto.items():
            print(f"📞 {nombre}: {telefono}")
            
contactos = {"Juan": "123456789", "Ana": "987654321"}

def anadir(listaContacto, nombre,contacto):
    listaContacto[nombre]=contacto
    print(f"✅ Contacto '{nombre}' añadido.")
    
def editar(listaContacto, nombre,nuevo_contacto):
    if nombre in listaContacto:
           print(f"✏️ Contacto '{nombre}' editado.")
    else:
        print(f"➕ Contacto '{nombre}' no existía, así que fue creado.")
    listaContacto[nombre] = nuevo_contacto

def eliminar(listaContacto, id):
    if id in listaContacto:
        del listaContacto[id]
        print(f"🗑️ Contacto '{id}' eliminado.")
    else:
        print(f"⚠️ Contacto '{id}' no existe. No se puede eliminar.")
        

def operaciones():
    contactos={}
    while True:
        menu()
        result = enterData("Ingrese una opción: ", "int")
        if result == 1:
            nombre = enterData("Ingrese el nombre: ", "str")
            telefono = enterData("Ingrese el número: ", "str")
            anadir(contactos, nombre, telefono)

        elif result == 2:
            nombre = enterData("Nombre del contacto a editar: ", "str")
            nuevo_telefono = enterData("Nuevo número: ", "str")
            editar(contactos, nombre, nuevo_telefono)

        elif result == 3:
            nombre = enterData("Nombre del contacto a eliminar: ", "str")
            eliminar(contactos, nombre)

        elif result == 4:
            listar(contactos)

        elif result == 5:
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")
        
if __name__ == "__main__":
    operaciones()
    