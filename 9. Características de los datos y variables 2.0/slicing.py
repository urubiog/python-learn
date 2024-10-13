# Rebanadas de iterables (iterable[inicio:final:paso])

texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."

frst_line = texto[:40] # Slicing
snd_line = texto[40:80]
...

print(frst_line)
print(snd_line)

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8 ,9]]

matriz = matriz[::-1]
print(matriz)