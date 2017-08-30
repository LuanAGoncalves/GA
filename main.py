'''
===========================================================================================
    ALGORITMO GENETICO BASICO - main.py
===========================================================================================
Universidade Federal do Para - UFPA
Trabalho de Computacao Evolucionaria
Docente: Prof. Dr. Roberto Celio Limao de Oliveira
Aluno: Luan Assis Goncalves
===========================================================================================
'''

# FUNCAO PRINCIPAL QUE PASSA OS PRIMEIROS PARAMETROS AO AG, CHAMA A FUNCAO PARA INICIAR E 
# PARA PLOTAR

from gapy.ga import geneticAlgorithms
from gapy.ga import routines
import numpy as np

if __name__ == '__main__':
    x = geneticAlgorithms.GeneticAlgorithms(2, [23,23], 1000, 5, 50, -25, 25)
    x.run()
    x.plotting()
