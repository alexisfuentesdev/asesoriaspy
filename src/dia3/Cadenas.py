print("*" * 60)

nueva_cadena = "Hola" + " " + "mundo!"
print(nueva_cadena)

mensaje = "Hola"
mensaje += " " # "Hola "
mensaje += "mundo!" # "Hola mundo!"
# n
print("*"*60)
# Sobrecarga
print(mensaje)

# Recorrer cadena por caracter
for caracteres in mensaje:
    print(caracteres)
# mensaje = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o", "!"]
print(len(mensaje))

# Busqueda dentro de cadenas
busqueda = mensaje.find("mundo") # Indice donde se encuentra lo que se busca, si en dado caso no se encuentra nos dara como resultado -1
if busqueda != -1:
    print("Indice donde se encuentra lo que se busca: {}".format(busqueda))
    print("La cadena \'{}\' contiene la letra \'m\'".format(mensaje))
else:
    print("Caracter no encontrado")
    

# Funciones para mayusculas y minusculas
print(mensaje.lower())
print(mensaje.upper())
    
mensaje = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o", "!"]

res = ""
for c in mensaje:
    res += c
print(res)