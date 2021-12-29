import seagull as sg
from seagull.lifeforms import Custom
from seagull.utils.statistics import cell_coverage
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from sys import argv
from datetime import datetime
import os
from numpy.random import randint
from math import floor

def compare_matrices(a, b):
    """
    param a: boolean matrix
    param b: boolean matrix
    return: True if both matrices' contents are identical
    """
    if a is b:
        return False

    xor = np.logical_xor(a, b)
    return not xor.any()


class CAAnalyzer:
    """
    Cellular Automaton Analyzer
    given starter configuration- will calculate CA's lifespan and max board coverage
    """
    
    board_size = 200

    def __init__(self,id:int , starter:list, generation:int=0):
        """
        :param id:          CA id number
        :param starter:     boolean matrix
        :param generation:  CA generation
        """
        self.starter = np.array(starter)
        self.board = None
        self.hist = []
        self.coverage = 0
        self.status = 'alive'
        self.time = 0
        self.peak_coverage = (0,0)  #(coverage, time of coverage)
        self.fitness = 0
        self.generation = generation
        self.id = id

    def run(self, iters:int=500):
        """
        :param iters:   number of maximum iterations to run
        :return:        CA status after run (alive/dead/looper)
        :rtype:         str
        """
        if not self.board:
            self.set_simulator()
        count_down = 10  

        for i in range(iters):
            if self.status == 'alive':
                self.time += 1
                self.coverage = cell_coverage(self.current)
                if self.coverage > self.peak_coverage[0]:
                    self.peak_coverage = (self.coverage,self.time)
                self.hist.append(self.current)
                self.update_status()
            else:
                # Extend animation a bit after CA stabelizes
                count_down -= 1
                if count_down == 0:
                    break
            self.current = sg.rules.conway_classic(self.current) # update board
        self.current = self.hist[-1]
        self.fitness = self.peak_coverage[0]* self.time*10/max(iters,self.time)
        if self.status == 'alive':
            # Check for long loops
            self.update_status(self.time)
            
        return self.status

    def update_status(self,looper_check:int=50):
        """
        :param looper_check:    Number of iteration to check for a loop
        """
        if any((compare_matrices(self.current, b) for b in self.hist[-(looper_check+1):-1])):
            self.status = 'looper'
        else:
            # alive, dead, looper
            self.status = 'alive' if self.coverage > 0 else 'dead'

    def set_simulator(self):
        """
        initiates simulator, board and current variables
        """
        self.board = sg.Board((CAAnalyzer.board_size, CAAnalyzer.board_size))
        self.board.add(Custom(self.starter), loc=(
            (CAAnalyzer.board_size//2, CAAnalyzer.board_size//2)))
        self.sim = sg.Simulator(self.board)
        self.current = self.board.state

    def mutate(self):
        """
        Mutates one bit of the starter copy
        :return:    The mutated starter
        :rtype:     np.ndarray
        """
        i, j = randint(self.starter.shape[0]), randint(self.starter.shape[0])
        new_starter = np.array(self.starter)
        new_starter[i][j] = not self.starter[i][j]
        return new_starter

    def animate(self):
        """
        Generates an animation of the calculated iterations
        :return:    Animation
        """
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
        X_blank = np.zeros(self.board.size, dtype=bool)
        im = ax.imshow(X_blank, cmap=plt.cm.binary, interpolation="nearest")
        im.set_clim(-0.05, 1)
        fig.suptitle(f'Fitness: {self.fitness}, max_time: {self.time}')
        def _animate(i, history):
            self.current_pos = history[i]
            im.set_data(self.current_pos)
            return (im,)

        def _init():
            im.set_data(X_blank)
            return (im,)

        history = np.asarray(self.hist)
        return animation.FuncAnimation(
            fig,
            func=_animate,
            frames=range(history.shape[0]),
            init_func=_init,
            interval=50 if self.time <= 500 else 10,
            fargs=(history,),
            blit=True,
        )


    def save_animation(self,folder:str='figures'):
        """
        Saves CA's animation to given folder
        :param folder:      output path
        """
        anim = self.animate()
        anim.save(f'{folder}/gen {self.generation}- {round(self.fitness,6)}.gif',writer=animation.PillowWriter(fps=10))
        plt.close()
        print(f"{folder}/gen {self.generation}- {round(self.fitness,6)}.gif Saved successfuly")
    
    def __str__(self):
        return f'CellularAutomaton #{self.id}\t{self.status}\t{self.time}\t{round(self.fitness,5)}'

def counter(start:int=0,end:int=-1):
    i=start
    while start != end:
        i+=1
        yield i
        
class GeneticAlg:
    """
    Genetic Algorithm Class
    Run simulations on a random population, find best results and mutate them. REPEAT
    """
    def __init__(self, population_size:int=100):
        """
        :param population_size: Defines the population size of ALL generations
        """
        self.__count = counter()
        self.output_path = f'./outputs/{"-".join(str(datetime.now()).split(".")[0].split(":"))}'  #a unique folder as the output path
        self.pop_size = population_size
        self.generations = 1
        self.__fitness_sum = 0
        self.__best_fitness = []
        pop = []
        for i in range(self.pop_size):
            # generate random population
            GeneticAlg.generate_new_starter(pop,randint,2,size=(5,5))
        self.pop = [CAAnalyzer(next(self.__count),starter,1) for starter in pop]
        self.best = []

    def process_generation(self, max_iterations:int=2000):
        """
        :param max_iterations:      maximum iterations for each CA to run
        :return:    Description of the processed generation 
        :rtype:     str
        """
        self.__fitness_sum = 0
        res = ''
        for CA in self.pop:
            CA.run(max_iterations)
            print(f'\t{CA}')
            res += f'\t{CA}\n'
            self.__fitness_sum += CA.fitness
        self.pop.sort(reverse=True, key=lambda ca: ca.fitness)  # Sort by fitness
        self.__best_fitness.append(self.pop[0].fitness)
        self.best.append(self.pop[0])
        self.best.sort(key= lambda ca: ca.fitness, reverse=True) # Find the best of the best
        return res

    def set_new_generation(self):
        """
        Generates and sets a new population.
        Each new CA is mutated from the previous population (parents are picked by fitness precentage) 
        and each is different than its brothers
        """
        # Calculate perant precentages according to fitness
        pop_prec = [floor(CA.fitness/self.__fitness_sum*self.pop_size)
                    for CA in self.pop]
        new_pop = []
        for i in range(len(pop_prec)):
            for j in range(pop_prec[i]):
                # Generate population according to calculated precentages
                GeneticAlg.generate_new_starter(new_pop,self.pop[i].mutate)
                
        while len(new_pop) < self.pop_size:
            # Fill population to be exactly the set amount
            GeneticAlg.generate_new_starter(new_pop,randint,2,size=(5,5))

        self.generations += 1
        self.pop = [ CAAnalyzer(next(self.__count),starter, self.generations) for starter in new_pop[:self.pop_size]]
        
    @staticmethod
    def generate_new_starter(pop_list:list,gen_function,*args, **kwargs):
        """
        Generates and adds a unique starter to pop_list.
        :param pop_list:        A list of starters, the new starter will be unique in the list
        :param gen_function:    A function that generates a starter (i.e. randint or CA.mutate), passing args and kwargs to it
        """
        new_starter = gen_function(*args,**kwargs)
        while any([compare_matrices(new_starter,starter) for starter in pop_list]):
            new_starter = gen_function(*args,**kwargs)
        pop_list.append(new_starter)
        
    
    def run(self, max_generations=30, max_iterations=2000, local_min_range=5):
        """
        Runs the genetic algorithm for until max_generations reached or fitness score stabelizes (local minimum)
        Prints best result and all acquired data to ./output/<time of init>
        :param max_generations: Maximum generations for the algorithm to run
        :param max_iterations:  Maximum iterations for each CA to process
        :param local_min_range: Number of generations back to compare to, when lower or equal than x previous generations run shall stop
        """
        count = max_generations 
        os.mkdir(self.output_path) # Create unique folder as output folder
        with open(f'{self.output_path}/data.txt', 'w') as out_file:
            out_file.write(f'population size: {self.pop_size}\nmax iterations: {max_iterations}\n')
            while count:
                header = f'\t ----------------- Generation #{self.generations} -----------------'
                print(header)
                data = self.process_generation(max_iterations)
                apendg = f'\n[WINNER]{self.pop[0]}\t{floor(self.pop[0].fitness/self.__fitness_sum*self.pop_size)}\n[ BEST ]{self.best[0]}\tGen {self.best[0].generation}\n'
                print(apendg)
                
                if self.generations > local_min_range and all([self.__best_fitness[-1] <= best for best in self.__best_fitness[-local_min_range-1:-1]]):
                    #if local minimum
                    break
                
                out_file.write(f'{header}\n{data}\n{apendg}\n')

                self.set_new_generation()
                count -= 1
            out_file.close()
        if not count:
            self.generations -= 1
        
        
        print('Saving best results, please wait for process to finish')
        # Saving best result animation
        self.best.sort(key= lambda ca: ca.fitness, reverse=True)
        self.best[0].save_animation(self.output_path) 
        # Saving bar chart summery of the process
        X = [*range(1,self.generations+1)]
        plt.bar(X,self.__best_fitness)
        plt.ylabel('Max Fitness')
        plt.xlabel('Genertation')
        plt.savefig(f'{self.output_path}/summery.png')
        plt.close()

    def __str__(self):
        res = f'\n[GeneticAlg]\tpop_size: {self.pop_size}\tGeneration {self.generations}\n\nPopulation:\t\tID\tStatus\tTime\tFitness Score\tFitness Score %'

        for CA in self.pop:
            res = f'{res}\n{CA}\t\t{round(CA.fitness/self.__fitness_sum*100,4)}%'
        return res

def main(pop_size=100,iters=2000):
    g = GeneticAlg(pop_size)
    g.run(30, max_iterations=iters)

if __name__ == '__main__':
    pop_size=100
    iters=2000
    try:
        if len(argv) > 1:
            pop_size = int(argv[1])
            if pop_size < 1:
                raise Exception()
        if len(argv) > 2:
            iters = int(argv[2])
            if iters < 1:
                raise Exception()
    except:
        print('ERROR: population size must be a positive integer')
    for i in range(10):
        main(pop_size,iters)