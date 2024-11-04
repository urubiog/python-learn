# Todos estos métodos están aplicados a cadenas de texto: objeto.método
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

cadena1 = "Hola soy Uriel"
cadena2 = "pepe"
cadena3 = "42"

# Convertir
cadena1.upper() # A MAYUSC
cadena1.lower() # a minusc
cadena1.capitalize() # Capitalizando
cadena1.swapcase() # minusc a MAYUSC y viceversa

# Buscar subcadena de una cadena
cadena1.find("H") # Devuelve su índice. Si no encuentra nada, devuelve -1.
cadena1.rfind("x") # Devuelve su índice final. Si no encuentra nada devuelve -1.

# Buscar por índice
cadena1.index("o") # Si no encuentra nada, devuelve una excepción.

# Verificar tipo de caracteres
cadena = "Hola, buenas"

cadena.isalnum()  # Devuelve True si todos los caracteres de la cadena son alfanuméricos (letras o números)
cadena.isalpha()  # Devuelve True si todos los caracteres de la cadena son letras
cadena.isdigit()  # Devuelve True si todos los caracteres de la cadena son dígitos
cadena.isspace()  # Devuelve True si todos los caracteres de la cadena son espacios en blanco, False de lo contrario
cadena.islower()  # Devuelve True si todos los caracteres alfabéticos de la cadena están en minúscula y hay al menos un carácter alfabético
cadena.isupper()  # Devuelve True si todos los caracteres alfabéticos de la cadena están en mayúscula y hay al menos un carácter alfabético
cadena.istitle()  # Devuelve True si la cadena está en formato de título (primer letra de cada palabra en mayúscula y las demás en minúscula)

# Devuelve el numero de coincidencias de una cadena en otra cadena.
cadena = "Hoola"

cadena1.count("o") # 2

# Verificar si una cadena empieza con otra cadena dada -> bool
cadena.startswith("H") # True

# También existe para verificar si acaba con una cadena
cadena1.endswith("l") # Devuelve True

# Remplazar un pedazo de la cadena dada por otra
cadena1.replace("Hola","Holu") # Ahora la cadena1 es Holu soy Uriel

# Dividir strings
cadena1.split() # Devuelve de los conjuntos de caracteres separados por espacio o el argumento

# Como argumento se puede pasar el caracter delimitador
info = "Uriel-16-Macho"
info.split(sep="-", maxsplit=1) # Sep es el argumento por defecto y maxsplit es el número de veces a dividir la string basado en el separador.

# Eliminar caracteres a los lados
string = "    o     "

string.strip() # Elimina todos los espacios en blanco a banda y banda
string.rstrip() # Elimina todos los espacioes en blanco a la derecha
string.lstrip() # Elimina todos los espacios en blanco a la izquierda

# Si se pasa un argumento, esa substring será eliminada
url = 'www.ejemplo.com/'
url.strip('w./') # ejemplo.com

iterable = [1,2,3,4]

# Juntar los elementos de un iterable con una string
"-".join(str(iterable)) # Devuelve una string -> "1-2-3-4"

# Verificar formato
cadena = "Hello123"
cadena.isascii()      # Devuelve True ya que todos los caracteres son ASCII
cadena.isdecimal()    # Devuelve False ya que no todos los caracteres son dígitos decimales
cadena.isidentifier() # Devuelve True ya que "Hello123" es un identificador válido de Python
cadena.isnumeric()    # Devuelve False ya que no todos los caracteres son caracteres numéricos

# Alinear texto
cadena = "Hello"
cadena.center(20)  # Devuelve "       Hello        "
cadena.ljust(20)   # Devuelve "Hello               "
cadena.rjust(20)   # Devuelve "               Hello"

# Separar y combinar
cadena = "Hello World it's me"
cadena.partition(" ")  # Devuelve ('Hello', ' ', 'World it's me'), la cadena es particionada en tres partes por la primera aparición del espacio
cadena.rpartition(" ")  # Devuelve ('Hello', 'World', 'it's', ' ', 'me'), la cadena es particionada en tres partes por la última aparición del espacio
cadena_multilinea = "Hola\nMundo\nPython"
cadena_multilinea.splitlines()  # Devuelve ['Hola', 'Mundo', 'Python'], lista de líneas en la cadena, separadas por saltos de línea
cadena.encode()  # Devuelve b'Hello World', la versión codificada de la cadena como bytes

# Formateo
cadena = "Mi nombre es {nombre} y tengo {edad} años."
cadena.format(nombre="Juan", edad=30)  # Devuelve "Mi nombre es Juan y tengo 30 años."
cadena.format_map({'nombre': "María", 'edad': 25})  # Devuelve "Mi nombre es María y tengo 25 años."

# Crear tabla de traducción
tabla = str.maketrans("aeiou", "12345")
cadena = "Hola Mundo"
(cadena.translate(tabla))  # Devuelve "H4l1 M5nd4"

# Convertir la cadena a minúsculas para comparación de cadenas
cadena = "HELLO I"
cadena.casefold()  # Devuelve "hello ı"

# Expandir tabulaciones
cadena = "Hola\tMundo"
cadena.expandtabs()  # Devuelve "Hola    Mundo", donde la tabulación es expandida con espacios

# Rellenar con ceros
numero = "42"
numero.zfill(5)  # Devuelve "00042", rellenando con ceros a la izquierda para que el resultado tenga una longitud total de 5

# Eliminar prefijo
cadena = "Hello World"
print(cadena.removeprefix("Hello "))  # Devuelve "World", eliminando el prefijo "Hello "

# Eliminar sufijo
cadena = "Hello World"
print(cadena.removesuffix(" World"))  # Devuelve "Hello", eliminando el sufijo " World"