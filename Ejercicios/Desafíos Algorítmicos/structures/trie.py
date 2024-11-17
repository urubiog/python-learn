# structures/trie.py

class TrieNode:
    def __init__(self) -> None:
        """
        Inicializa un nodo del trie, que contiene un diccionario de hijos
        y un valor de finalización de palabra.
        """
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        """
        Inicializa un trie vacío.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserta una palabra en el trie.
        
        Parámetros:
        - word: La palabra a insertar en el trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Busca una palabra en el trie.
        
        Parámetros:
        - word: La palabra a buscar en el trie.
        
        Retorna:
        - True si la palabra existe en el trie, False si no.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Verifica si existe alguna palabra en el trie que comience con el prefijo dado.
        
        Parámetros:
        - prefix: El prefijo a verificar.
        
        Retorna:
        - True si el trie contiene alguna palabra que comience con el prefijo, False si no.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word: str) -> bool:
        """
        Elimina una palabra del trie si existe.
        
        Parámetros:
        - word: La palabra a eliminar.
        
        Retorna:
        - True si la palabra se eliminó exitosamente, False si no.
        """
        return self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, index: int) -> bool:
        """
        Elimina recursivamente una palabra del trie.
        
        Parámetros:
        - node: El nodo actual.
        - word: La palabra a eliminar.
        - index: El índice de la letra actual.
        
        Retorna:
        - True si la palabra se eliminó exitosamente, False si no.
        """
        if index == len(word):
            if not node.is_end_of_word:
                return False  # La palabra no existe.
            node.is_end_of_word = False
            return len(node.children) == 0  # El nodo puede ser eliminado si no tiene hijos.

        char = word[index]
        if char not in node.children:
            return False  # La palabra no existe.
        
        can_delete = self._delete(node.children[char], word, index + 1)
        
        if can_delete:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False

    def get_words(self) -> list[str]:
        """
        Devuelve una lista de todas las palabras almacenadas en el trie.
        
        Retorna:
        - Una lista con todas las palabras almacenadas en el trie.
        """
        words = []
        self._get_words(self.root, "", words)
        return words

    def _get_words(self, node: TrieNode, current_word: str, words: list[str]) -> None:
        """
        Obtiene recursivamente todas las palabras en el trie.
        
        Parámetros:
        - node: El nodo actual.
        - current_word: La palabra construida hasta el momento.
        - words: La lista donde se agregan las palabras completas.
        """
        if node.is_end_of_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._get_words(child_node, current_word + char, words)


# Ejercicio 1: Insertar una palabra en el trie
def insertar_palabra_trie(trie: Trie, word: str) -> None:
    """
    Inserta una palabra en el trie.
    
    Parámetros:
    - trie: El trie en el que se insertará la palabra.
    - word: La palabra a insertar.
    """
    pass


# Ejercicio 2: Buscar una palabra en el trie
def buscar_palabra_trie(trie: Trie, word: str) -> bool:
    """
    Busca una palabra en el trie.
    
    Parámetros:
    - trie: El trie en el que se buscará la palabra.
    - word: La palabra a buscar.
    
    Retorna:
    - True si la palabra se encuentra en el trie, False si no.
    """
    pass


# Ejercicio 3: Verificar si existe un prefijo en el trie
def verificar_prefijo_trie(trie: Trie, prefix: str) -> bool:
    """
    Verifica si hay alguna palabra en el trie que comience con el prefijo dado.
    
    Parámetros:
    - trie: El trie donde se buscará el prefijo.
    - prefix: El prefijo a verificar.
    
    Retorna:
    - True si el prefijo existe en el trie, False si no.
    """
    pass


# Ejercicio 4: Eliminar una palabra del trie
def eliminar_palabra_trie(trie: Trie, word: str) -> bool:
    """
    Elimina una palabra del trie.
    
    Parámetros:
    - trie: El trie de donde se eliminará la palabra.
    - word: La palabra a eliminar.
    
    Retorna:
    - True si la palabra se eliminó con éxito, False si no se pudo eliminar.
    """
    pass


# Ejercicio 5: Obtener todas las palabras del trie
def obtener_palabras_trie(trie: Trie) -> list[str]:
    """
    Obtiene todas las palabras almacenadas en el trie.
    
    Parámetros:
    - trie: El trie del que se extraerán las palabras.
    
    Retorna:
    - Una lista con todas las palabras en el trie.
    """
    pass

