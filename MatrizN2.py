class Grafo:

     def __init__(self,vertices):
           self.vertices = vertices
           self.grafo = [[0]*self.vertices for i in range(self.vertices)]

     def add_aresta(self, u, v):
         self.grafo[u-1][v-1] = 1


     def imprime_matriz(self):
         print('MATRIZ DE ADJACÊNCIAS É:')
         for i in range(self.vertices):
             print(self.grafo[i])

G = Grafo(20)
G.add_aresta('1','2')
G.add_aresta('1','4')
G.add_aresta('1 ', '14')
G.add_aresta('1 ', '11')
G.add_aresta('2 ', '3 ')
G.add_aresta('2 ', '14 ')
G.add_aresta( '9 ', '10 ')
G.add_aresta( '9 ', '4 ' )
G.add_aresta( '9 ', '8 ' )
G.add_aresta( '5 ', '8 ' )
G.add_aresta( '8 ', '7 ' )
G.add_aresta( '7 ', '6 ' )
G.add_aresta( '6 ', '5 ' )
G.add_aresta( '6 ', '12 ' )
G.add_aresta( '5 ', '4 ' )
G.add_aresta( '5 ', '13 ' )
G.add_aresta( '4 ', '13 ' )
G.add_aresta( '14 ', '15 ' )
G.add_aresta( '13 ', '16 ' )
G.add_aresta( '12 ', '17 ' )
G.add_aresta( '15 ', '19 ' )
G.add_aresta( '19 ', '20 ' )
G.add_aresta( '15 ', '18 ' )
G.add_aresta( '16 ', '15 ' )
G.add_aresta( '16 ', '18 ' )
G.add_aresta( '17 ', '16 ' )
G.add_aresta( '18 ', '17 ' )

G.imprime_matriz()




