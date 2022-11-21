class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def criar_aresta(self, u, v):
        self.manipular_aresta(u, v, 1)

    def remover_aresta(self, u, v):
        self.manipular_aresta(u, v, 0)

    def manipular_aresta(self, u, v, r):
        self.grafo[u - 1][v - 1] = r

    def checar_grafo_nulo(self):
        return self.checar_quantidade_arestas() == 0

    def checar_existencia_aresta(self, u, v):
        return self.obter_aresta(u, v) == 1

    def checar_quantidade_vertices(self):
        return self.vertices

    def checar_quantidade_arestas(self):
        qtd_arestas = 0
        for i in range(self.vertices):
            for y in self.grafo[i]:
                if y == 1:
                    qtd_arestas += 1
        return qtd_arestas

    def obter_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

    def obter_aresta(self, u, v):
        return self.grafo[u - 1][v - 1]