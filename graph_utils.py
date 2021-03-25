import random

import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl


# p jaki ułamek krawędzi chcę zachować
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

def find_smallest_degree_nodes(g):
    s = sorted(list(g.degree()), key=lambda tup: tup[1])
    if len(s)==0:
        return None
    #all vertices with the smallest and second smallest degree
    small_degree_nodes = []
    small_degree_nodes.append(s[0])
    small= s[0][1]
    third_small_flag = False
    for i in s[1:]:
        if i[1]==small:
            small_degree_nodes.append(i)
        elif third_small_flag:
            return small_degree_nodes
        else:
            small_degree_nodes.append(i)
            small =i[1]
            third_small_flag = True

    return small_degree_nodes

def is_clique(g):
    degree = len(g.nodes)-1
    for d in g.degree():
        if d[1]<degree:
            return False
    return True

def max_clique(g):
    cliques = list(cl.enumerate_all_cliques(g))
    print("These are cliques in the graph:")
    #one of the biggest
    max_clique_graph = g.subgraph(nodes=cliques[-1])
    return max_clique_graph

def draw(g,title="",nodes_with_different_col = None):
    plt.figure(figsize=(10,5))
    ax = plt.gca()
    ax.set_title(title)
    if nodes_with_different_col == None:
        nx.draw(g, node_size=900, with_labels=True,ax=ax)
    else:
        colors = []
        for node in g.nodes:
            if node in nodes_with_different_col:
                colors.append('yellow')
            else:
                colors.append('pink')
        nx.draw(g, node_size=900, node_color=colors,with_labels=True,ax=ax)

    plt.show()

def report_real_max_clique(g):
    print("------------------------ BEST CLIQUE BY NETWORX ALG. "," ---------------------------")
    clique = max_clique(g)
    print("With nodes in clique= ", list(clique.nodes))
    draw(g, "BEST CLIQUE BY NETWORX ALG.",list(clique.nodes))


if __name__ == '__main__':
    random.seed(3)
    g = generateGraph(10,0.7)
    report_real_max_clique(g)


