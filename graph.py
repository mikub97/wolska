import itertools
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph(object):

    ## do poprawy
    def __init__wrong(self,n=10,p=0.7):
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

    def __init__(self,n=10,p=0.7):
        self.vertices_no=n
        self.vertices = list(range(n))
        self.graph = []
        for i in range(n):
            row = list(np.ones(n-i,dtype=int))
            s = random.sample(list(range(1,n-i)),int((n-i)*p))
            for j in s:
                row[j]=0
            for j in range(i):
                row.insert(0,0)
            self.graph.append(row)
        print(np.matrix(self.graph))
        for i in range(n):
            for j in range(i):
                self.graph[i][j] = self.graph[j][i]
        print(np.matrix(self.graph))

    def show_graph(self):
        rows, cols = np.where(np.matrix(self.graph) == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        all_rows = range(0, np.matrix(self.graph).shape[0])
        for n in all_rows:
            gr.add_node(n)
        gr.add_edges_from(edges)
        nx.draw(gr, node_size=900, with_labels=True)
        plt.show()

    # function determines the neighbors of a given vertex
    def N(self,vertex):
        c = 0
        l = []
        for i in self.graph[vertex]:
            if i == 1:
                l.append(c)
            c += 1
        return l

#the Bron-Kerbosch recursive algorithm
# not working yet
def bronk(g, r,p,x):
    if len(p) == 0 and len(x) == 0:
        print(r)
        return
    for vertex in p[:]:
        r_new = r[::]
        r_new.append(vertex)
        p_new = [val for val in p if val in g.N(vertex)] # p intersects N(vertex)
        x_new = [val for val in x if val in g.N(vertex)] # x intersects N(vertex)
        bronk(g,r_new,p_new,x_new)
        p.remove(vertex)
        x.append(vertex)

g = Graph(n=5,p=0)

print("n(4)= ",g.N(4))
g.show_graph()