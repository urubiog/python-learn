# Para leer

# Primero se abre el archivo
archivo = open("C:\\Users\\Mi Pc\\Desktop\\Onedrive\\Hacking Y Programación\\Python\\Curso\\Archivos\\prueba.txt", encoding="UTF-8") # encoding hace que se manipule de manera correcta el archivo

# Se puede guardar la información de la lectura del archivo
lectura = archivo.read()

archivo.readline() # Lee linea (chars)
archivo.readlines() # Imprime una lista de las lineas (chars)
archivo.readable() # Devuelve si es leíble o no

archivo.close() # Se usa para cerrar el archivo, si no se cierra no se puede manipular de otra manera

# De manera optima se usa with ahorrando .close()

# Imprimiendo la lectura completa de prueba.txt como archivo
with open("Curso\\Archivos\\prueba.txt", encoding="UTF-8") as archivo: # Con (el archivo txt) como {archivo}
    print("\n" + archivo.read()) # Imprime la lectura del archivo
        
#--------------------------------------------------------------------------------

# Para escribir con permisos de escritura

# Abrimos el archivo con permisos de escritura con encoding UTF-8
with open("Curso\\Archivos\\prueba.txt","w", encoding="UTF-8") as archivo: # "w" se usa para dar permisos de escritura (write)
    
    archivo.write("Te he rescrito el archivo") # Sobreescribe el archivo
    archivo.writable() # Devuelve si el archivo se puede sobreescribir o añadir contenido
    archivo.writelines("\nY ahora te añado lineas") # Escribe lineas
    archivo.writelines(["\n" , "TAMBIÉN PUEDO AÑADIR LISTAS" , "\n" ,"PARÁMETRO 2"])
    
# Para escribir con permisos de append

# Abrimos el archivo con permisos de append con encoding UTF-8
with open("Curso\\Archivos\\prueba.txt","a", encoding="UTF-8") as archivo: # "a" se usa para dar permisos de append
    
    archivo.write("\nAhora no estoy sobreescribiendo, sino que hago un append")
    
# Agregando n lineas en una line de code
for i in range(6): open("Curso\\Archivos\\prueba.txt","a", encoding="UTF-8").write(f"\nLinea {i+1} agragada")