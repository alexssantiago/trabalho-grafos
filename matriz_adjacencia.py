class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def criar_aresta(self, u, v, r=0):
        self.manipular_aresta(u, v, 1 if r == 0 else r)

    def remover_aresta(self, u, v):
        if self.grafo[u - 1][v - 1] == 0:
            print('\nAresta (', u, ',', v, ') não existe!')
        else:
            self.manipular_aresta(u, v, 0)

    def manipular_aresta(self, u, v, r):
        self.grafo[u - 1][v - 1] = r

    def checar_grafo_nulo(self):
        return self.checar_quantidade_arestas() == 0

    def checar_existencia_aresta(self, u, v):
        return self.obter_aresta(u, v) > 0

    def checar_quantidade_vertices(self):
        return len(self.grafo)

    def checar_quantidade_arestas(self):
        qtd_arestas = 0
        for i in range(self.vertices):
            for y in self.grafo[i]:
                if y != 0:
                    qtd_arestas += 1
        return qtd_arestas

    def obter_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

    def obter_aresta(self, u, v):
        return self.grafo[u - 1][v - 1]

    def checar_adjacencia_entre_vertices(self, u, v):
        return self.checar_existencia_aresta(u, v)

    def checar_adjacencia_entre_arestas(self, u1, v1, u2, v2):
        return self.checar_existencia_aresta(u1, u2) or self.checar_existencia_aresta(u1, v2) \
               or self.checar_existencia_aresta(v1, v2) or self.checar_existencia_aresta(v1, u2)

    def ponderar_arestas(self, u, v, r):
        self.manipular_aresta(u, v, r)
        print('\nPonderação de aresta (', u, ',', v, ')', ':', r)
