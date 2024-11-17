# **Guía Rápida de los Problemas Algorítmicos**

Esta sección está diseñada para ayudarte a resolver problemas algorítmicos comunes usando estructuras de datos y técnicas clásicas. Aquí encontrarás módulos para cada tipo de estructura de datos y una colección de algoritmos que te ayudarán a abordar una gran variedad de desafíos. La idea es que cada módulo esté optimizado tanto en tiempo como en espacio para que puedas resolver los problemas de manera eficiente.

<!-- Table of contents -->

* [**1. Estructuras de Datos** (`structures`)](#1-estructuras-de-datos-structures)
    * [**¿Qué encontrarás aquí?**](#qué-encontrarás-aquí)
* [**2. Algoritmos** (`algorithms`)](#2-algoritmos-algorithms)
    * [**¿Qué hay en esta carpeta?**](#qué-hay-en-esta-carpeta)
* [**3. Utilidades Matemáticas** (`math_utils`)](#3-utilidades-matemáticas-math_utils)
    * [**¿Qué hay aquí?**](#qué-hay-aquí)
* [**4. Técnicas Algorítmicas** (`techniques`)](#4-técnicas-algorítmicas-techniques)
    * [**¿Qué hay aquí?**](#qué-hay-aquí-1)
* [**Consejos**](#consejos)

<!-- end -->

---

## **1. Estructuras de Datos** (`structures`)

### **¿Qué encontrarás aquí?**

Este paquete contiene las implementaciones de las estructuras de datos más comunes, fundamentales para resolver cualquier tipo de problema de programación. La clave de muchos algoritmos eficientes es elegir la estructura de datos correcta. Aquí te dejo un resumen de lo que puedes encontrar:

-   **`linked_list.py`**: Listas enlazadas (simples, dobles y circulares). Son útiles cuando necesitas insertar o eliminar elementos de manera rápida en cualquier parte de la lista.

    -   **Tip**: Son rápidas para insertar o eliminar, pero el acceso es más lento que en las listas normales (O(n)).

-   **`stack_queue.py`**: Pilas, colas y deque (colas dobles). Estas estructuras se usan mucho en algoritmos como BFS, DFS y otros que requieren un manejo ordenado de elementos.

    -   **Tip**: Las pilas son geniales para problemas recursivos y backtracking. Las colas se usan para BFS y problemas en los que necesitas procesar elementos en orden.

-   **`tree.py`**: Árboles binarios, AVL, B-trees. Perfectos para problemas que requieren búsquedas rápidas o estructuras jerárquicas.

    -   **Tip**: Los árboles binarios de búsqueda (BST) son buenos para búsquedas rápidas, pero los árboles AVL mantienen el árbol equilibrado, lo que hace que las búsquedas sean aún más eficientes.

-   **`graph.py`**: Implementación de grafos, tanto dirigidos como no dirigidos. Los grafos se usan cuando quieres representar relaciones entre elementos, como redes o dependencias.

    -   **Tip**: Usa listas de adyacencia si el grafo es disperso. Si el grafo es denso, las matrices de adyacencia pueden ser más eficaces.

-   **`heap.py`**: Montículos (heaps), tanto mínimos como máximos. Ideales para implementar colas de prioridad.

    -   **Tip**: Los heaps son perfectos para problemas donde necesitas acceder al mínimo o máximo rápidamente, como en la planificación de tareas o la selección de elementos.

-   **`hash_table.py`**: Tablas hash, para hacer búsquedas rápidas de elementos. Usadas en problemas que requieren acceso constante a datos con claves.

    -   **Tip**: Las tablas hash son súper rápidas para búsquedas (O(1) en promedio), pero ten cuidado con las colisiones.

-   **`trie.py`**: Árboles Trie, geniales para trabajar con cadenas de texto, como en problemas de autocompletado o búsqueda de prefijos.

    -   **Tip**: Si tienes que hacer búsquedas de cadenas o palabras en un conjunto grande de datos, un Trie puede ser tu mejor amigo.

-   **`union_find.py`**: Union-Find, también conocido como Disjoint Set, es muy útil para manejar conjuntos disjuntos, como en el algoritmo de Kruskal para encontrar el árbol de expansión mínima.

    -   **Tip**: Perfecto para problemas en grafos donde necesitas comprobar si dos elementos están en el mismo conjunto.

-   **`segment_tree.py`**: Árboles segmentados, ideales para hacer consultas de rango (por ejemplo, sumas o máximos) en secuencias de datos.

    -   **Tip**: Usa un árbol segmentado cuando necesites hacer muchas consultas de rango de manera eficiente.

-   **`fenwick_tree.py`**: Árboles Fenwick (o Binary Indexed Trees). Parecen segment trees pero son más eficientes en cuanto a espacio.
    -   **Tip**: Si tienes que hacer sumas acumuladas o actualizaciones de elementos en una secuencia, el Fenwick Tree es un buen candidato.

---

## **2. Algoritmos** (`algorithms`)

### **¿Qué hay en esta carpeta?**

Aquí encontrarás implementaciones de algunos de los algoritmos más usados para resolver problemas clásicos de programación. Todos están optimizados para que puedas resolver los problemas de la manera más eficiente posible. Tienes desde algoritmos de ordenación hasta búsqueda de caminos y manipulación de cadenas.

-   **`sorting.py`**: Diferentes algoritmos de ordenación, como Bubble Sort, Merge Sort, Quick Sort, Heap Sort, Radix Sort, entre otros.

    -   **Tip**: Para la mayoría de los casos, QuickSort y MergeSort son los mejores en cuanto a tiempo (O(n log n)). Radix y Bucket Sort son útiles para ciertos tipos de datos.

-   **`searching.py`**: Algoritmos de búsqueda: binaria, secuencial, de interpolación y exponencial.

    -   **Tip**: La búsqueda binaria es mucho más eficiente que la secuencial (O(log n) vs O(n)), pero solo funciona en listas ordenadas.

-   **`pathfinding.py`**: Algoritmos para encontrar caminos en grafos: BFS, DFS, Dijkstra, A\*, Floyd-Warshall, Bellman-Ford.
    -   **Tip**: Si el grafo es no ponderado, usa BFS. Para grafos ponderados, Dijkstra o A\* (si tienes heurísticas) son los mejores. Asegúrate de saber cuál se ajusta mejor a tu caso.

---

## **3. Utilidades Matemáticas** (`math_utils`)

### **¿Qué hay aquí?**

En esta carpeta encontrarás módulos que te ayudarán con cálculos matemáticos esenciales, como operaciones con números primos, combinatoria, teoría de números y más.

-   **`primes.py`**: Algoritmos para encontrar números primos, incluyendo la Criba de Eratóstenes.

    -   **Tip**: Si necesitas generar primos hasta un número n, usa la Criba de Eratóstenes. Es O(n log log n), ¡muy eficiente!

-   **`number_theory.py`**: Funciones para el cálculo de MCD, MCM y más.

    -   **Tip**: El algoritmo de Euclides es perfecto para calcular el MCD rápidamente (O(log n)).

-   **`geometry.py`**: Funciones geométricas básicas, como el cálculo de áreas y operaciones con líneas.

    -   **Tip**: Útil para resolver problemas de geometría computacional, como la intersección de líneas o el cálculo de áreas de polígonos.

-   **`probability.py`**: Herramientas para trabajar con probabilidades, combinaciones y permutaciones.
    -   **Tip**: Si tienes que resolver problemas que involucran probabilidades o combinatoria, este módulo es lo que necesitas.

---

## **4. Técnicas Algorítmicas** (`techniques`)

### **¿Qué hay aquí?**

Aquí es donde se encuentran las técnicas más avanzadas y poderosas para resolver problemas complejos. Este paquete contiene técnicas que puedes aplicar en una gran variedad de situaciones.

-   **`dynamic_programming.py`**: Técnicas de programación dinámica para optimizar problemas de optimización.

    -   **Tip**: La programación dinámica es genial para problemas donde los subproblemas se repiten. Asegúrate de guardar los resultados intermedios (memoization o tabulación) para no repetir cálculos innecesarios.

-   **`greedy.py`**: Algoritmos codiciosos, que siempre eligen la opción más prometedora en el momento.

    -   **Tip**: La técnica codiciosa puede no ser la mejor para todos los problemas, pero funciona de maravilla en problemas como el de la mochila o la selección de actividades.

-   **`backtracking.py`**: Algoritmos de retroceso (backtracking), útiles para problemas de búsqueda de soluciones combinatorias.

    -   **Tip**: Utiliza backtracking cuando el espacio de soluciones sea grande y necesites explorar todas las opciones posibles, como en problemas de n-reinas o Sudoku.

-   **`divide_and_conquer.py`**: Divide y vencerás: esta técnica divide un problema grande en subproblemas más pequeños y los resuelve por separado.
    -   **Tip**: Es genial para problemas como la ordenación (MergeSort, QuickSort), multiplicación de matrices y más.

---

## **Consejos**

1. **Optimiza en complejidad temporal**

    > Siempre que puedas, trata de elegir soluciones con menor complejidad temporal. Ojo, a veces un algoritmo que es O(n log n) es mucho mejor que uno que es O(n^2), ¡así que tenlo en cuenta!

2. **Escoge la estructura de datos correcta**

    > Asegúrate de elegir la estructura de datos adecuada según el problema. Algunas estructuras como las tablas hash o los árboles de búsqueda balanceados pueden hacer que tu solución sea mucho más rápida.

3. **Practica y prueba**
    > No olvides probar tus soluciones con casos de prueba. Los algoritmos no siempre se comportan como esperamos en situaciones límite.
