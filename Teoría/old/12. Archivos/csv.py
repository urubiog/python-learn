# Utilizamos la librería csv
import csv
# Se recomienda utilizar la lib pandas
import pandas as pd # Se trabaja usando la librería como pd

#------------------------------------------------------------------

# Para leer archivos CSV con csv

try: # Ahora con try podremos manejar mejor las excepciones
    with open("Curso\\Archivos\\contacts.csv") as archivo: # Mismo método que antes
        for row in csv.reader(archivo): # Aquí iteramos el archivo por columnas
            print(row) # E imprimimos cada col
    
except Exception as e: # Exceptuando la excepción como "e"
    print(e) # Imprime la excepción
    

print("\n\n")
#------------------------------------------------------------------

# Para leer archivos CSV con pd

try: 
    with open("Curso\\Archivos\\contacts.csv", encoding="UTF-8") as archivo: # Mismo método que antes
        df = pd.read_csv(archivo , names=["name","lastname","age"]) # Esto es un dataframe
        print(df) # No usamos un bucle sinó que directamente se reconoce el archivo csv y da una buena salida
     
except Exception as e: # Exceptuando la excepción como "e"
    print(e) # Imprime la excepción
    
#------------------------------------------------------------------

# Funciones de pd
    
print("\n")

df.drop(0,inplace=True) # Para eliminar una fila con indice x

print("\n")

print(df["name"]) # Esto lo que hace es imprimir la columna name
    
print("\n")

contacts_sorted = df.sort_values("age") # Ordena la tabla por la col "age"

print(contacts_sorted)

print("\n")

contacts_reversed = df.sort_values("age",ascending=False) # Lo ordena de manera descendente

print(contacts_reversed)

print("\n")

df_concatenado = pd.concat([contacts_sorted , contacts_reversed]) # Concateno los dos dataframes

print(df_concatenado) # Muestra las dos tablas como una donde se han concatenado estas dos

print("\n")

primera_row = df.head(2).tail(1) # Accedemos a la primera fila que está en la segunda

print(primera_row)

print("\n")

ultima_row = df.tail(1) # Ahora accedemos a la cola de la tabla

print(ultima_row)

print("\n")

print(df.shape) # Accedemos al total de filas y columnas

print("\n")

print(df.describe()) # Accedemos a la información descriptica del datframe

print("\n")

elemento_especifico = df.loc[1 , "age"] # Accedemos al valor [row , col]

print(elemento_especifico)

print("\n")

elemento_especifico_i = df.iloc[2,2] # la "i" viene de index, accedemos al valor [index,index]

print(elemento_especifico_i)

print("\n")

fila_3 = df.loc[2,:] # Accedemos a la fila con index 2 y todas sus cols

print(fila_3)

print("\n")

print(df)

print("\n")

mayores_de_edad = df.loc[df["age"] > 18 ,:]

print(mayores_de_edad)