import random
import itertools

from networkx import connected_components, Graph

from graph_utils import *
import numpy as np

class GeneticAlgorithm():

    n_iter= 100;
    POP_SIZE = 50 ;
    P_MUT = 0.2 ;

    def __init__(self,graph): #initialization of algorithm
        self.graph = graph
        self.vert_n = len(graph.nodes)
        self.population = []
        self.population2= []
        self.best = (-1,- float("inf"),[],[]) # generation, value(aim),nodes in clique,genotype

    # Generowanie LOSOWEJ POPULACJI
    # można rozważyć inne opcje, np.
    # subgrafy
    def random_population_init(self):
        population = []
        for i in range(self.POP_SIZE):
            population.append(list(np.random.randint(2, size=self.vert_n)))
        return population


    ## to do with greedy algorithm
    # def not_random_population_init(self):
    #     population = []
    #     comp =connected_components(self.graph)
    #     for c in comp:
    #         print(c)

    # Jak na ten moment funkcja celu jest banalna i... chyba nie dokońca dobrze napisana.
    # Jest to punkty krytyczny
    # Teraz, sprawdzam połączenia pomiędzy każdym z węzłów potencalnego rozwiązania,
    # jeśli dane połączenie (Edge w graphie) istnieje dodaje 100 "punktów", jeśli nie istnieje
    # odejmuje.
    #               TO DO !!!
    #[0,1,2,3,4,5,6,7,8,9], [0, 0, 0, 1, 0, 1, 1, 1, 0, 0] -- > [3,5,6,7]
    # def aim(self,genotype):
        # result = 0.0
        # nodes = self.genotype_to_nodes(genotype)
        # comb = list(itertools.combinations(nodes,2))
        # for c in comb:
        #     if (g.has_edge(c[0],c[1])):
        #         result+=100
        #     # else:
        #     #     result-=100
        # return result




    # ewaluacja populacji, zwracana jest tablica ocen - wart. funkcji celu, dla każdego z osobnika
    # indeksy zwróconej tablicy res, odpowiadają indeksom odpowiednich osobników w populacji
    # dodatkowo zwracany jest indeks najlepszego osobnika w danej populacji oraz jego wartość celu
    def evaluate(self,population,iter):
        res = []
        i = 0
        was_best_changed= False
        for g in population:
            # AIM < -- FUNKCJA CELU
            extracted_clique = list(self.clique_extraction(g).nodes)
            res.append(len(extracted_clique))
            if len(extracted_clique)>self.best[1]:      #self.best[generation, value(aim),nodes in clique,genotype]
                self.best = [iter,len(extracted_clique),extracted_clique,g]
                was_best_changed=True
        if was_best_changed:
            self.report_best()
        return res;

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
        eval_res = self.evaluate(self.population,0)
        for t in range(self.n_iter):
            self.population2 = self.select(self.population,eval_res)
            self.population2 = self.mutate(self.population2)
            eval_res = self.evaluate(self.population2,t+1)
            self.population = self.population2

    # Funkcja, która zwraca liste node'ów należących do danego rozwiązania
    def genotype_to_nodes(self, genotype):
        nodes = []
        for i in range(len(genotype)):
            if genotype[i] == 1:
                nodes.append(i)
        return nodes

    def genotype_to_graph(self,genotype):
        g = Graph()
        nodes = self.genotype_to_nodes(genotype)
        g.add_nodes_from(nodes)
        for e in list(itertools.combinations(nodes,2)):
            if self.graph.has_edge(e[0],e[1]):
                g.add_edge(e[0],e[1])
        return g

    # reports current best
    def report_best(self):
        print("------------------------ ITERATION NR. ",self.best[0]," ---------------------------")
        print(" [generation , value (aim) ,  nodes_in_clique , genotype] - > ",self.best)
        draw(g,"best from iteration "+str(self.best[0]),self.best[2])


    def clique_extraction(self,genotype):
        g = self.genotype_to_graph(genotype)
        while (not is_clique(g)):
            smallest_degree_nodes = find_smallest_degree_nodes(g)
            g.remove_node(smallest_degree_nodes[(random.randint(0, len(smallest_degree_nodes)-1))][0]);
        return g


if __name__ == '__main__':
    random.seed(3)
    n=100     # ilość węzłów
    p= 0.4    # ile chcesz zostawić krawędzi
    g = generateGraph(n,p)
    ag = GeneticAlgorithm(g)
    ag.start()
    report_real_max_clique(g)

