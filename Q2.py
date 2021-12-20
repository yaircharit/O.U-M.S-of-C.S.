import seagull as sg
from seagull.lifeforms import Custom
import random
import matplotlib.pyplot as plt



# board = sg.Board(size=(__board_size,__board_size))

def create_random_life():
        res = []
        for i in range(CellAuto.starter_size):
            res.append([])
            for j in range(CellAuto.starter_size):
                res[i].append(random.randint(0,1))
        return res

class CellAuto:
    __count = 0
    board_size = 200
    starter_size = 5
    iterations_number = 1000
    def __init__(self):
        self.__starter = create_random_life()
        self.__size = sum([sum (line) for line in self.__starter])
        self.__time = 1
        self.__status = 'alive' if self.__size > 0 else 'dead'  # alive, dead, looper
        
        self.board = sg.Board((CellAuto.board_size,CellAuto.board_size))
        self.board.add(Custom(self.__starter), loc=(CellAuto.board_size//2,CellAuto.board_size//2))
        
        CellAuto.__count += 1
        self.__id = CellAuto.__count
        self.sim = sg.Simulator(self.board)
        
        # You can also get it using get_history()
        # self.hist = self.sim.get_history()
        # self.stats = self.sim.compute_statistics(self.hist)
        # self.__f = self.fitness()
        
    def fitness(self):
        return self.stats.peak_cell_covarage
    
    def run(self):
        for i in range(CellAuto.iterations_number):
            self.sim.run(sg.rules.conway_classic, iters=1)
            print(len(self.sim.get_history()))
        anim = self.sim.animate()
        plt.show()
        
    def __str__(self):
        return f'CellAuto #{self.__id} is {self.__status}: time={self.__time}\n{self.__starter}'

# class Genetics:
#     sim 
            
# board.add(Custom([[0,1,1,0], [0,0,1,1]]), loc=(0,0))
c= CellAuto()
print(c)
c.run()