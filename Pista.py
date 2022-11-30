
from Node import Node
from grafo import Graph
from queue import Queue

class Pista():

    def __init__(self, start, goal,matrix,linha,coluna):
        self.g=Graph(directed=True) # Grafo
        self.start=start #Posição Start
        self.goal=goal #Posição End
        self.matrix = matrix #Matrix correspondente ao grafo
        self.linha = linha #Número de linhas da matrix
        self.coluna = coluna #Número de colunas da matrix

    # Serve para criar o grafo à medida que passa por todos os nodos
    def cria_grafo(self):
        estados = []
        estados.append(self.start) # adicionado o estado inicial
        #self.g.m_nodes.append(Node(self.start[0],self.start[1]))
        #self.g.m_graph[self.start] = set()
        visitados = []
        visitados.append(self.start) # adicionamos o estado inicial ao estados visitados


        while estados != []:
            estado = estados.pop()
            expansao = self.expande(estado)
            for e in expansao:
                self.g.add_edge(str(estado),str(e),1)
                if e not in visitados: 
                    estados.append(e)
                    visitados.append(e)



# Serve para obter numa lista, todos os estados possiveis a partir do estado atual que nos encontramos
    def expande(self,estado):
        lista = []
        cordx = estado[0]
        cordy = estado[1]

        if cordx+1 < self.linha and self.matrix[cordx+1][cordy] != '#':
            res = (cordx+1,cordy)
            lista.append(res)
        if cordx-1 > 0 and self.matrix[cordx-1][cordy] != '#' :
            res = (cordx-1,cordy)
            lista.append(res)
        if  cordy+1 < self.coluna and self.matrix[cordx][cordy+1] != '#':
            res = (cordx,cordy+1) 
            lista.append(res)
        if cordy-1>0 and self.matrix[cordx][cordy-1] != '#':
            res = (cordx,cordy-1)
            lista.append(res)
        return lista


    # Aplica a Procura BFS
    def solucaoBFS(self,start,goal):
        return self.g.procura_BFS(str(start),str(goal))

    # Aplica a Procura DFS
    def solucaoDFS(self,start,goal):
        res=self.g.procura_DFS(start,goal,path=[], visited=set())
        return (res)