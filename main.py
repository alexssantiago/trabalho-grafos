from matriz_adjacencia import Grafo

if __name__ == '__main__':
    grafo = Grafo(int(input('Informe a quantidade de vértices de G: ')))

    grafo.criar_aresta(1, 2)
    grafo.criar_aresta(2, 3)
    grafo.criar_aresta(3, 4)
    grafo.criar_aresta(4, 1)

    # grafo.remover_aresta(1, 2)
    # grafo.remover_aresta(3, 4)

    print('\nMatriz de adjacências definida:')
    grafo.obter_matriz()

    print('\nChecagem da existência de aresta (1,2): ', grafo.checar_existencia_aresta(1, 2))

    print('\nChecagem da quantidade de vértices: ', grafo.checar_quantidade_vertices())
    print('\nChecagem da quantidade de arestas: ', grafo.checar_quantidade_arestas())

    print('\nChecagem de grafo nulo: ', grafo.checar_grafo_nulo())
