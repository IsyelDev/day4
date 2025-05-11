import pandas as pd
import numpy as np


data = pd.DataFrame({
    "Name ":["elmer","manuel","rosalin","erika"],
    "Age":[24,14,17,15],
    "salario":[10000,30651,51215,24444]
})

print(data.mean)
print("="*40)
print(data.describe())
print("="*40)
print(data.head())


print("="*40)
filtrado = data[data["Age"]<15]
print(filtrado)