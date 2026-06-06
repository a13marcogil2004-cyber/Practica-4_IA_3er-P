import heapq

grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

def prim(grafo, inicio):
    visitados = set([inicio])
    aristas = []

    for vecino, peso in grafo[inicio]:
        heapq.heappush(aristas, (peso, inicio, vecino))

    mst = []
    costo_total = 0
    paso = 1

    print(f"\nNodo inicial: {inicio}\n")

    while aristas:
        peso, origen, destino = heapq.heappop(aristas)

        if destino in visitados:
            continue

        visitados.add(destino)
        mst.append((origen, destino, peso))
        costo_total += peso
