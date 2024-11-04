# La herencia sirve para reutilizar una clase con otras clases heredadas (clases hijas)

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona): # La clase empleado hereda los atributos de la clase Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # De la superclase inicializamos el constructor
        super().__init__(nombre, edad, nacionalidad)  # Se quita 'self' como primer argumento y usamos la función super().__init__() con los parámetros de la clase padre
        self.trabajo = trabajo # Definimos nuevos atributos própios de esta clase
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, institucion, media):
        # De la superclase inicializamos el constructor
        super().__init__(nombre, edad, nacionalidad)  # Se quita 'self' como primer argumento
        self.institucion = institucion
        self.media = media

class EmpleadoEstudiante(Empleado, Estudiante):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario, institucion, media, ganas):
        # Se utiliza super() para acceder a los métodos de las superclases
        super(Empleado).__init__(nombre, edad, nacionalidad, trabajo, salario)
        super(Estudiante).__init__(nombre, edad, nacionalidad, institucion, media)
        self.ganas = ganas

    def motivation_to_live(self):
        # Se utiliza super() para acceder al atributo 'nombre' de la superclase
        return f"Yo, {super().nombre}, tengo {self.ganas} ganas de vivir"


Daniel = EmpleadoEstudiante("Daniel", 48, "español", "empresario", 2000, "Fotovoltaics", 7.4, 1000)

# Se corrige la llamada a la función agregando paréntesis
print(Daniel.motivation_to_live())