import random

import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl


n  = 5
p = 0.4 # ile zostawić

def generateGraph(n,p):
    g = nx.Graph()

    for i in range(n):
        g.add_node(i)

    for i in range(n):
        for j in range(n):
            g.add_edge(i,j)
    e = random.sample(g.edges, int(len(g.edges)*p))
    g.clear_edges();
    g.add_edges_from(e)
    return g

def max_clique(g):
    cliques = cl.enumerate_all_cliques(g)
    print("These are cliques in the graph:")
    for x in cliques:
        print(x)
    #one of the biggest
    max_clique_graph = g.subgraph(nodes=x)
    return max_clique_graph


# g = generateGraph(n,p)
# nx.draw(g,node_size=900, with_labels=True)
# plt.show()
#
# g_max = max_clique(g)
# nx.draw(g_max,node_size=900, with_labels=True)
# plt.show()

