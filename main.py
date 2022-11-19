from matriz_adjacencia import Grafo

if __name__ == '__main__':
    #Cricao de um grafo
    grafo = Grafo(int(input('Informe a quantidade de vértices de G: ')))

    #Criacao de arestas
    grafo.criar_aresta(1, 2)
    grafo.criar_aresta(2, 3)
    grafo.criar_aresta(3, 4)

    #Remocao de arestas
    #grafo.remover_aresta(1, 2)
    #grafo.remover_aresta(3, 4)

    print('\nMatriz de adjacências definida:')
    grafo.obter_matriz()

    #Checagem da existencia de arestas
    print('\nChecagem da existência de aresta (1,2) ', grafo.checar_existencia_aresta(1, 2))

    #Checagem da quantidade de vertices e arestas
    print('\nChecagem da quantidade de vértices: ', grafo.checar_quantidade_vertices())
    #print('\nChecagem da quantidade de arestas: ', grafo.checar_quantidade_arestas())