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

def gera_tuplo(lista):
    listaNova = lista[0]
    tuploN = (int(listaNova[0]),int(listaNova[1]), 0, 0)
    return tuploN

def tracking(caminho1,caminho2,matrix):
    for c,r in zip(caminho1[0],caminho2[0]):
                x = c[1:-1].split(',')
                x1 = int(x[0])
                x2 = int(x[1])
               
                w = r[1:-1].split(',')
                w1 = int(w[0])
                w2 = int(w[1])
                matrix[x1][x2] = 'P'
                matrix[w1][w2] = 'J'
                z = 0
                k = 0
                os.system('clear')
                
                while (z < len(matrix)):
                    strr = ""
                    while (k < len(matrix[z])):
                
                        strr += matrix[z][k]
                        strr += " "
                        k = k+1
                
                    k = 0
                    print(strr)
                    z += 1
                time.sleep(0.5)
                matrix[x1][x2] = '-'
                matrix[w1][w2] = '-'

def prints(x, y, caminho, caminhoJ): 
     
     print(" ")
 
     if (x == 1):
         print_dfs()
     elif(x == 2):
         print_bfs()
     elif(x == 3):
         print_astar()
     elif(x == 4):
         print_greedy()
 
     print("===> Caminho do Jogador P")
     print(caminho)
     print(" ")
 
     if (y == 1):
         print_dfs()
     elif (y == 2):
         print_bfs()
     elif (y == 3):
         print_astar()
     elif (y == 4):
         print_greedy()
 
     print("===> Caminho do jogador J")
     print(caminhoJ)
     print(" ")


# Função main
def main():
    var = -1
    menu()
    while var != 0:
        print("[1] - Gera Circuito")
        print("[2] - Gera Matriz correspondente ao Circuito escolhido")
        print("[3] - Mostrar Circuito Guardado")
        print("[4] - Cria Grafo")
        print("[5] - Correr Algoritmos")
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
            goal = retorna_coords_posicao(matrix,'F')
            jogadorj= retorna_coords_posicao(matrix,'J')
            tP=gera_tuplo(start)
            tF=gera_tuplo(goal)
            tJ= gera_tuplo(jogadorj)
            problema = Pista(tP,tF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tJ,tF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()
            print("========> [GRAFO DO JOGADOR P]")
            print(problema.g)
            print(" ")
            print("========> [GRAFO DO JOGADOR J]")
            print(problemaJ.g)
            l=input("prima enter para continuar")
        elif var == 5:
            print("[1] -> Algoritmo DFS")
            print("[2] -> Algoritmo BFS")
            print("[3] -> Algoritmo aStar")
            print("[4] -> Algoritmo Greedy")
            varP = int(input("Escolha um algoritmo para o jogador P -> "))
            varJ = int(input("Escolha um algoritmo para o jogador J -> "))


            matrix = converte_matrix()
            matrix_alteracao = converte_matrix()
            start = retorna_coords_posicao(matrix,'P')
            goal = retorna_coords_posicao(matrix,'F')
            jogadorj= retorna_coords_posicao(matrix,'J')
            tP=gera_tuplo(start)
            tF=gera_tuplo(goal)
            tJ= gera_tuplo(jogadorj)
            problema = Pista(tP,tF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tJ,tF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()

            if   (varP == 1):
                caminho=problema.solucaoDFS(str(tP),str(tF))                                # Gera a solucao BFS para o jogador P

            elif (varP == 2):
                caminho=problema.solucaoBFS(str(tP),str(tF))
            
            elif (varP == 3):
                caminho=problema.solucaoAstar(str(tP),str(tF))

            elif (varP == 4):
                caminho=problema.solucaoGreedy(str(tP),str(tF))


            if   (varJ == 1):
                caminhoJ=problemaJ.solucaoDFS(str(tJ),str(tF))                                # Gera a solucao BFS para o jogador P
 
            elif (varJ == 2):
                caminhoJ=problemaJ.solucaoBFS(str(tJ),str(tF))
 
            elif (varJ == 3):
                caminhoJ=problemaJ.solucaoAstar(str(tJ),str(tF))
 
            elif (varJ == 4):
                caminhoJ=problemaJ.solucaoGreedy(str(tJ),str(tF))

            prints(varP, varJ, caminho, caminhoJ) 
            print("Tracking do caminho iniciando em breve....")
            time.sleep(4)
            tracking(caminho,caminhoJ,matrix_alteracao)
            l=input("prima enter para continuar")


            

if __name__ == "__main__":
    main()
