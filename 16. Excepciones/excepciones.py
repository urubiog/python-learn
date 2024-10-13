def suma_dos(): # Esta function lo único que hace es sumar dos número y devolver el resultado
    while True: # Lo metemos en un bucle hasta que no se consiga obtener el resultado
        a = input("Introduce un número 1: ")
        b = input("Introduce un segundo número 2: ")
        try: # Intentamos obtener el resultado
            resultado = int(a) + int(b)
            
            print(f"La suma de ellos es {resultado}")
            
        except Exception as e: # Si no se puede mandamos esta Exception (que es clase exception)
            print(f"Te pedí solo dos números \n      Error: {e}")
            
        else: # Este else se ejecuta en caso de que try no mande una excepción
            break
        
        finally: # Esto se ejecuta siempre tras el try y (else o except)
            print("\nIntento de suma hecho\n")
            
    return resultado # Devolvemos el resultado
        
suma_dos()