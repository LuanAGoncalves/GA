# -*- coding: utf-8 -*-
# TODO(alexis): add **tests** (and try unittest.mock.MagicMock at the same
# time).

import collections
import random
import funcs
import numpy as np


__all__ = ['DE']
Individual = collections.namedtuple('Individual', 'ind fit')


class DE(object):
    """This class implements differential evolution.

    This method is described by Storne and Price in a paper titled
    "Differential evolution-a simple and efficient heuristic for global
    optimization over continuous spaces".

    Variables names in the implementation (x, y, z, u, v, F, CR, NP) try to
    match their equivalents in the paper.
    """

    def __init__(self, min_real, x='rand', y=1, z='bin', *, F=.5, CR=.1):
        self.x = x
        self.y = y
        self.z = z
        self.F = F
        self.CR = CR
        self.func_val = 0
        self.criterion_found = 0
        self.min_real = min_real
    # TODO(alexis): add a fitness_aim param?
    # TODO(alexis): add a generic way to generate initial pop?
    def solve(self, NP, fitness, initial_population, iterations=2*pow(10,5)):
        current_generation = [Individual(ind, fitness(*ind)) for ind in
                              initial_population]

        for _ in range(int(iterations/NP)):
            trial_generation = []

            for ind in current_generation:
                self.func_val += 1
                v = self._mutate(current_generation)
                u = self._crossover(ind.ind, v)

                trial_generation.append(Individual(u, fitness(*u)))

            current_generation = self._selection(current_generation,
                                                 trial_generation)
            best_index = self._get_best_index(current_generation)
            if np.abs(function(*(current_generation[best_index].ind))-self.min_real) < error:
                self.criterion_found += 1
                break
            
        return current_generation[best_index].ind

    def _mutate(self, population):
        if self.x == 'rand':
            r1, *r = self._get_indices(self.y * 2 + 1, len(population))

        elif self.x == 'best':
            r1 = self._get_best_index(population)
            r = self._get_indices(self.y * 2, len(population), but=xr1)

        mutated = population[r1].ind[:]  # copy base vector
        dimension = len(mutated)
        difference = [0] * dimension

        for plus in r[:self.y]:
            for i in range(dimension):
                difference[i] += population[plus].ind[i]

        for minus in r[self.y:]:
            for i in range(dimension):
                difference[i] -= population[minus].ind[i]

        for i in range(dimension):
            mutated[i] += self.F * difference[i]

        return mutated

    def _crossover(self, x, v):
        # assume self.z == 'bin'

        u = x[:]
        i = random.randrange(len(x))  # NP

        for j, (a, b) in enumerate(zip(x, v)):
            if i == j or random.random() <= self.CR:
                u[j] = v[j]

        return u

    def _selection(self, current_generation, trial_generation):
        generation = []

        for a, b in zip(current_generation, trial_generation):
            if a.fit < b.fit:
                generation.append(a)
            else:
                generation.append(b)

        return generation

    def _get_indices(self, n, upto, but=None):
        candidates = list(range(upto))

        if but is not None:
            # yeah O(n) but random.sample cannot use a set
            candidates.remove(but)

        return random.sample(candidates, n)

    def _get_best_index(self, population):
        min_fitness = population[0].fit
        best = 0

        for i, x in enumerate(population):
            if x.fit < min_fitness:
                best = i

        return best

    def _set_x(self, x):
        if x not in ['rand', 'best']:
            raise ValueError("x should be either 'rand' or 'best'.")

        self._x = x

    def _set_y(self, y):
        if y < 1:
            raise ValueError('y should be > 0.')

        self._y = y

    def _set_z(self, z):
        if z != 'bin':
            raise ValueError("z should be 'bin'.")

        self._z = z

    def _set_F(self, F):
        if not 0 <= F <= 2:
            raise ValueError('F should belong to [0, 2].')

        self._F = F

    def _set_CR(self, CR):
        if not 0 <= CR <= 1:
            raise ValueError('CR should belong to [0, 1].')

        self._CR = CR

    x = property(lambda self: self._x, _set_x, doc='How to choose the vector '
                 'to be mutated.')
    y = property(lambda self: self._y, _set_y, doc='The number of difference '
                 'vectors used.')
    z = property(lambda self: self._z, _set_z, doc='Crossover scheme.')
    F = property(lambda self: self._F, _set_F, doc='Weight used during '
                                                   'mutation.')
    CR = property(lambda self: self._CR, _set_CR, doc='Weight used during '
                                                      'bin crossover.')


if __name__ == '__main__': 
    D=2
    NP = 50
    iterations = 2*pow(10,5)
    error = 1e-5
    function = funcs.branin_Nd
    bound11 = -5
    bound12 = 10
    bound21 = 0
    bound22 = 15
    min_real = 0.3979
    v_stat = []
    Ncriterion_found = []
    f=open("DE_final_pop.csv","w")
    for i in range (D):
        f.write('v['+str(i)+']'+'\t')
    f.write('Ncriterion_found'+'\t')
    f.write('output'+'\t'+'func_val'+'\n')
    
    for sim in range(100):
        print ("SIM = ", str(sim))
        de = DE(min_real)
        pop = [[random.uniform(bound11, bound12), random.uniform(-bound21, bound22) ]
               for _ in range(NP)]  # 20 * dimension of the problem
        v = de.solve(NP, function, pop, iterations) 
        v_stat.append(function(*v))
        Ncriterion_found.append(de.criterion_found)
#        for i in range(NFuncVal):
#            v = de.solve(function, pop, iterations) 
#            print(function(*v))
#            if function(*v) < error:
#                v_stat.append(function(*v))
#                break
#            if i == NFuncVal-1:
#                v_stat.append(function(*v))
    
        for i in range (len(v)):
            f.write(str(v[i])+'\t')
        f.write(str(Ncriterion_found[-1])+'\t')
        f.write(str(v_stat[sim])+'\t'+str(de.func_val)+'\n')
        
    f.close()   
