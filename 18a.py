def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

# Grafo de conexiones entre ciudades
grafo = {
    'A': {'B': 5, 'C': 8, 'D': 9},
    'B': {'A': 5, 'E': 15, 'F': 7},
    'C': {'A': 8, 'G': 12, 'H': 10},
    'D': {'A': 9, 'I': 11, 'J': 6},
    'E': {'B': 15, 'K': 9, 'L': 13},
    'F': {'B': 7, 'M': 8, 'N': 6},
    'G': {'C': 12, 'O': 10, 'P': 5},
    'H': {'C': 10, 'Q': 11, 'R': 7},
    'I': {'D': 11, 'S': 14, 'T': 8},
    'J': {'D': 6, 'U': 9, 'V': 12},
    'K': {'E': 9},
    'L': {'E': 13},
    'M': {'F': 8},
    'N': {'F': 6},
    'O': {'G': 10},
    'P': {'G': 5},
    'Q': {'H': 11},
    'R': {'H': 7},
    'S': {'I': 14},
    'T': {'I': 8},
    'U': {'J': 9},
    'V': {'J': 12}
}

# Función para encontrar la ruta más corta entre dos ciudades
def encontrar_ruta_mas_corta(origen, destino):
    ruta = dfs(grafo, origen, destino)
    if ruta:
        return ' '.join(ruta)
    else:
        return 'None'

# Leer entrada de usuario
origen, destino = input().split()

# Encontrar y mostrar la ruta más corta
print(encontrar_ruta_mas_corta(origen, destino))
