personaActiva = True
result ="No esta activa" if not personaActiva else "Activa"
print("="*40)
print(result)

edadMayor = False
result ="No eres mayor" if not edadMayor else "Eres Mayor"
print("="*40)
print(result)

logueado = True
bloqueado = True
result ="Ingreso al sistema" if logueado and not bloqueado else "No Ingreso al sistema"
print("="*40)
print(result)


admin = True
activo = False
suspendido =False
result ="Ingreso al sistema" if (admin or activo) and not suspendido else "No Ingreso al sistema"
print("="*40)
print(result)





