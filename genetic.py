import random
import itertools
from graph_utils import *
import numpy as np


n = 10
p=0.4
n_iter = 30;

class GeneticAlgorithm():

    POP_SIZE = 100;
    P_MUT = 0.15

    def __init__(self,graph): #initialization of algorithm
        self.graph = graph
        self.vert_n = len(graph.nodes)
        self.population = []
        self.population2= []
        self.best = (-1,-1,[]) # generation, value(aim), genotype

    # Generowanie LOSOWEJ POPULACJI
    # można rozważyć inne opcje, np.
    # subgrafy
    def random_population_init(self):
        population = []
        for i in range(self.POP_SIZE):
            population.append(list(np.random.randint(2, size=self.vert_n)))
        return population

    # Jak na ten moment funkcja celu jest banalna i... chyba nie dokońca dobrze napisana.
    # Jest to punkty krytyczny
    # Teraz, sprawdzam połączenia pomiędzy każdym z węzłów potencalnego rozwiązania,
    # jeśli dane połączenie (Edge w graphie) istnieje dodaje 100 "punktów", jeśli nie istnieje
    # odejmuje.
    #                               TO DO !!!
    #[0,1,2,3,4,5,6,7,8,9], [0, 0, 0, 1, 0, 1, 1, 1, 0, 0] -- > [3,5,6,7]
    def aim(self,genotype):
        result = 0.0
        nodes = self.genotype_to_nodes(genotype)
        comb = list(itertools.combinations(nodes,2))
        for c in comb:
            if (g.has_edge(c[0],c[1])):
                result+=100
            # else:
            #     result-=100
        return result

    # ewaluacja populacji, zwracana jest tablica ocen - wart. funkcji celu, dla każdego z osobnika
    # indeksy zwróconej tablicy res, odpowiadają indeksom odpowiednich osobników w populacji
    # dodatkowo zwracany jest indeks najlepszego osobnika w danej populacji oraz jego wartość celu
    def evaluate(self,population):
        res = []
        best_aim = - float("inf")
        best_index = -1
        i = 0
        for g in population:
            aim = self.aim(g)
            if (aim>best_aim):
                best_aim = aim
                best_index=i
            res.append(self.aim(g))
            i=i+1
        return (best_index,best_aim,res);

    # Selekcja turniejowa turniej k - osobnikowy (k=2)
    def select(self,population, evaluation_results, k=2):
        pop2 = []
        for i in range(self.POP_SIZE):
            indexes = []
            results = []
            for j in range(k):
                ind = random.randint(0,self.POP_SIZE-1)
                indexes.append(ind)
                results.append(evaluation_results[ind])
            pop2.append(population[indexes[results.index(max(results))]])   # najlepszy z k wylosowanych idzie do nowej populacji
        return pop2


    # Mutacja z prawdopodobieństwem P_MUT
    def mutate(self,population):
        pop2 = []
        for g in population:
            if (random.random()<=self.P_MUT):
                mod_g = g
                pos = random.randint(0,len(mod_g)-1)
                if (mod_g[pos]==1):
                    mod_g[pos]=0
                else:
                    mod_g[pos]=1
                pop2.append(mod_g)
            else:
                pop2.append(g)
        return pop2

    # maksymalizujemy funkcje
    # TO DO sukcesja generacyjna ??
    def start(self):
        self.population = self.random_population_init()
        # 3 węzły w grafie i 3 osobnika w populacji
        (best_index,best_val, eval_res) = self.evaluate(self.population)

        for t in range(n_iter):
            if best_val > self.best[1]:
                self.best = (t, best_val, self.population[best_index])
            self.population2 = self.select(self.population,eval_res)
            self.population2 = self.mutate(self.population2)
            (best_index,best_val,eval_res) = self.evaluate(self.population2)
            self.population = self.population2


    # Funkcja, która zwraca liste node'ów należących do danego rozwiązania
    # [0, 0, 0, 1, 0, 1, 1, 1, 0, 0] -- > [3,5,6,7]
    def genotype_to_nodes(self, genotype):
        nodes = []
        for i in range(len(genotype)):
            if genotype[i] == 1:
                nodes.append(i)
        return nodes

    # rysuje graf, jeśli podano argument to ten z argumentu, jeśli nie podano to ten zdefiniowany w konstr.
    def draw_graph(self, g= None):
        if g !=None:
            nx.draw(g, node_size=900, with_labels=True)
        else:
            nx.draw(self.graph,node_size=900, with_labels=True)
        plt.show()



if __name__ == '__main__':
    g = generateGraph(n,p)
    ag = GeneticAlgorithm(g)
    # ag.draw_graph()
    ag.start()
    ag.draw_graph()
    print("alg. g. best - >",ag.best)
    print("best best.->",max_clique(g).nodes)
    nodes = ag.genotype_to_nodes(ag.best[2])
    sub = g.subgraph(nodes)
    ag.draw_graph(sub)


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
