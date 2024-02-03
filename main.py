from Dijkstra import shortest_path
import matplotlib.pyplot as plt
import networkx as nx

#? define graph
graph = {
    'v0':{'v1':8,'v4':1},
    'v1':{'v0':8,'v2':3,'v4':1},
    'v2':{'v1':3,'v3':5,'v4':4},
    'v3':{'v2':5,'v4':10},
    'v4':{'v0':1,'v1':1,'v2':4,'v3':10}
}

#? Visualize the gragh
G = nx.DiGraph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, k=0.7)
edge_labels = {(i, j): w["weight"] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
nx.draw_networkx(G, pos, with_labels=True, alpha=0.5)

#? Create a list of all vertices
vertices = ['v' + str(i) for i in range(0, G.number_of_nodes())]

#? Iterate over all pairs of vertices
for start in vertices:
    for end in vertices:
        #? Skip if start and end are the same
        if start == end:
          cost, path = '-','-'
        else:
          cost, path = shortest_path(graph, start, end)
        print(f"{start} to {end} : {cost}, {path}")

plt.axis("off")
plt.show()
