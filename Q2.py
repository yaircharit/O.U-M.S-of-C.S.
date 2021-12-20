from numpy.ma.core import array
import seagull as sg
from seagull.lifeforms import Custom
from seagull.utils.statistics import cell_coverage
import random
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand



# board = sg.Board(size=(__board_size,__board_size))

def create_random_life():
        res = rand.randint(2,size=(CellAuto.starter_size,CellAuto.starter_size))
        return res

def compare_matrices(a,b):
    if a is b:
        return False
    # print('\na: ', a)
    # print('\nb: ', b)
    xor = np.logical_xor(a, b)
    # print('\nxor', xor)
    # print('any xor:',xor.any(),'all xor:',xor.all())
    return not xor.any()
class CellAuto:
    __count = 0
    board_size =10
    starter_size = 5
    iterations_number = 100
    iterations_in_batch = 5
    def __init__(self):
        self.__starter = create_random_life()
        self.__size = sum([sum (line) for line in self.__starter])
        self.__time = 1
        self.__status = 'alive' if self.__size > 0 else 'dead'  # alive, dead, looper
        self.__fitness_list = list()
        self.board = sg.Board((CellAuto.board_size,CellAuto.board_size))
        self.board.add(Custom(self.__starter), loc=(CellAuto.board_size//2,CellAuto.board_size//2))
        self.hist = list(self.board.state)
        self.__coverage = self.__size / CellAuto.board_size
        CellAuto.__count += 1
        self.__id = CellAuto.__count
        self.sim = sg.Simulator(self.board)
        self.__fitness_list.append(self.__fitness__())
        # You can also get it using get_history()
        # self.hist = self.sim.get_history()
        # self.stats = self.sim.compute_statistics(self.hist)
        # self.__f = self.fitness()
        
    def fitness(self):
        res = sum(self.__fitness_list)/self.__time
        return res
    
    def __fitness__(self):
        return self.__coverage * self.__time
    
    def run(self):
        for i in range(CellAuto.iterations_number//CellAuto.iterations_in_batch):
            self.sim.run(sg.rules.conway_classic, iters=CellAuto.iterations_in_batch)
            self.hist = self.sim.get_history()
            self.current = self.hist[-1]
            self.__size = sum([sum(line) for line in self.current])
            self.__coverage = cell_coverage(self.current)
            if self.__status != 'looper':
                self.__status = 'alive' if self.__coverage > 0 else 'dead'  # alive, dead, looper
            self.__time += 1*CellAuto.iterations_in_batch
            if self.__status != 'alive':
                print(self)
                break
            print(self.__time, len(self.hist[:-1]))
            print([compare_matrices(self.current, b) if self.current is not b else None for b in self.hist[:-1]])
            if any((compare_matrices(self.current, b) for b in self.hist[:-1])):
                self.__status = 'looper'
            self.__fitness_list.append(self.__fitness__())
        print(self)
        anim = sg.Simulator(self.board)
        # iters = self.__time+10 if self.__status == 'dead' else self.__time
        anim.run(sg.rules.conway_classic, iters=self.__time+10 if self.__status == 'dead' else self.__time)
        anim = anim.animate()
        plt.show()
        
        
    def __str__(self):
        return f'\n\nCellAuto #{self.__id} is {self.__status}: f={self.__fitness__()} time={self.__time}, f_total={self.fitness()}\n\n'

# class Genetics:
#     sim 
            
# board.add(Custom([[0,1,1,0], [0,0,1,1]]), loc=(0,0))
c= CellAuto()
print(c)
c.run()
print(c)