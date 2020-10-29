import numpy as np # estamos llamando a numpy y lo podemos usar

matriz1 = [
    [1, -1, 1],
    [2, 2, 3],
    [-2, -3, -1]
]

matriz2 = [
    [1, 0, 4],
    [0, 2, 5],
    [1, 3, 0]
]

matriz3 = [] # Tercera matriz de resultados

# Llenando una matriz de 3 x 3 con los datos en cero
'''
[0,0,0], <--- este nos da el tamaño de la columna
[0,0,0],
[0,0,0]
'''
for row in matriz1:
    matriz3.append([0]*len(row))
    
# La multiplicación de las matrices

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz1[0])):
            matriz3[i][j] += matriz1[i][k] * matriz2[k][j]

print("*"*30)
print("El resultado de la multiplicación de matrices es:")
for row in matriz3:
    print(row)