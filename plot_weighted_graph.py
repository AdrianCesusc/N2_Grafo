#importamos a biblioteca Networkx para geração de grafos e tratamento de dados
##importamos a biblioteca matplotlib para geração do grafico viasual do grafo.
import matplotlib.pyplot as plt
import networkx as nx


#criamos o grafo seguindo o padrão da bibloteca 
G = nx.Graph()


#Criamos os vertices
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_node("G")
G.add_node("H")
G.add_node("I")
G.add_node("J")
G.add_node("K")
G.add_node("L")
G.add_node("M")
G.add_node("N")
G.add_node("O")
G.add_node("P")
G.add_node("Q")
G.add_node("R")
G.add_node("S")
G.add_node("T")


#criamos as arestas com seu peso
G.add_edge("A","B" , weight=3)
G.add_edge("A","D", weight=3)
G.add_edge("A","N", weight=3)
G.add_edge("A","K", weight=0.2)
G.add_edge("B","C", weight=0.8)
G.add_edge("B","N", weight=0.6)
G.add_edge("I","J", weight=0.1)
G.add_edge("I","D", weight=0.6)
G.add_edge("I","H", weight=3)
G.add_edge("E","H", weight=0.6)
G.add_edge("H","G", weight=1)
G.add_edge("G","F", weight=0.6)
G.add_edge("F","E", weight=1)
G.add_edge("F","L", weight=0.9)
G.add_edge("E","D", weight=3)
G.add_edge("E","M", weight=2)
G.add_edge("D","M", weight=3)
G.add_edge("N","O", weight=3)
G.add_edge("M","P", weight=3)
G.add_edge("L","Q", weight=2.8)
G.add_edge("O","S", weight=3)
G.add_edge("S","T", weight=3)
G.add_edge("O","R", weight=1)
G.add_edge("P","O", weight=3)
G.add_edge("P","R", weight=4)
G.add_edge("Q","P", weight=3)
G.add_edge("R","Q", weight=1)

#criamos duas variaveis uma com as menores arestas e uma com as maiores arestas 
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 1.5]

#definimos a posição de todos os vertices
pos = nx.spring_layout(G, seed=10) 

#Personalizamos o node
nx.draw_networkx_nodes(G, pos, node_size=700 )

#Personalizamos as arestas
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, edge_color="red")
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="green", style="dashed")

# Definimos a etiqueta dos vertices
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# Definimos a etiqueta dos vertices
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#Guardamos o numero de vertices e de arestas
n_vertices = G.number_of_nodes()
n_arestas = G.number_of_edges()

print("\nGrafo")
print('-Vertices: ', n_vertices, '\n-Arestas: ', n_arestas)

#Criamos as variveis de inicio e destino para busca do menor caminho
inicial = input("\nDigite a letra do ponto de partida\n")
destino = input("\nDigite a letra do ponto de chegada\n")

#Criamos a variavel cam_nos para salvar os vertices do menor caminho e utilizamos o mêtodo 'shortest' da biblioteca Networkx 
#para realizar este processo
cam_nos = nx.shortest_path(G,inicial,destino)
print("O menor caminho é seguindo as arestas",cam_nos)


#Imprimimos o grafo usando o padrão da biblioteca matplotlib
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
