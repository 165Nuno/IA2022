
from Node import Node
from Graph import Grafo
from queue import Queue

class Pista():


    # start deve ser a capacidade dos dois baldes no inicio ex (0,0) "estado inicial"
    # goal deve ser o objectivo ex (2,0).  " estado final"
    # os estados são representados por "(x,y)" como string, em que x e y representam
    # as quantidades de agua nos jarros

    def __init__(self, start, goal,matrix):
        self.g=Grafo(directed=True)
        self.start=start
        self.goal=goal
        self.matrix = matrix




    def cria_grafo(self):
        print("OLA")
        estados = []
        estados.append(self.start) # adicionado o estado inicial
        visitados = []
        visitados.append(self.start) # adicionamos o estado inicial ao estados visitados


        while estados != []:
            print("OLA 2")
            estado = estados.pop()
            print("OLA 3")
            print(self.start)
            print(estado)
            print(estado[1])
            expansao = self.expande(estado)
            print("OlA 4")
            for e in expansao:
               # if verifica_fora_pista(e) == 1:
                #    self.g.add_edge(estado,e,25) ## Caso em que ele sai fora da pista fica com um custo de 25
                print(e)
                self.g.add_edge(estado,e,1)
                if e not in visitados:
                    estados.append(e)
                    visitados.append(e)


    def expande(self,estado):
        lista = []
        cordx = int(estado[1])
        cordy = int(estado[3])

        if self.matrix[cordx+1][cordy] != '#':
            res = "(" + str(cordx+1) + "," + str(cordy) + ")"
            lista.append(res)
        if self.matrix[cordx-1][cordy] != '#':
            res = "(" + str(cordx-1) + "," + str(cordy) + ")"
            lista.append(res)
        if self.matrix[cordx][cordy+1] != '#':
            res = "(" + str(cordx) + "," + str(cordy+1) + ")"    
            lista.append(res)
        if self.matrix[cordx][cordy-1] != '#':
            res = "(" + str(cordx) + "," + str(cordy-1) + ")"
            lista.append(res)
        return lista


# Função que verifica se estamos numa parede FIX ME
    def parede_verifica(self,matrix,estado):
        x = estado[0]
        y = estado[1]
        for i in range(len(matrix)):
            contlin = contlin + 1

        for j in range(i):
            contcol = contcol + 1 

# Função que verifica se um dado carro está fora da pista
# Caso esteja fora retorna 1 caso contrário retorna 0
    def verifica_fora_pista(estado,matrix):
        contlin = 0
        contcol = 0
        px = estado[0]
        py = estado[1]

        for i in range(len(matrix)):
            contlin = contlin + 1

        for j in range(i):
            contcol = contcol + 1  

        if px > contlin or px < 0 or py > contcol or py < 0:
            return 1
        else:
            return 0

    def verifica_parede(estado,matrix):
        cordx = estado[0]
        cordy = estado[1]
    
        if (matrix[cordx][cordy]) == '#':
            return 1
        else:
            return 0

    def edireita(self,estado):
        cordx = estado[0]
        cordy = estado[1]
        return (cordx+1,cordy)

    def eesquerda(self,estado):
        cordx = estado[0]
        cordy = estado[1]
        return (cordx-1,cordy)

    def ecima(self,estado):
        cordx = estado[0]
        cordy = estado[1]
        return (cordx,cordy+1)

    def ebaixo(self,estado):
        cordx = estado[0]
        cordy = estado[1]
        return (cordx,cordy-1)
# Cria o grafo
