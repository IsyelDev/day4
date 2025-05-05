import os

os.system("cls")

def info(a,b,c):
    return {"nombre":a,"edad":b,"pais":c}

def encontrarValor(dicionario,valor):
    return dicionario.get(valor,"Clave no encontrada")

def modifica(dicionario,valor):
    return dicionario.update({"nombre":valor})

def agrega(dicionario,valor):
    dicionario["direccion"]=valor
    return dicionario

def eliminar(dicionario,valor):
    return dicionario.pop(valor,"Clave no encontrada")

if __name__=="__main__":
    dicionario = info("elmer",20,"peru")
    print(dicionario)
    print(encontrarValor(dicionario,"edad"))
    print(encontrarValor(dicionario,"direccion"))
    modifica(dicionario,"isabel")
    agrega(dicionario,"comas")
    print(dicionario)
    print(eliminar(dicionario,"edad"))
    print(dicionario)