from numpy.ma.core import array
import seagull as sg
from seagull.lifeforms import Custom
from seagull.utils.statistics import cell_coverage
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand
from matplotlib import animation


# board = sg.Board(size=(__board_size,__board_size))

def create_random_life():
        res = rand.randint(2,size=(RandomCellularAutomatonAnalyzer.starter_size,RandomCellularAutomatonAnalyzer.starter_size))
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
class RandomCellularAutomatonAnalyzer:
    __count = 0
    board_size =400
    starter_size = 5
    iterations_number = 100
    
    def __init__(self):
        self.starter = create_random_life()
        self.board = sg.Board((RandomCellularAutomatonAnalyzer.board_size,RandomCellularAutomatonAnalyzer.board_size))
        self.board.add(Custom(self.starter),loc=((RandomCellularAutomatonAnalyzer.board_size//2,RandomCellularAutomatonAnalyzer.board_size//2)))
        self.sim = sg.Simulator(self.board)
        self.current = self.board.state
        self.hist = []
        self.coverage_list = []
        self.status = 'alive'
        self.time = 0
        RandomCellularAutomatonAnalyzer.__count += 1
        self.id = RandomCellularAutomatonAnalyzer.__count
        
    def run(self, iters=iterations_number):
        count_down = 10
        for i in range(iters): 
            if self.status == 'alive':
                self.time += 1
                self.coverage_list.append(cell_coverage(self.current))
                self.hist.append(self.current)
                if any((compare_matrices(self.current, b) for b in self.hist[self.time-400:])):
                    self.status = 'a looper'
                else:
                    self.status = 'alive' if self.coverage_list[-1] > 0 else 'dead'  # alive, dead, looper     
            else:
                count_down -= 1     
                if count_down == 0:
                    break
            self.current = sg.rules.conway_classic(self.current)
        self.peak_coverage = max(self.coverage_list)    
        print(self)
        return self.status
        
    def fitness(self):
        res = sum(self.coverage_list)*self.time/RandomCellularAutomatonAnalyzer.iterations_number
        return res

    
    def animate(self):
        fig = plt.figure(figsize=(5,5))
        ax = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
        X_blank = np.zeros(self.board.size, dtype=bool)
        im = ax.imshow(X_blank, cmap=plt.cm.binary, interpolation="nearest")
        im.set_clim(-0.05, 1)

        def _animate(i, history):
            self.current_pos = history[i]
            im.set_data(self.current_pos)
            return (im,)

        def _init():
            im.set_data(X_blank)
            return (im,)

        history = np.asarray(self.hist)
        animation.FuncAnimation(
            fig,
            func=_animate,
            frames=range(history.shape[0]),
            init_func=_init,
            interval=100 if self.time <= 100 else 50,
            fargs=(history,),
            blit=True,
        )
        plt.show()
        
    def __str__(self):
        return f'\nRandomCellularAutomatonAnalyzer #{self.id} is {self.status}: time={self.time}, f_total={self.fitness()}\n\n'
max_iterations = 10000
c= RandomCellularAutomatonAnalyzer()
while c.status == 'alive' and c.time <= max_iterations: c.run()
c.animate()