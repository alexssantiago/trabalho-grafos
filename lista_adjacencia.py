class ListaAdjacencia:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def criar_aresta(self, u, v):
        self.manipular_aresta(u, v)

    def manipular_aresta(self, u, v):
        self.grafo[u - 1].append(v)

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

    def obter_aresta(self, u, v):
        return self.grafo[u - 1][v]

    def checar_adjacencia_entre_vertices(self, u, v):
        return self.checar_existencia_aresta(u, v)

    def checar_adjacencia_entre_arestas(self, u1, v1, u2, v2):
        return self.checar_existencia_aresta(u1, u2) or self.checar_existencia_aresta(u1, v2) \
               or self.checar_existencia_aresta(v1, v2) or self.checar_existencia_aresta(v1, u2)

    def ponderar_arestas(self, u, v, r):
        self.manipular_aresta(u, v, r)
        print('\nPonderação de aresta (', u, ',', v, ')', ':', r)

    def checar_grafo_completo(self):
        completo = True
        total_vertices = self.checar_quantidade_vertices()
        qtd_arestas = 0
        for i in range(self.vertices):
            qtd_arestas = 0
            for y in self.grafo[i]:
                if y != 0:
                    qtd_arestas += 1
        if qtd_arestas < total_vertices:
            return False

        return completo

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i + 1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

# g = Grafo(4)

# g.criar_aresta(1,2)
# g.criar_aresta(1,3)
# g.criar_aresta(1,4)
# g.criar_aresta(2,3)

# g.mostra_lista()