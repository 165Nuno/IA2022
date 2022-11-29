
import numpy as np

# Função que devolve um array de tuplo com as posições daquilo que pretendemos
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
    
# Função que printa o mapa
def print_matrix():
    file = open('text.txt') 
    print(file.read())

# Função que transforma o circuito em uma matrix
def converte_matrix():
    fin = open('mapa.txt','r')
    matrix=[]
    for line in fin.readlines():
        matrix.append( [ str(x) for x in line.split() ] )
    return matrix

def teste (xd):
    str = ""
    for e in xd:
      x1 = str(e[0])
      x2 = str(e[1])
      str = "(" + x1 + "," + x2 + ")"
    return str
    

def converter(xd):
    delimitador = ","
    res = delimitador.join([str(value) for value in xd])
    return xd

# Função que verifica se um dado carro está fora da pista
# Caso esteja fora retorna 1 caso contrário retorna 0
def verifica_forapista(estado,matrix):
    contlin = 0
    contcol = 0
    px = int(estado[1])
    py = int(estado[3])

    for i in range(len(matrix)):
        contlin = contlin + 1

    for j in range(i):
        contcol = contcol + 1  

    if px > contlin or px < 0 or py > contcol or py < 0:
        return 1
    else:
        return 0

# Cria o grafo
def cria_grafo(self):
        estados = []
        estados.append(self.start) # adicionado o estado inicial
        visitados = []
        visitados.append(self.start) # adicionamos o estado inicial ao estados visitados


        while estados != []:
            estado = estados.pop()
            expansao = self.expande(estado)
            for e in expansao:
                if verifica_forapista(e) == 1:
                    self.g.add_edge(estado,e,25) ## Caso em que ele sai fora da pista fica com um custo de 25
                else:
                    self.g.add_edge(estado,e,1)
                if e not in visitados:
                    estados.append(e)
                    visitados.append(e)




def main():
    print_matrix()
    m = converte_matrix()
    xd = retorna_coords_posicao(m,'P')
    print(xd)
    ola = converter(xd)
    ola2 = teste(xd)
    print(ola2)

if __name__ == "__main__":
    main()