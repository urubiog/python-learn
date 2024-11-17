# La clase Node se define de la siguiente manera...
class Node:
    def __init__(self, val: int | float, next: "Node") -> None:
        self.val = val
        self.next = next

# Ejercicio 1: Crear una lista simplemente enlazada desde un arreglo
def crear_lista_desde_arreglo(arreglo: list[int]) -> Node:
    """
    Crea una lista simplemente enlazada a partir de un arreglo de enteros.
    """
    pass


# Ejercicio 2: Recorrer e imprimir los elementos de la lista
def imprimir_lista(cabeza: Node) -> None:
    """
    Recorre la lista simplemente enlazada e imprime cada elemento.
    """
    pass


# Ejercicio 3: Insertar un nodo en la cabeza
def insertar_en_cabeza(cabeza: Node, valor: int) -> Node:
    """
    Inserta un nodo con el valor dado al inicio de la lista.
    """
    pass


# Ejercicio 4: Eliminar un nodo por valor
def eliminar_por_valor(cabeza: Node, valor: int) -> Node:
    """
    Elimina el primer nodo que contiene el valor especificado.
    """
    pass


# Ejercicio 5: Encontrar el elemento medio de la lista
def encontrar_elemento_medio(cabeza: Node) -> int:
    """
    Encuentra y devuelve el valor del nodo medio de la lista.
    """
    pass


# Ejercicio 6: Detectar ciclos en la lista
def detectar_ciclo(cabeza: Node) -> bool:
    """
    Determina si la lista contiene un ciclo.
    """
    pass
