
# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id, poderia ter também informação sobre um ob jeto a guardar.....
class Node:
    def __init__(self,p_linha,p_coluna):     #  construtor do nodo....."
        self.p_linha = int(p_linha)# posição linha
        self.p_coluna = int(p_coluna)# posicção coluna
        #self.ac_linha; # acelaração linha
        #self.ac_coluna; # acelaração coluna

    def __str__(self):
        return "node x:" + self.p_linha + "node y:" + self.p_coluna

    def __repr__(self):
        return "node " + self.m_name

    def setLinha(self, linha):
        self.p_linha = linha

    def getLinha(self):
        return self.p_linha

    def setColuna(self,coluna):
        self.p_coluna = coluna

    def getColuna(self):
        return self.p_coluna

    def __eq__(self, other):
        return self.p_linha == other.p_linha and self.p_coluna == other.p_coluna   

    # ver isso
    def __hash__(self):
        return hash(self.m_name)