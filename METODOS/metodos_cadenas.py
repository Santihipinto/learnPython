cadenas1 = "Hola soy dalto"
cadenas2 = "Bienvenido, Maquina"

# Devuelve la lista de atributos válidos del objeto pasado
resultado = dir(cadena1)

# Convierte a mayusculas
resultado1 = cadenas1.upper()
# Converte a minusculas
resultado2 = cadenas1.lower()
# Primera en mayuscula
resultado3 = cadenas1.capitalize()
# Buscamos una cadena en otra cadena, si no hay coincidencias devuleve -1 
resultado4 = cadenas1.find("Hola")
# Buscamos una cadena en otra cadena, si no hay coincidencias devuleve una excepcion 
resultado4 = cadenas1.index("Hola")
# Si es numerico devulve True, sino devulve False
resultado5 = cadenas1.isnumeric()
# Si es Alfanumerico devulve True, sino devuelve False
resultado6 = cadenas1.isalpha()
# Buscamos una cadena en otra cadena, devuelve el numero de coincidencias, sino hay coincidencias devuelve 0
resultado4 = cadenas1.count("a")
# Contamos cuantos caracteres tiene la cadena
resultado7 = len(cadenas1)
# Verificamos si una cadena empieza con otra cadena dada, si es asi devulve True
resultado8 = cadenas1.startswith("H")
# Verificamos si una cadena termina con otra cadena dada, si es asi devulve True
resultado8 = cadenas1.endswith("H")
# Si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
resultado9 = cadenas1.replace("la", "lu")
# Separa cadenas con la cadena que le pasemos, devulve una lista con los valores
resultado10 = cadenas2.split(",")
