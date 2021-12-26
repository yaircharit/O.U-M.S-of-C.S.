from numpy.ma.core import array
import seagull as sg
from seagull.lifeforms import Custom
from seagull.utils.statistics import cell_coverage
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import animation
from math import ceil
from threading import Thread
from sys import argv


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
    __count = 0
    board_size = 200

    def __init__(self, starter, generation=0):
        self.starter = np.array(starter)
        self.board = None
        self.hist = []
        self.coverage = 0
        self.status = 'alive'
        self.time = 0
        self.peak_coverage = (0,0)
        self.fitness = 0
        self.generation = generation
        CAAnalyzer.__count += 1
        self.id = CAAnalyzer.__count

    def run(self, iters=500):
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
                count_down -= 1
                if count_down == 0:
                    break
            self.current = sg.rules.conway_classic(self.current)

        self.fitness = self.peak_coverage[0]* self.time*10
        if self.status == 'alive':
            self.update_status(True)
        return self.status

    def update_status(self,looper_check=50, looper_check_unlimited=False):
        if looper_check_unlimited :
            looper_check = self.time 
        if any((compare_matrices(self.current, b) for b in self.hist[-(looper_check+1):-1])):
            self.status = 'looper'
        else:
            # alive, dead, looper
            self.status = 'alive' if self.coverage > 0 else 'dead'

    def set_simulator(self):
        self.board = sg.Board((CAAnalyzer.board_size, CAAnalyzer.board_size))
        self.board.add(Custom(self.starter), loc=(
            (CAAnalyzer.board_size//2, CAAnalyzer.board_size//2)))
        self.sim = sg.Simulator(self.board)
        self.current = self.board.state

    def mutate(self):
        i, j = np.random.randint(self.starter.shape[0]), np.random.randint(self.starter.shape[0])
        new_starter = np.array(self.starter)
        new_starter[i][j] = not self.starter[i][j]
        return new_starter

    def animate(self):
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
        
        # plt.show()

    def save_animation(self,folder='figures'):
        anim = self.animate()
        anim.save(f'{folder}/gen {self.generation}- {round(self.fitness,6)}.gif',writer=animation.PillowWriter(fps=10))
        plt.close()
        print(f"{folder}/gen {self.generation}- {round(self.fitness,6)}.gif Saved successfuly")
    
    def __str__(self):
        return f'[CellularAutomaton]\t#{self.id}\t{self.status}\t{self.time}\t{round(self.fitness,5)}'


class Genetics:

    def __init__(self, population_size=100):
        self.pop_size = population_size
        self.generations = 1
        self.__fitness_sum = 0
        self.__best_fitness = []
        pop = []
        for i in range(self.pop_size):
            new_starter = Genetics.create_random_life()
            while any([compare_matrices(new_starter,starter) for starter in pop]):
                new_starter = Genetics.create_random_life()
            pop.append(new_starter)
        self.pop = [CAAnalyzer(starter,1) for starter in pop]
        self.best = []

    @staticmethod
    def create_random_life(start_size=(5, 5)):
        res = np.random.randint(2, size=start_size)
        return res

    def process_generation(self, max_iterations=10000, iterations_batch_size=500):
        self.__fitness_sum = 0
        thrds = []
        for CA in self.pop:
            print(f'CA #{CA.id} running:')
            while CA.time < max_iterations and  CA.status == 'alive':
                CA.run(iterations_batch_size)
                print(f'\t- {CA.time}\tfit= {round(CA.fitness,2)}')
            CA.fitness /= max_iterations
            self.__fitness_sum += CA.fitness
        self.pop.sort(reverse=True, key=lambda ca: ca.fitness)
        self.__best_fitness.append(self.pop[0].fitness)
        self.best.append(self.pop[0])
        self.best.sort(key= lambda ca: ca.fitness, reverse=True)
        if self.best[0].generation != self.generations:
            self.__fitness_sum += self.best[0].fitness

    def set_new_generation(self):
        pop_prec = [round(CA.fitness/self.__fitness_sum*self.pop_size)
                    for CA in self.pop]
        
        new_pop = []
        pop_starters = [self.best[0].starter]+[ CA.starter for CA in self.pop]
        if self.generations != self.best[0].generation:
            for i in range(round(self.best[0].fitness/self.__fitness_sum*self.pop_size)):
                new_starter = self.best[0].mutate()
                while any([compare_matrices(new_starter,starter) for starter in pop_starters]):
                    new_starter = self.best[0].mutate()
                new_pop.append(new_starter)
        for i in range(len(pop_prec)):
            for j in range(pop_prec[i]):
                new_starter = self.pop[i].mutate()
                while any([compare_matrices(new_starter,starter) for starter in pop_starters]):
                    new_starter = self.pop[i].mutate()
                new_pop.append(new_starter)
        while len(new_pop) < self.pop_size:
            new_starter = Genetics.create_random_life()
            while any([compare_matrices(new_starter,starter) for starter in pop_starters]):
                new_starter = Genetics.create_random_life()
            new_pop.append(new_starter)
            
        self.pop_size = len(new_pop)
        self.pop = [ CAAnalyzer(starter, self.generations) for starter in new_pop]

    
    def run(self, max_generations=10, improvement_deadline=5, **kwargs):
        count = max_generations
        count_down = improvement_deadline
        res = ''
        out_file = open('./out.txt', 'a')
        # out_file.write(f'max iterations: {kwargs['max_iterations']}')
        while count:
            self.process_generation(**kwargs)
            print(self)
            out_file.write(f'{str(self)}\n')
            if any([self.pop[0].fitness <= best for best in self.__best_fitness[-improvement_deadline-1:-1]]):
                count_down -= 1
                if count_down == 0:
                    break
            else:
                count_down = improvement_deadline

            self.set_new_generation()
            count -= 1
        if not count:
            self.generations -= 1
        out_file.close()
        print('Saving best results, please wait for process to finish')
        self.best.sort(key= lambda ca: ca.fitness, reverse=True)
        self.best[0].save_animation() 
        plt.bar([*range(1,self.generations+1)],self.__best_fitness)
        plt.ylabel('Max Fitness')
        plt.xlabel('Genertation')
        plt.show()
        plt.close()

    def __str__(self):
        res = f'\n[Genetics]\tpop_size: {self.pop_size}\tGeneration {self.generations}\n\nPopulation:\t\tID\tStatus\tTime\tFitness Score\tFitness Score %'

        for CA in self.pop:
            res = f'{res}\n{CA}\t\t{round(CA.fitness/self.__fitness_sum*100,4)}%'
        return res
    
if __name__ == '__main__':
    pop_size = 100
    iters = 2000
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
    g = Genetics(pop_size)
    g.run(30, max_iterations=iters, iterations_batch_size=500)
