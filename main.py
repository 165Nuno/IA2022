import random
import sys
import os
import time
import numpy as np
from prints import *
from map import *
from grafo import *
from Node import *
from Pista import *


# Função que lê de um ficheiro um circuito e transforma-o em matrix
def converte_matrix():
    fin = open('mapa.txt','r')
    matrix=[]
    for line in fin.readlines():
        matrix.append( [ str(x) for x in line.split() ] )
    return matrix

# Função que devolve para cada posição "P" ou "F", uma lista com os tuplos das suas coordenadas
def retorna_coords_posicao(matrix,posicao):
    #a = np.array(matrix)
    #print(np.where(a=='P'))
        if (posicao == 'P'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'P']
            return resultado
        elif (posicao == 'F'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'F']
            return resultado
        elif (posicao == 'J'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'J']
            return resultado
        else :
            return null

# Função main
def main():
    var = -1
    menu()
    while var != 0:
        print("[1] - Gera Circuito")
        print("[2] - Gera Matriz correspondente ao Circuito escolhido")
        print("[3] - Mostrar Circuito Guardado")
        print("[4] - Cria Grafo")
        print("[5] - Aplicar DFS")
        print("[6] - Aplicar BFS")
        print("[0] - Saír")
        var = int(input("introduza a sua opcao-> "))
        if var == 0:
            print("Saindo.......")
        elif var == 1:
            largura = int(input("ESCOLHA A SUA LARGURA -> "))
            altura = int(input("ESCOLHA A SUA ALTURA -> "))
            open('mapa.txt', 'w').close()
            gera_mapa(largura,altura)
            l=input("prima enter para continuar")
        elif var == 2:
            print(converte_matrix())
            l=input("prima enter para continuar")
        elif var == 3:
            print_matrix()
            l=input("prima enter para continuar")
        elif var == 4:
            matrix = converte_matrix()
            start = retorna_coords_posicao(matrix,'P')
            startP = start[0]
            tuploP = (int(startP[0]),int(startP[1]))
            goal = retorna_coords_posicao(matrix,'F')
            goalF = goal[0]
            tuploF = (int(goalF[0]),int(goalF[1]))
            jogadorj= retorna_coords_posicao(matrix,'J')
            jogadorJ = jogadorj[0]
            tuploJ = (int(jogadorJ[0]),int(jogadorJ[1]))
            problema = Pista(tuploP,tuploF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tuploJ,tuploF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()
            print(problema.g)
            print(" ")
            print(problemaJ.g)
            l=input("prima enter para continuar")
        elif var == 5:
            matrix = converte_matrix()
            matrix_alteracao = converte_matrix()
            start = retorna_coords_posicao(matrix,'P')
            startP = start[0]
            tuploP = (int(startP[0]),int(startP[1]))
            goal = retorna_coords_posicao(matrix,'F')
            goalF = goal[0]
            tuploF = (int(goalF[0]),int(goalF[1]))
            problema = Pista(tuploP,tuploF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            caminho = problema.solucaoDFS(str(tuploP), str(tuploF))
            print(" ")
            print("==========> [Caminho que resultou da aplicação do Algoritmo DFS]")
            print(" ")
            print(caminho)
            print(" ")
            print("Tracking do caminho iniciando em breve....")

            time.sleep(4)

            for c in caminho[0]:
                x = c[1:-1].split(',')
                x1 = int(x[0])
                x2 = int(x[1])
                #print(matrix_alteracao)
                matrix_alteracao[x1][x2] = 'C'
                z = 0
                k = 0
            #print(matrix_alteracao[1][1])
            #print("======> Representação visual do caminho obtido")
            #print(" ")
                while (z < len(matrix_alteracao)):
                    strr = ""
                    while (k < len(matrix_alteracao[z])):
                
                        strr += matrix_alteracao[z][k]
                        strr += " "
                        k = k+1
                
                    k = 0
                    print(strr)
                    z += 1
                time.sleep(0.5)
                os.system('clear')
            l=input("prima enter para continuar")
        elif var == 6:
            matrix = converte_matrix()
            matrix_alteracao = converte_matrix()


            start = retorna_coords_posicao(matrix,'P')
            startP = start[0]
            tuploP = (int(startP[0]),int(startP[1]))
            goal = retorna_coords_posicao(matrix,'F')
            goalF = goal[0]
            tuploF = (int(goalF[0]),int(goalF[1]))
            jogadorj= retorna_coords_posicao(matrix,'J')
            jogadorJ = jogadorj[0]
            tuploJ = (int(jogadorJ[0]),int(jogadorJ[1]))
            print(tuploJ)
            problema = Pista(tuploP,tuploF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tuploJ,tuploF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()
            caminho=problema.solucaoBFS(str(tuploP),str(tuploF))
            caminhoJ = problemaJ.solucaoBFS(str(tuploJ),str(tuploF))
            print(" ")
            print("==========> [Caminho que resultou da aplicação do Algoritmo BFS]")
            print(" ")
            print(caminho)
            print(" ")
            print(caminhoJ)
            print(" ")
            print("Tracking do caminho iniciando em breve....")

            time.sleep(4)


            for c,r in zip(caminho[0],caminhoJ[0]):
                x = c[1:-1].split(',')
                x1 = int(x[0])
                x2 = int(x[1])
                gx1 = x1
                gx2 = x2
                w = r[1:-1].split(',')
                w1 = int(w[0])
                w2 = int(w[1])
                gw1 = w1
                gw2 = w2
               # matrix_alteracao[gx1][gx2] = '-'
               # matrix_alteracao[gw1][gw2] = '-'
                matrix_alteracao[x1][x2] = 'P'
                matrix_alteracao[w1][w2] = 'J'
                z = 0
                k = 0
                os.system('clear')
                
                while (z < len(matrix_alteracao)):
                    strr = ""
                    while (k < len(matrix_alteracao[z])):
                
                        strr += matrix_alteracao[z][k]
                        strr += " "
                        k = k+1
                
                    k = 0
                    print(strr)
                    z += 1
                time.sleep(0.5)
                matrix_alteracao[gx1][gx2] = '-'
                matrix_alteracao[gw1][gw2] = '-'
                
            l=input("prima enter para continuar")


            
    

if __name__ == "__main__":
    main()
