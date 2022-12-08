import random
from matriz_adjacencia import MatrizAdjacencia


def main():
    grafo.criar_aresta(1, 2)
    grafo.criar_aresta(2, 3)
    grafo.criar_aresta(3, 1)
    grafo.criar_aresta(2, 4)
    grafo.criar_aresta(5, 4)
    # criar_arestas_aleatorias()

    # grafo.remover_aresta(1, 3)
    # grafo.remover_aresta(3, 4)

    # grafo.ponderar_arestas(3, 4, 9.5)

    print('\nMatriz de adjacências definida:')
    grafo.obter_matriz()

    # obter_existencia_aresta_aleatoria()
    # obter_existencia_aresta(1, 2)

    # obter_adjacencia_entre_vertices_aleatorios()
    # obter_adjacencia_entre_vertices(1, 2)

    # obter_adjacencia_entre_arestas(2, 3, 5, 3)

    print('\nChecagem da quantidade de vértices: ', grafo.checar_quantidade_vertices())
    print('\nChecagem da quantidade de arestas: ', grafo.checar_quantidade_arestas())

    print('\nChecagem de grafo nulo: ', grafo.checar_grafo_nulo())
    print('\nChecagem de grafo completo: ', grafo.checar_grafo_completo())

    print('\nTarjan: ', lowtime_tarjan())


def obter_existencia_aresta(u, v):
    print('\nChecagem da existência de aresta (', u, ',', v, ')', ':', grafo.checar_existencia_aresta(u, v))


def criar_arestas_aleatorias():
    qtd_vertices = grafo.checar_quantidade_vertices()
    for v in range(qtd_vertices):
        grafo.criar_aresta(random.randint(1, qtd_vertices), random.randint(1, qtd_vertices), round(random.random(), 1))


def obter_existencia_aresta_aleatoria():
    qtd_vertices = grafo.checar_quantidade_vertices()
    obter_existencia_aresta(random.randint(1, qtd_vertices), random.randint(1, qtd_vertices))


def obter_adjacencia_entre_vertices_aleatorios():
    qtd_vertices = grafo.checar_quantidade_vertices()
    obter_adjacencia_entre_vertices(random.randint(1, qtd_vertices), random.randint(1, qtd_vertices))


def obter_adjacencia_entre_vertices(u, v):
    print('\nChecagem de adjacência entre os vértices', u, 'e', v, ':', grafo.checar_adjacencia_entre_vertices(u, v))


def obter_adjacencia_entre_arestas(u1, v1, u2, v2):
    print('\nChecagem de adjacência entre as arestas (', u1, ',', v1, ') e (', u2, ',', v2, ') :',
          grafo.checar_adjacencia_entre_arestas(u1, v1, u2, v2))


def tarjan(graph, visited, node, parent, par, intime, lowtime, lst):
    global timer
    visited[node] = 1
    lst.append(node)
    parent[node] = par
    intime[node] = timer
    lowtime[node] = timer
    timer += 1
    for child in graph[node]:
        if not visited[child]:
            tarjan(graph, visited, child, parent, node, intime, lowtime, lst)
            lowtime[node] = min(lowtime[node], lowtime[child])
        else:
            if child != par and (child in lst):
                lowtime[node] = min(lowtime[node], intime[child])


def lowtime_tarjan():
    visited = {}
    parent = {}
    intime = {}
    lowtime = {}
    # timer = 1

    qtd_vertices = grafo.checar_quantidade_vertices()

    for i in range(1, qtd_vertices + 1):
        visited[i] = 0
        parent[i] = None
        intime[i] = None
        lowtime[i] = None

    for i in range(1, qtd_vertices + 1):
        if not visited[i]:
            lst = []
            tarjan(grafo, visited, i, parent, -1, intime, lowtime, lst)
            print(lowtime)


if __name__ == '__main__':
    grafo = MatrizAdjacencia(int(input('Informe a quantidade de vértices de G: ')))
    timer = 1
    main()
