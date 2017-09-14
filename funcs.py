# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:06:04 2017

@author: José
"""
# Nd = Number of Dimensions

if __name__ == '__main__': 
#import math
    import numpy
    
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*3
    D=len(x)
    def ackley_Nd(*x):

       sum1=0
       sum2=0
       for d in range(len(x)):
          sum1 = sum1 + x[d]**2
          sum2 = sum2 + numpy.cos(2 * numpy.pi * x[d])
                
        
          ack=20 + numpy.e - 20 * numpy.exp(-.2 * (1/D * sum1) ** .5) - numpy.exp(1/D * (sum2))  
        
       return ack
    
    
    def rastrigin_Nd(*x):

       sum1=0
       sum2=0
       for d in range(len(x)):
          sum1 = sum1 + x[d]**2
          sum2 = sum2 - numpy.cos(2 * numpy.pi * x[d])
                
        
          rast=10*D + sum1 + 10 * sum2  
        
       return rast
    
    
    def rosenbrock_Nd(*x):
       sum1=0
       sum2=0
       for d in range(len(x)-1):
          sum1 = sum1 + (x[d+1]-x[d]**2)**2
          sum2 = sum2 + (x[d]-1)**2
                
        
          rosen=100*sum1 + sum2  
        
       return rosen
        
    def exp_Nd(*x):
       sum1=0
       for d in range(len(x)):
          sum1 = sum1 + (x[d])**2
                
        
          exp_Nd=-numpy.exp(-.5*sum1) + 1  
        
       return exp_Nd 
        
    def ellipsoidal_Nd(*x):
       ellip=0 
       for d in range(len(x)):
          ellip = ellip + (x[d]-(d+1))**2
    
    
       return ellip
   
    
    rast = rastrigin_Nd(*x)
    ack = ackley_Nd(*x)
    rosen = rosenbrock_Nd(*x)
    expo = exp_Nd(*x)
    ellip = ellipsoidal_Nd(*x)