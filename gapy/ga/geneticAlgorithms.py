'''
===========================================================================================
    ALGORITMO GENETICO BASICO - geneticAlgorithms.py
===========================================================================================
Universidade Federal do Para - UFPA
Trabalho de Computacao Evolucionaria
Docente: Prof. Dr. Roberto Celio Limao de Oliveira
===========================================================================================
'''

# AQUI EH IMPLEMENTADA A CLASSE DO AG



import cv2
import random as rd
import numpy as np
from gapy.ga import routines        # Importa classe com rotinas principais
import matplotlib
import matplotlib.pyplot as plt

class GeneticAlgorithms:
    
    def __init__ (self, nvar, lvar, ngenerations, nNgenerations, populationSize, ls, li, tc = 0.7, tm = 0.008):
    
        self.nvar = nvar                        # Numero de variaveis
        self.lvar = lvar                        # Tamanho de cada variaveis
        self.ngenerations = ngenerations         # Numero de geracoes
        self.generations = []
        self.nNgenerations = nNgenerations        # Numero vezes que o AG ira rodar
        self.populationSize = populationSize    # Tamanho da populacao
        self.tc = tc                            # Taxa de cruzamento
        self.tm = tm                             # Taxa de mutacao
        self.max = []                            # Maximo
        self.min = []                            # Minimo    
        self.mean = []                            # Media
        self.ls = ls                            # Limite superior
        self.li = li                             # Limite inferior
        self.var = 0

    def run (self):        
        n = 0

        while n < self.nNgenerations: 
            print "# Generation:", n
            # Criando as geracoes
            self.generations += [routines.newGeneration(self.nvar, self.lvar, self.populationSize, self.ls, self.li)]
            m = 1
            while m < self.ngenerations:
                # Rotinas de Crossover e Mutacao
                 self.generations += [routines.crossingOnePoint (self.nvar, self.lvar, self.tc, self.generations[-1], self.ls, self.li)]
                 self.generations[-1] = routines.mutation(self.generations[-1], self.tm)
                 m += 1
            n += 1

#            self.var = [input ('Digite 1 para continuar: ')]

        maximum = []
        minimum = []
        mean = []

        for i in range (0,len(self.generations), self.ngenerations):
            for j in range (i, i+self.ngenerations):
                maximum += [float(max(map(lambda x: x.fitness, self.generations[j])))]
                minimum += [float(min(map(lambda x: x.fitness, self.generations[j])))]
                mean += [float(sum(map(lambda x: x.fitness/self.populationSize, self.generations[j])))]
            self.max += [maximum]
            self.min += [minimum]
            self.mean += [mean]
            maximum = []
            minimum = []
            mean = []

    def plotting (self):
        # Plotagem dos graficos

        keys = range(self.ngenerations)

        for i in range (0, self.nNgenerations):
            plt.figure()
            plt.plot(keys, self.max[i], 'o', label = 'Maximo', color = 'blue')
            plt.plot(keys, self.min[i], '*', label = 'Minimo', color = 'green')
            plt.plot(keys, self.mean[i], '+', label = 'Media', color = 'red')
            plt.title('Performance')
            plt.xlabel('Geracao')
            plt.ylabel('Fitness')
            plt.legend()
            plt.grid()
        plt.show()
