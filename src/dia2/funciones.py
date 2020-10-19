'''
Mostrarnos una lista de posibles figuras y al seleccionar una de ellas
nos va pedir los datos para calcular el area de ella
'''
# Función para calcular el area de un cuadrado
def calcular_area_cuadrado(b, h):
    return b*h

# Función para calcular el area de un triangulo
def calcular_area_triangulo(b, h):
    return (b*h)/2

# Función principal
def main():
    # imprimir un listado de las figuras
    print("Opciones de la figuras:")
    print("1 .- Cuadrado\n2 .- Triángulo")
    
    figura = input("Figura a calcular el área: ") 
    
    if figura != "1" and figura != "2":
        print("Opción no valida!!!")
        
    # print(figura)
    # print(type(figura))
        
    base = int(input("Base de la figura: "))
    altura = int(input("Altura de la figura: "))
    
    # Calculo del area del cuadrado
    if figura == "1": # Cuadrado
        a = calcular_area_cuadrado(base, altura)
        print("*"*40)
        print("El área del cuadrado con base = {} y altura {} es: {}".format(
                    base, altura, a
                )
            )
        print("*"*40)
    
    if figura == "2": # Triangulo
        a = calcular_area_triangulo(base, altura)
        print("*"*40)
        print("El área del triángulo con base = {} y altura {} es: {}".format(
                    base, altura, a
                )
            )
        print("*"*40)


main() # Llamando a la función Main
