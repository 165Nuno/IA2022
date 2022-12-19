
# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id, poderia ter também informação sobre um ob jeto a guardar.....
class Node:
    def __init__(self,name):     #  construtor do nodo....."
        self.m_name = name       # posição linha, velocidade x, velocidade y (tuplo de 4 elementos)
        
        # posicção coluna
        #self.ac_linha; # acelaração linha
        #self.ac_coluna; # acelaração coluna

   
    def __str__(self):
        return "node" + self.m_name

    def __repr__(self):
        return "node" + self.m_name

    def setName(self,name):
        self.m_name = name

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name # são iguais se nome igual, não usa o id

    def __hash__(self):
        return hash(self.m_name)
