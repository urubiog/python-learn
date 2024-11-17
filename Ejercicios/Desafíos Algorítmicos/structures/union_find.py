# structures/union_find.py

class UnionFind:
    def __init__(self, size: int) -> None:
        """
        Inicializa una estructura de Union-Find con un número de elementos determinado.
        
        Parámetros:
        - size: El número de elementos en el conjunto.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        """
        Encuentra el representante del conjunto al que pertenece el elemento x, aplicando
        compresión de caminos para optimizar futuras búsquedas.
        
        Parámetros:
        - x: El elemento del cual se busca el representante.
        
        Retorna:
        - El representante del conjunto al que pertenece x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compresión de caminos
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Une los conjuntos que contienen a los elementos x e y, utilizando la técnica de
        unión por rango para mantener la estructura equilibrada.
        
        Parámetros:
        - x: Un elemento del primer conjunto.
        - y: Un elemento del segundo conjunto.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Unión por rango: el árbol más pequeño se adjunta al más grande
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Verifica si los elementos x e y pertenecen al mismo conjunto.
        
        Parámetros:
        - x: El primer elemento.
        - y: El segundo elemento.
        
        Retorna:
        - True si x e y pertenecen al mismo conjunto, False si no.
        """
        return self.find(x) == self.find(y)


# Ejercicio 1: Unir dos conjuntos
def unir_conjuntos(uf: UnionFind, x: int, y: int) -> None:
    """
    Une los conjuntos que contienen los elementos x e y.
    
    Parámetros:
    - uf: La instancia de UnionFind.
    - x: Un elemento del primer conjunto.
    - y: Un elemento del segundo conjunto.
    """
    pass


# Ejercicio 2: Verificar si dos elementos están en el mismo conjunto
def verificar_conexion(uf: UnionFind, x: int, y: int) -> bool:
    """
    Verifica si los elementos x e y pertenecen al mismo conjunto.
    
    Parámetros:
    - uf: La instancia de UnionFind.
    - x: El primer elemento.
    - y: El segundo elemento.
    
    Retorna:
    - True si x e y están conectados (pertenecen al mismo conjunto), False si no.
    """
    pass


# Ejercicio 3: Encontrar el representante de un conjunto
def encontrar_representante(uf: UnionFind, x: int) -> int:
    """
    Encuentra el representante del conjunto al que pertenece el elemento x.
    
    Parámetros:
    - uf: La instancia de UnionFind.
    - x: El elemento del cual se encuentra el representante.
    
    Retorna:
    - El representante del conjunto al que pertenece x.
    """
    pass


# Ejercicio 4: Realizar múltiples uniones
def realizar_uniones(uf: UnionFind, uniones: list[tuple[int, int]]) -> None:
    """
    Realiza múltiples uniones en el conjunto de UnionFind.
    
    Parámetros:
    - uf: La instancia de UnionFind.
    - uniones: Una lista de tuplas donde cada tupla (x, y) representa una unión entre los
      elementos x e y.
    """
    pass


# Ejercicio 5: Encontrar si un conjunto está totalmente conectado
def conjunto_totalmente_conectado(uf: UnionFind) -> bool:
    """
    Verifica si todos los elementos están en el mismo conjunto.
    
    Parámetros:
    - uf: La instancia de UnionFind.
    
    Retorna:
    - True si todos los elementos pertenecen al mismo conjunto, False si no.
    """
    pass

