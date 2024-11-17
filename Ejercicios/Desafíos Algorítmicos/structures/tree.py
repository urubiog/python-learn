# structures/tree.py


class Node:
    def __init__(self, val: int | float) -> None:
        """
        Inicializa un nodo con un valor dado y dos hijos (izquierda y derecha) nulos.

        Parámetros:
        - val: El valor del nodo.
        """
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        """
        Inicializa un árbol binario vacío.
        """
        self.root = None

    def insert(self, val: int | float) -> None:
        """
        Inserta un nuevo nodo en el árbol binario.

        Parámetros:
        - val: El valor del nodo a insertar.
        """
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node: Node, val: int | float) -> None:
        """
        Inserta recursivamente un nuevo nodo en el árbol binario siguiendo el criterio de orden.

        Parámetros:
        - node: El nodo actual en el árbol.
        - val: El valor del nodo a insertar.
        """
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def search(self, val: int | float) -> bool:
        """
        Busca un valor en el árbol binario.

        Parámetros:
        - val: El valor a buscar.

        Retorna:
        - True si el valor está presente en el árbol, False si no lo está.
        """
        return self._search(self.root, val)

    def _search(self, node: Node, val: int | float) -> bool:
        """
        Busca recursivamente un valor en el árbol binario.

        Parámetros:
        - node: El nodo actual.
        - val: El valor a buscar.

        Retorna:
        - True si el valor se encuentra, False si no.
        """
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def inorder(self) -> list[int | float]:
        """
        Realiza un recorrido en orden (inorder) en el árbol binario y devuelve una lista de valores.

        Retorna:
        - Una lista de los valores de los nodos en orden ascendente.
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Node, result: list[int | float]) -> None:
        """
        Realiza un recorrido recursivo en orden (inorder) en el árbol binario.

        Parámetros:
        - node: El nodo actual.
        - result: Lista donde se guardan los valores.
        """
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def preorder(self) -> list[int | float]:
        """
        Realiza un recorrido preorden (preorder) en el árbol binario y devuelve una lista de valores.

        Retorna:
        - Una lista de los valores de los nodos en preorden.
        """
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: Node, result: list[int | float]) -> None:
        """
        Realiza un recorrido recursivo preorden (preorder) en el árbol binario.

        Parámetros:
        - node: El nodo actual.
        - result: Lista donde se guardan los valores.
        """
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self) -> list[int | float]:
        """
        Realiza un recorrido postorden (postorder) en el árbol binario y devuelve una lista de valores.

        Retorna:
        - Una lista de los valores de los nodos en postorden.
        """
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: Node, result: list[int | float]) -> None:
        """
        Realiza un recorrido recursivo postorden (postorder) en el árbol binario.

        Parámetros:
        - node: El nodo actual.
        - result: Lista donde se guardan los valores.
        """
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

    def height(self) -> int:
        """
        Devuelve la altura del árbol binario.

        Retorna:
        - La altura del árbol.
        """
        return self._height(self.root)

    def _height(self, node: Node) -> int:
        """
        Calcula la altura recursiva del árbol binario.

        Parámetros:
        - node: El nodo actual.

        Retorna:
        - La altura del nodo.
        """
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1


# Ejercicio 1: Insertar un nodo en el árbol binario
def insertar_nodo_arbol(val: int | float) -> BinaryTree:
    """
    Crea un árbol binario e inserta un nodo en el árbol.

    Parámetros:
    - val: El valor a insertar.

    Retorna:
    - El árbol con el nodo insertado.
    """
    pass


# Ejercicio 2: Buscar un valor en el árbol binario
def buscar_valor_arbol(arbol: BinaryTree, val: int | float) -> bool:
    """
    Busca un valor en un árbol binario.

    Parámetros:
    - arbol: El árbol donde se realizará la búsqueda.
    - val: El valor a buscar.

    Retorna:
    - True si el valor se encuentra en el árbol, False si no.
    """
    pass


# Ejercicio 3: Realizar un recorrido en orden (Inorder)
def recorrido_inorder(arbol: BinaryTree) -> list[int | float]:
    """
    Realiza un recorrido en orden del árbol binario.

    Parámetros:
    - arbol: El árbol donde se realizará el recorrido.

    Retorna:
    - Una lista con los valores en orden ascendente.
    """
    pass


# Ejercicio 4: Realizar un recorrido preorden (Preorder)
def recorrido_preorder(arbol: BinaryTree) -> list[int | float]:
    """
    Realiza un recorrido preorden del árbol binario.

    Parámetros:
    - arbol: El árbol donde se realizará el recorrido.

    Retorna:
    - Una lista con los valores en preorden.
    """
    pass


# Ejercicio 5: Realizar un recorrido postorden (Postorder)
def recorrido_postorder(arbol: BinaryTree) -> list[int | float]:
    """
    Realiza un recorrido postorden del árbol binario.

    Parámetros:
    - arbol: El árbol donde se realizará el recorrido.

    Retorna:
    - Una lista con los valores en postorden.
    """
    pass


# Ejercicio 6: Calcular la altura del árbol
def calcular_altura_arbol(arbol: BinaryTree) -> int:
    """
    Calcula la altura de un árbol binario.

    Parámetros:
    - arbol: El árbol binario.

    Retorna:
    - La altura del árbol.
    """
    pass
