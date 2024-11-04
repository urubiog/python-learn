class MiExcepcion(Exception): # Esto crea una clase de excepción
    def __init__(self, err): # Definimos su funcionamiento con self y err que será el input hacía la function
        print(f"Has cometido un error: {err}") # Imprimimos el error
        
raise MiExcepcion("Te has metido en programación\nAhora sufrirás") # Esto sirve para provocar manualmente una excepción