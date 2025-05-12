import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear DataFrame con columnas corregidas (sin espacios)
# Datos simulados
data = pd.DataFrame({
    "Name": [
        "elmer", "manuel", "rosalin", "erika", "lucia", "pedro", "camila", "david", "noemi", "cesar",
        "raul", "diana", "jorge", "valeria", "samuel", "karla", "renzo", "luis", "sofia", "andrea",
        "gonzalo", "fernando", "flor", "luciano", "isabel", "jhon", "melissa", "alejandro", "irene", "cristian"
    ],
    "Age": np.random.randint(18, 60, size=30),  # Edades entre 18 y 60
    "Salario": np.random.randint(8000, 70000, size=30)  # Salarios aleatorios
})

# Exploración de datos
print("=" * 40)
print("📊 Descripción estadística:")
print(data.describe())

print("=" * 40)
print("🔎 Últimas filas:")
print(data.tail())

print("=" * 40)
print("ℹ️ Información general:")
data.info()

print("=" * 40)
print("🔍 Filtrado (Age < 15):")
filtrado = data[data["Age"] < 15]
print(filtrado)

print("=" * 40)
print("🧱 Columnas:")
print(data.columns)

print("=" * 40)
print("📐 Dimensiones (filas, columnas):")
print(data.shape)

# Visualización
plt.figure(figsize=(10, 4))

# Histograma de edad
plt.subplot(1, 2, 1)
plt.hist(data["Age"], color="skyblue", edgecolor="black")
plt.title("Distribución de Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

# Gráfico de barras: salario por nombre
plt.subplot(1, 2, 2)
plt.bar(data["Name"], data["Salario"], color="orange")
plt.title("Salario por Persona")
plt.xlabel("Nombre")
plt.ylabel("Salario")

plt.tight_layout()
plt.show()
