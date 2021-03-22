import random
import itertools
from graph import Graph
import numpy as np

n = 5

g = Graph(n=n)
POP_SIZE = 100;
P_MUT = 0.1
P_CROSS = 0.2
GENOME_SIZE = n # the number of nodes in the graph


#initialization of the population
population = []
for i in range(POP_SIZE):
    population.append(list(np.random.randint(2, size=n)))
print(population[0])

def evaluate(pop):
    evaluation = []
    i = 0
    for genome in population:
        indices = [i for i, x in enumerate(genome) if x == 1]
        permutations = list(itertools.product(indices,indices))
        result = aim()
        evaluation.append((i,result))
        i=i+1

## Main loop

t=0
stop = False
eval_result = evaluate(population)
while(not stop):
    select(eval_result,population)
    cross()
    mutate()
    t+=1;
    if t>20 or (False):     ## przemyśleć inne warunki stopu
        stop = True
