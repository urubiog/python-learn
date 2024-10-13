# Proporciona operadores sobre cadenas de texto
import re

raw_string = r"Soy una raw string"
formated_and_raw_string = rf"Soy una formated raw string"

texto = """Hola lector, esta es la primera cadena, cadena 1!
Esta es la segunda, 2?
Y finalmente la esta es última, 3. 000
"""
# Buscando coincidencias
resultado = re.findall(    "es",    texto,   flags=re.IGNORECASE) # Esta flag hace que la búsqueda no sea CaseSensitive
#            (operador)  (cadena),(objeto),(flag)

# \d --> Busca digitos numéricos 0-9
resultado = re.findall(r"\d", texto)

# \D --> Busca caracteres alfabéticos a-z A-Z
resultado = re.findall(r"\D", texto)

# \w --> Busca caracteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)

# \W --> Busca caracteres especiales y espacios
resultado = re.findall(r"\W", texto)

# \s --> Busca espacios en blanco [espacios, tabs, saltos]
resultado = re.findall(r"\s", texto)

# \S --> Busca TODO menos espacios en blanco [espacios, tabs, saltos]
resultado = re.findall(r"\S", texto)

# . --> Busca TODO menos saltos de linea
resultado = re.findall(r".", texto)

# \n --> Busca saltos de linea
resultado = re.findall(r"\n", texto)

# \. --> Buscar puntos
resultado = re.findall(r"\.", texto)

# Creando variable que busque un número seguido de un punto y un espacio
resultado = re.findall(r"\.\s\d", texto) # \. -> punto, \s -> espacio, \d -> num

# ^ --> Busca el principio de una linea
resultado = re.findall(r"^Hola", texto)

# re.M para que interprete que hay varias lineas
resultado = re.findall(r"^Esta", texto, flags=re.M)

# $ --> Busca el final de una linea
resultado = re.findall(r"0$", texto)

# {n} --> Busca n cantidad de veces su valor 
resultado = re.findall(r"\d{3}", texto) # En este caso el valor es los números 0-9

# {n,m} --> Busca un valor en un rango desde n hasta m
resultado = re.findall(r"\d{1,3}", texto)

# | --> Busca un valor u otro (or)
resultado = re.findall(r"\w\w\w\w\s|Hola", texto) # Devuelve los valores en orden

print(resultado)

#------------------------------------------------------------------------------------

# Comprobando que se cumplan las condiciones (buscando coincidencias)

text = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$", text) # * Hace que haya un elemento o más en la linea

if x:
    print("Sí")
else:
    print("No")
    
#------------------------------------------------------------------------------------

# Remplazando un valor en dos cadenas

cadena1 = "Mi número de telefono és 123-456-789"
cadena2 = "Ah pues a mi me dieron el 987-654-321, que guay"

# Reconocemos el patrón
patron = r"\d{3}\W\d{3}\W\d{3}" # Tres num guión tres num guión tres num

# Cadena a remplazar
remplazo = "NÚMERO DE TELÉFONO"

# Remplazamos las cadenas en el patrón con el remplazo
texto_nuevo1 = re.sub(patron, remplazo, cadena1)
texto_nuevo2 = re.sub(patron, remplazo, cadena2)

print("Textos modificados:\n", texto_nuevo1, "\n",texto_nuevo2)

#------------------------------------------------------------------------------------

# Pasando vocales a numeros

# Introducimos la cadena
cadena = input("\nIntroduce un texto: \n\n")

# Hacemos los patrones
a = re.sub("[a]", "4", cadena)
A = re.sub("[A]", "4", a)
e = re.sub("[e]", "3", A)
E = re.sub("[E]", "3", e)
i = re.sub("[i]", "1", E)
I = re.sub("[I]", "1", i)
o = re.sub("[o]", "0", I)
new_text = re.sub("[O]", "0", o)

print(new_text)

#------------------------------------------------------------------------------------

# Validando URLs

texto = "URLs a comprovar: https://.elpedro.com https://matando.c https://youtube.com http://192.168.2.10:1212 https://192.168.1.1.com "

pattern = r"\shttps?://\w[\w\.]+[\.][\w]{2,}[\s]" # No tiene límite el {} pero si principio

URLs = re.findall(pattern, texto)

print(URLs)