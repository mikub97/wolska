import itertools
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph(object):

    ## do poprawy
    def __init__(self,n=10,p=0.7):
        self.vertices_no = n
        self.vertices = list(range(n))
        self.graph = np.ones((n, n), dtype=int)
        print("Full graph with ", n, "nodes and ", n*n, "edges created")
        s = list(itertools.product(self.vertices,self.vertices))
        #deleting diagonal
        for i in range(n):
            s.remove((i,i))
        cutted_s = random.sample(s, int(len(s)*p))
        for e in cutted_s:
            self.graph[e[0]][e[1]]=0
        print("Removing ",p*100,"% edges from the graph")
        print("Graph has ",np.sum(self.graph)-n, "edges (without the diagonal)")
        print(self.graph)


    def show_graph(self):
        rows, cols = np.where(self.graph == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        all_rows = range(0, self.graph.shape[0])
        for n in all_rows:
            gr.add_node(n)
        gr.add_edges_from(edges)
        nx.draw(gr, node_size=900)#, labels=mylabels, with_labels=True)
        plt.show()

g = Graph(n=20,p=0.9)
g.show_graph()