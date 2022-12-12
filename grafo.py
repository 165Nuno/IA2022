#import matplotlib.pyplot as plt
from queue import Queue

import math
from Node import Node


class Graph:

    def __init__(self, directed=True):
        self.m_nodes = []
        self.m_directed = directed 
        self.m_graph = {}   
        #self.m_h={}       


    # Escrever o grafo como string
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    
    #####################################
    # Adicionar aresta no grafo, com peso
    ####################################
    def add_edge(self, node1, node2, weight):   #node1 e node2 são os 'nomes' de cada nodo
        n1 = Node(node1)     # cria um objeto node  com o nome passado como parametro
        n2 = Node(node2)     # cria um objeto node  com o nome passado como parametro
        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[node1] = set()
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            self.m_nodes.append(n2)
            self.m_graph[node2] = set()
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[node1].add((node2, weight))

        # se o grafo for nao direcionado, colocar a aresta inversa
        if not self.m_directed:
            self.m_graph[node2].add((node1, weight))

    ################################
    # Encontrar nodo pelo nome
    ################################
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None

    ###########################
    # Imprimir arestas
    ###########################
    def imprime_aresta(self):
        listaA = ""
        for nodo in self.m_graph.keys():
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################################
    # Devolver o custo de uma aresta
    ################################
    def get_arc_cost(self, node1, node2):
        custoT=math.inf
        a=self.m_graph[node1]    # lista de arestas para aquele nodo
        for (nodo,custo) in a:
            if nodo==node2:
                custoT=custo

        return custoT



    ######################################
    # Dado um caminho calcula o seu custo
    #####################################
    def calcula_custo(self, caminho):
        #caminho é uma lista de nomes de nodos
        teste=caminho
        custo=0
        i=0
        while i+1 < len(teste):
             custo=custo + self.get_arc_cost(teste[i], teste[i+1])
             i=i+1
        return custo


    ################################################################################
    # Procura DFS
    ####################################################################################
    def procura_DFS(self,start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT= self.calcula_custo(path)
            return (path, custoT)
        #print(start + str(self.m_graph[start]))
        for (adjacente, peso) in self.m_graph[start]:
            #print(adjacente)
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None
    
    
    
    
    ################################################################################
    # Procura BFS
    ####################################################################################
        
    def procura_BFS(self, start, end):
        queue = Queue()
        parents = {}
        visited = []
        caminho = []
        
        queue.put(start)
        parents[start] = set()
        parents[start].add(start) 
        while not queue.empty(): 
            node = queue.get()
            visited.append(node)
            pai = end
            for(adjacente, valor) in self.m_graph[node]:
                if adjacente == end:
                    parents[adjacente] = set()
                    parents[adjacente].add(node)
                    while pai != start:    
                        caminho.append(pai)
                        x = parents.get(pai)
                        pai = x.pop()
                    caminho.append(pai)
                    caminho.reverse()
                    custoT= self.calcula_custo(caminho)
                    return (caminho, custoT)

                if adjacente not in visited:
                    queue.put(adjacente)
                    parents[adjacente] = set()
                    parents[adjacente].add(node)
        return None
        
        



    