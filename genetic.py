import random
import itertools
from graph_utils import *
import numpy as np


n = 99
p=0.4
n_iter = 10;

class GeneticAlgorithm():

    POP_SIZE = 100;
    P_MUT = 0.1
    P_CROSS = 0.2


    def __init__(self,graph): #initialization of algorithm
        self.graph = graph
        self.vert_n = len(graph.nodes)
        self.population = []
        self.population2= []
        self.best = []

    def random_population_init(self):
        population = []
        for i in range(self.POP_SIZE):
            population.append(list(np.random.randint(2, size=self.vert_n)))
        return population


    def draw_graph(self):
        nx.draw(self.graph,node_size=900, with_labels=True)
        plt.show()


    # TO DO best, select, mutate, evaluate
    def start(self):
        self.population = self.random_population_init()
        eval_res = self.evaluate(self.population)
        for t in range(n_iter):
            self.population2 = self.select(self.population,eval_res)
            self.population2 = self.mutate(self.population2)
            eval_res = self.evaluate(self.population2)








g = generateGraph(n,p)

ag = GeneticAlgorithm(g)
ag.draw_graph()
print('finito')

# t=0
# stop = False
# eval_result = evaluate(population)
# while(not stop):
#     select(eval_result,population)
#     cross()
#     mutate()
#     t+=1;
#     if t>20 or (False):     ## przemyśleć inne warunki stopu
#         stop = True
