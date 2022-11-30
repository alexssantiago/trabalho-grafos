import random
from matriz_adjacencia import Grafo


def main():
    # grafo.criar_aresta(1, 2)
    # grafo.criar_aresta(2, 3)
    # grafo.criar_aresta(3, 4)
    # grafo.criar_aresta(5, 2)
    # grafo.criar_aresta(5, 2, 3.1)
    criar_arestas_aleatorias()

    # grafo.remover_aresta(1, 3)
    # grafo.remover_aresta(3, 4)

    # grafo.ponderar_arestas(3, 4, 9.5)

    print('\nMatriz de adjacências definida:')
    grafo.obter_matriz()

    obter_existencia_aresta(1, 2)
    obter_adjacencia_entre_vertices(1, 2)
    obter_adjacencia_entre_arestas(2, 3, 5, 3)

    print('\nChecagem da quantidade de vértices: ', grafo.checar_quantidade_vertices())
    print('\nChecagem da quantidade de arestas: ', grafo.checar_quantidade_arestas())

    print('\nChecagem de grafo nulo: ', grafo.checar_grafo_nulo())


def obter_existencia_aresta(u, v):
    print('\nChecagem da existência de aresta (', u, ',', v, ')', ':', grafo.checar_existencia_aresta(u, v))


def obter_adjacencia_entre_vertices(u, v):
    print('\nChecagem de adjacência entre os vértices', u, 'e', v, ':', grafo.checar_adjacencia_entre_vertices(u, v))


def obter_adjacencia_entre_arestas(u1, v1, u2, v2):
    print('\nChecagem de adjacência entre as arestas (', u1, ',', v1, ') e (', u2, ',', v2, ') :',
          grafo.checar_adjacencia_entre_arestas(u1, v1, u2, v2))


def criar_arestas_aleatorias():
    qtd_vertices = grafo.checar_quantidade_vertices()
    for v in range(qtd_vertices):
        grafo.criar_aresta(random.randint(1, qtd_vertices), random.randint(1, qtd_vertices), round(random.random(), 1))


if __name__ == '__main__':
    grafo = Grafo(int(input('Informe a quantidade de vértices de G: ')))
    main()
