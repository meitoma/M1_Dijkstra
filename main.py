from Dijkstra import shortest_path
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#? Visualize the gragh
def visualize(mins,path):
    node_value=mins
    node_name={f'v{i}':f'v{i}' for i in range(0,len(node_value))}
    node_color={'v'+str(i): 'r' if 'v'+str(i) in path else 'b' for i in range(0,len(node_value)) }

    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_node(node,color=node_color[node])
            G.add_edge(node, neighbor, weight=weight)

    pos={'v0': np.array([-0.98478449, -0.72021842]), 
        'v1': np.array([-0.71819667, -0.07275903]), 
        'v2': np.array([0.18478262, 0.5568943 ]), 
        'v3': np.array([1.        , 0.35508905]),
        'v4': np.array([ 0.51819854, -0.11900592])} # ラベルの座標を手動で指定
        
    label_margin=0.13
    label_pos = {'v0': pos['v0'] - np.array([label_margin,0]), 
                'v1': pos['v1'] - np.array([label_margin,0]), 
                'v2': pos['v2'] - np.array([label_margin,0]), 
                'v3': pos['v3'] + np.array([label_margin,0]), 
                'v4': pos['v4'] + np.array([label_margin,0])}  # ラベルの座標を手動で指定


    edge_labels = {(i, j): w["weight"] for i, j, w in G.edges(data=True)}
    node_colors=nx.get_node_attributes(G, 'color')

    nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()))
    nx.draw_networkx_labels(G, label_pos, labels=node_name)
    nx.draw_networkx_labels(G, pos, labels=node_value, font_color='white')

    nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos)

    plt.axis("off")
    plt.show()

#? define graph
graph = {
    'v0':{'v1':8,'v4':1},
    'v1':{'v0':8,'v2':3,'v4':1},
    'v2':{'v1':3,'v3':5,'v4':4},
    'v3':{'v2':5,'v4':10},
    'v4':{'v0':1,'v1':1,'v2':4,'v3':10}
}

#? Create a list of all vertices
vertices = ['v' + str(i) for i in range(0,len(graph))]

#? Iterate over all pairs of vertices
# start=v3,end=v0の例
for start in vertices:
    if start!="v3":continue
    for end in vertices:
        if end!="v0":continue
        #? Skip if start and end are the same
        if start == end:
            cost, path = '-','-'
        else:
            cost, path, mins = shortest_path(graph, start, end)
            visualize(mins,path)

        print(f"{start} to {end} : {cost}, {path}")

