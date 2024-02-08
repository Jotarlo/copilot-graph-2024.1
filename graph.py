# Create the Node class with label, weight, and edges

class Node:
    def __init__(self, label):
        self.label = label
        self.edges = []

    def add_edge(self, node, weight):
        self.edges.append({'node': node
                            , 'weight': weight})

    def __str__(self):
        return f'Node {self.label}'

    def __repr__(self):
        return f'Node {self.label}'
    
# Create the Graph class with nodes
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, label):
        self.nodes.append(Node(label))

    def add_edge(self, node1, node2, weight):
        node1.add_edge(node2, weight)
        node2.add_edge(node1, weight)

    def __str__(self):
        return f'Graph with {len(self.nodes)} nodes'

    def __repr__(self):
        return f'Graph with {len(self.nodes)} nodes'
    
# Create the graph with 10 nodes
graph = Graph()
for i in range(10):
    graph.add_node(i)

# Add 30 edges to the graph with different weights
graph.add_edge(graph.nodes[0], graph.nodes[1], 1)
graph.add_edge(graph.nodes[0], graph.nodes[2], 2)
graph.add_edge(graph.nodes[1], graph.nodes[2], 3)
graph.add_edge(graph.nodes[1], graph.nodes[3], 4)
graph.add_edge(graph.nodes[2], graph.nodes[3], 5)
graph.add_edge(graph.nodes[3], graph.nodes[4], 6)
graph.add_edge(graph.nodes[4], graph.nodes[5], 7)
graph.add_edge(graph.nodes[5], graph.nodes[6], 8)
graph.add_edge(graph.nodes[6], graph.nodes[7], 9)
graph.add_edge(graph.nodes[7], graph.nodes[8], 10)
graph.add_edge(graph.nodes[8], graph.nodes[9], 11)
graph.add_edge(graph.nodes[9], graph.nodes[0], 12)
graph.add_edge(graph.nodes[0], graph.nodes[3], 13)
graph.add_edge(graph.nodes[1], graph.nodes[4], 14)
graph.add_edge(graph.nodes[2], graph.nodes[5], 15)
graph.add_edge(graph.nodes[3], graph.nodes[6], 16)
graph.add_edge(graph.nodes[4], graph.nodes[7], 17)
graph.add_edge(graph.nodes[5], graph.nodes[8], 18)
graph.add_edge(graph.nodes[6], graph.nodes[9], 19)
graph.add_edge(graph.nodes[7], graph.nodes[0], 20)
graph.add_edge(graph.nodes[8], graph.nodes[1], 21)
graph.add_edge(graph.nodes[9], graph.nodes[2], 22)
graph.add_edge(graph.nodes[0], graph.nodes[4], 23)
graph.add_edge(graph.nodes[1], graph.nodes[5], 24)
graph.add_edge(graph.nodes[2], graph.nodes[6], 25)
graph.add_edge(graph.nodes[3], graph.nodes[7], 26)
graph.add_edge(graph.nodes[4], graph.nodes[8], 27)
graph.add_edge(graph.nodes[5], graph.nodes[9], 28)
graph.add_edge(graph.nodes[6], graph.nodes[0], 29)
graph.add_edge(graph.nodes[7], graph.nodes[1], 30)
graph.add_edge(graph.nodes[8], graph.nodes[2], 31)
graph.add_edge(graph.nodes[9], graph.nodes[3], 32)

# Show the graph nodes and edges with weights in an image
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
for node in graph.nodes:
    G.add_node(node.label)
    for edge in node.edges:
        G.add_edge(node.label, edge['node'].label, weight=edge['weight'])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold', font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Show the graph nodes and edges with weights in a table
import pandas as pd
edges = []
for node in graph.nodes:
    for edge in node.edges:
        edges.append([node.label, edge['node'].label, edge['weight']])
df = pd.DataFrame(edges, columns=['Node1', 'Node2', 'Weight'])
print(df)

# show the best path from node 0 to node 9 using Dijkstra's algorithm in a recursive way
def dijkstra(graph, start, end, visited=[], distances={}, predecessors={}):
    if start == end:
        path = []
        pred = end
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        readable = path[0]
        for i in range(1, len(path)):
            readable = path[i] + ' -> ' + readable
        print(f'Shortest path: {readable}')
    else:
        if not visited:
            distances[start] = 0
        for neighbor in graph.nodes[start].edges:
            if neighbor['node'].label not in visited:
                new_distance = distances[start] + neighbor['weight']
                if new_distance < distances.get(neighbor['node'].label, float('inf')):
                    distances[neighbor['node'].label] = new_distance
                    predecessors[neighbor['node'].label] = start
        visited.append(start)
        unvisited = {}
        for k in distances:
            if k not in visited:
                unvisited[k] = distances[k]
        next_node = min(unvisited, key=unvisited.get)
        dijkstra(graph, next_node, end, visited, distances, predecessors)

dijkstra(graph, 0, 9)
