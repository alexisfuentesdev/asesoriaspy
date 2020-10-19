#importamos la libreria math de python
from math import *

# Resolver la ecuación y retornar un valor flotante*
def pol(x):
    return exp(x)*sin(x)-(x/2)

# Resolver la ecuación y retornar un valor flotante*
def diff(x):
	return exp(x)*sin(x)+exp(x)*cos(x)-(1/2)


# Se pueden obviar la inserción de los parametros "f" y "df"

def NewRap(a, tol): #vamos a llamar la función para que realice el método
    # a = -2
	if pol(a)/diff(a) < 0:

        # La impresión de los titulos
		print ("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format
		  ("i","a","fa","f´d","xr","fxr","ErrorAp"))

	    # Inicializamos el contador y encontramos la raíz

        # Asignaciones de datos
		i = 1 # El numero de la fila
		xr = a-(pol(a)/diff(a))	#se calcula el 4.3
		xra = xr 		#ese 4.3 lo guardo en xra

        # impresión de los resultados
        # El .4f nos mostrara el total de decimales para la impresión
		print ("{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}".format
		    (
                i,
                float(a),
                float(pol(a)),
                float(diff(a)),
                float(xr),
                float(pol(xr))
            )
        )

        # Calculamos el error, función de math ABS
		error = abs(pol(xr)) 	#por mientras para entarr al ciclo

        # Iniciamos un ciclo
		while error > tol:
			i = i + 1		#estoy imprimindo la iteraccion

            # Verificamos con if si el resultado de las dos función
			if pol(a)*pol(xr) < 0:
				a=xr
			else:
				a=xra
    
            # Calculamos el resultado de la función, en esta linea es que va a cambiar
			xr = a-(pol(a)/diff(a)) 	#aqui se
   
            # calculamos el error
			error = abs((xr-xra)/xr)*100
   
            # Solo se imprimen los resultados
			print ("{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}".format
		        (
                    i,
                    float(a),
                    float(pol(a)),
                    float(diff(a)),
                    float(xr),
                    float(pol(xr)),
                    float(error)
                )
            )

			xra = xr
	else:
		print("No hay raices en el intervalo", "{",a,"}")

# Llamada a la función principal
# NewRap(pol,diff,-2,0.0001) -> Antes de eliminar pol y diff que no son necesarios dentro de los parametros de la llamada a la función
NewRap(-2,0.0001)
