import random
import sys
import numpy as np
from prints import *
from map import *
from Graph import *
from Node import *
from Pista import *


# Função que transforma o circuito em um grafo
def converte_matrix():
    fin = open('mapa.txt','r')
    matrix=[]
    for line in fin.readlines():
        matrix.append( [ str(x) for x in line.split() ] )
    return matrix


def retorna_coords_posicao(matrix,posicao):
    #a = np.array(matrix)
    #print(np.where(a=='P'))
        if (posicao == 'P'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'P']
            return resultado
        elif (posicao == 'F'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'F']
            return resultado
        else :
            return null




def main():
    var = -1
    est = (39,3)

    #xd = retorna_coords_posicao(matrix,'P')
    # print(verifica_forapista(xd[0],matrix))
    menu()
    while var != 0:
        print("1-Gera Circuito")
        print("2-Gera Matriz correspondente ao Circuito escolhido")
        print("3-Coords do P")
        print("4-BFS")
        print("5-DFS")
        print("0-Saír")
        var = int(input("introduza a sua opcao-> "))
        if var == 0:
            print("Saindo.......")
        elif var == 1:
            largura = int(input("ESCOLHA A SUA LARGURA -> "))
            altura = int(input("ESCOLHA A SUA ALTURA-> "))
            open('mapa.txt', 'w').close()
            gera_mapa(largura,altura)
            l=input("prima enter para continuar")
        elif var == 2:
            print(converte_matrix())
            l=input("prima enter para continuar")
        elif var == 3:
            matrix = converte_matrix()
            print(retorna_coords_posicao(matrix,'P'))
            x = retorna_coords_posicao(matrix,'P')
            print(verifica_parede((1,0),matrix))
            print(eesquerda((1,0)))
            l=input("prima enter para continuar")
        elif var == 4:
            matrix = converte_matrix()
            startT = retorna_coords_posicao(matrix,'P')
            start = startT[0]
            resS = "(" + str(start[0]) + "," + str(start[1]) + ")"
            goalL = retorna_coords_posicao(matrix,'F')
            goal = goalL[0]
            resG = "(" + str(goal[0]) + "," + str(goal[1]) + ")"
            problema = Pista(resS,resG,matrix)
            problema.cria_grafo()
            caminho=problema.solucaoDFS(start[0],goal[0])
            print(caminho)
            print("ola")
            #print(expande((5,5),matrix))
            l=input("prima enter para continuar")
        elif var == 5:
            matrix = converte_matrix()
            start = retorna_coords_posicao(matrix,'P')
            goal = retorna_coords_posicao(matrix,'F')
            problema = Pista(start[0],goal[0],matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            caminho=problema.solucaoDFS(start[0], goal[0])
            # caminho=problema.solucaoBFS(start[0],goal[0])
            print(problema)
            l=input("prima enter para continuar")

            
    

if __name__ == "__main__":
    main()