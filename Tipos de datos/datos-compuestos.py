#Las listas se pueden modificar
listas = ["Lucas Dalto", "soy andres", True, 1.85]
#print(listas)
# las tuplas no se pueden modificar
tupla = ("Lucas Dalto", "soy andres", True, 1.85)
# FORMA DE AGARRAR UN VALOR DE UNA LISTA
listas = ["Lucas Dalto", "soy andres", True, 1.85]
#print(listas[1])

# Creando un conjunto (set)
# No se pueden modificar, pero se pueden reescribir
# No se puede asceder por posicion
# No se puedne terner datos repetidos o duplicados
# Se puedne accer a los elementos por un bucle
conjunto = {"Lucas Dalto", "soy andres", True, 1.85}

# CREANDO UN DICCIONARIO (dict)
# la estructura del diccionario es Key : value o clave - valor
diccionario = {
    'nombre': "soy andres",
    'canal': 'andres pinto',
    'esta_emocionado': True,
    'altura': 1.84,
    'dato_duplicado':"soy andres"
}

print(diccionario["altura"])