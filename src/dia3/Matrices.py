# lista = [
#     23, 
#     "a", 
#     [45, 89], 
#     {"dict": "Hola mundo"}
# ]

# for elemento in lista:
#     print("Elemento {} de tipo {}".format(elemento, type(elemento)))

m1 = [
    # *
    [0, 0, 0], # <------
    [0, 0, 0],
    [0, 0, 0]
]

# for fila in m1:
#     print(fila)

# Recorrido por elemento
for fila in m1:
    for elemento in fila:
        print(elemento)
        
print("*"*60)
print("Recorrido por indice")
# Recorrido por indice de la matriz
for i in range(len(m1)):
    for j in range(len(m1[0])):
        print(m1[i][j])
        
# SUMA DE MATRICES

# Primero matriz
matriz1 = [
    [8, 9],
    [2, 7]
]

# Segunda matriz
matriz2 = [
    [12, 11],
    [8, 3]
]

# Definición de la matriz resultado
matriz3 = [] # Matriz vacia
for fila in matriz1:
    matriz3.append([0] * len(fila))

# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]


for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
        

# Imprimir el resultado
print("*"*60)
for row in matriz3:
    print(row)
