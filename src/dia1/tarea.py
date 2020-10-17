#importamos la libreria math de python
from math import *

# Resolver la ecuación y retornar un valor flotante*
def pol(x):
    return exp(x)*sin(x)-(x/2)

# Resolver la ecuación y retornar un valor flotante*
def diff(x):
	return exp(x)*sin(x)+exp(x)*cos(x)-(1/2)


def NewRap(f, df, a, tol): #vamos a llamar la función para que realice el método

	if pol(a)/diff(a) < 0:


		print ("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format
		  ("i","a","fa","f´d","xr","fxr","ErrorAp"))

	# Inicializamos el contador y encontramos la raíz

		i = 1
		xr = a-(pol(a)/diff(a))	#se calcula el 4.3
		xra = xr 		#ese 4.3 lo guardo en xra
	
		print ("{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}".format
		  (i,float(a),float(pol(a)),float(diff(a)),float(xr),float(pol(xr))))


		error = abs(pol(xr)) 	#por mientras para entarr al ciclo


		while error > tol:

			i = i + 1		#estoy imprimindo la iteraccion

			if pol(a)*pol(xr)<0:
				a=xr
			else:
				a=xra

			xr = a-(pol(a)/diff(a)) 	#aqui se

			error = abs((xr-xra)/xr)*100

			print ("{:^10}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}{:^10.6f}".format
		  (i,float(a),float(pol(a)),float(diff(a)),float(xr),float(pol(xr)),float(error)))

			xra = xr

	else:

		print("No hay raices en el intervalo", "{",a,"}")

# Llamada a la función principal
NewRap(pol,diff,-2,0.0001)
