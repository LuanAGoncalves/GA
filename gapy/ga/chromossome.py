'''
===========================================================================================
	ALGORITMO GENETICO BASICO - chromossome.py
===========================================================================================
Universidade Federal do Para - UFPA
Trabalho de Computacao Evolucionaria
Docente: Prof. Dr. Roberto Celio Limao de Oliveira
===========================================================================================
'''



import random as rd
from math import sin, sqrt
import numpy as np
from ..aux import aux
import routines

class Chromossome:
	'''
	Classe para criar o cromossomo e gerar seu fitness

	Funciona de duas formas:
		1. ch = chromossome.Chromossome(nvar, lvar)
			Usado para gerar cromossomos com uma sequencia aleatoria 
		
		2. ch = chromossome.Chromossome(nvar, lvar, sequence)
			Usado quando jah existe uma sequencia de cromossomos
			sequence => sequencia de cromossomos passada para a funcao
	'''

	def __init__(self, nvar, lvar, ls, li, sequence = None):
		self.nvar = nvar
		self.lvar = lvar
		self.ls = ls
		self.li = li
		if sequence == None:
			self.sequence = aux.randomSequence(self.lvar)
		else:
			self.sequence = sequence
		self.fitness = self.function()
		self.sl = [0,0]


	def function (self):
		# Funcao de avalicao do AG

		x,y = aux.bin2real(self.nvar, self.lvar, self.sequence, self.ls, self.li)

		print 'X= %r \t Y= %r \t' %(x,y)

		fitness = 0.5-((((sin(sqrt(x**2+y**2)))**2)-(0.5))/(((1)+(0.001)*((x**2+y**2)))**2));

		print 'F(X,Y): %r \t' %(fitness)

		return  fitness

		# return 0.5 + (sin((x**2)+(y**2))**2 - 0.5)/(1 + 0.001*sin((x**2)+(y**2))**2)

		
