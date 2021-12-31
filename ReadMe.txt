This module contains 2 classes: CAAnalyzer and GeneticAlg

The CAAnalyzer will run and analyze a cellular automaton with a given starter.
Each CAAnalyzer has a fitness score (lifespan*peak_coverage) that helps determin weather this Cellular Automaton is a Metushelah

The GeneticAlg class generates a random population of starting configurations.
After processing the first generation the algorithm will generate mutations from the best fitting CAs and add them as well as some new and random CAs (to try and avoid a local maximum solution)
After a set amount of generations with no improving the best result found is saved to a unique folder.

CMD Variables:
    -p = population size for each generation
    -i = Maximum number of iterations to run on each CAAnalyzer
    -b = Board size of each CAAnalyzer
    -s = the size of the initial configuration of the CAAnalyzer
    -l = Limit of generations without improving fitness score

