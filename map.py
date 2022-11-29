import random
from prints import *

# Geração do Mapa Aleatório
def randomNumb(largura):
    string = ""
    #random.seed() ?????
    hm = largura
    while(hm > 0):
        if (hm == largura or hm == 1):
            string += "#"
            string += " "
        elif ((random.randint(1,100)) < 20):
            string += "#"
            string += " "
        else:
            string += "-"
            string += " "
        hm = hm - 1
    print(string)
    printar_file(string)

def meio(largura,altura):
    hm = altura - 2
    while(hm > 0):
        randomNumb(largura)
        hm = hm - 1

def printmetaplayer(pl,largura):
    hm = largura
    string = ""
    x = random.randint(1,hm)
    while(hm > 0):
        if (x == hm and pl == 2): 
            string += "F"
            string += " "
        elif (x == hm and pl == 1): 
            string += "P"
            string += " "
        else: 
            string += "#"
            string += " "
        hm = hm - 1
    print(string)
    printar_file(string)

# Função que gera o map aleatóriamente
def gera_mapa(largura,altura):
        printmetaplayer(1,largura)
        meio(largura,altura)
        printmetaplayer(2,largura)