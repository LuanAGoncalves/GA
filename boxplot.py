#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:06:23 2017

@author: luan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name1 = './GA_ultimate/ellipsoidal/DE_final_pop.csv';
name2 = './GA_ultimate/ellipsoidal/FSADE_final_pop.csv';

columns = [];

n_var = 30

n_param = n_var + 3;

temp1 = pd.read_csv(name1, sep='\t', usecols=range(n_param))
temp2 = pd.read_csv(name2, sep='\t', usecols=range(n_param))


data = [temp1['output'],temp2['output']]

data2 = [temp1['func_val'], temp2['func_val']];

## Create a figure instance
#fig1 = plt.figure(1, figsize=(9, 6))
#
## Create an axes instance
#ax1 = fig1.add_subplot(111)
#
## Create the boxplot
#bp1 = ax1.boxplot(data)
#
### Custom x-axis and y-axis labels
#ax1.set_xticklabels(['DE','FSADE'])
#ax1.set_ylabel('Mean Error')
#
## Save the figure
#fig1.savefig('fig1.png', bbox_inches='tight')

fig2 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax2 = fig2.add_subplot(111)

# Create the boxplot
bp2 = ax2.boxplot(data2)

## Custom x-axis and y-axis labels
ax2.set_xticklabels(['DE','FSADE'])
ax2.set_ylabel('Average Function Evaluation')

# Save the figure
fig2.savefig('./GA_ultimate/ellipsoidal/fig2.png', bbox_inches='tight')


# DE.
mean_DE = np.mean(temp1['output'])
sd_DE = np.std(temp1['output'])
afe_DE = np.mean(temp1['func_val'])
deNcriterion_found = np.sum(temp1['Ncriterion_found'])

print ("#### DE ####\n")
print ("AFE = "+ str(afe_DE)+ "\n")
print ("SD = "+ str(sd_DE)+ "\n")
print ("output_mean = "+ str(mean_DE)+ "\n")
print ("Criterion found = "+ str(deNcriterion_found)+ "\n")

#FSADE
mean_FSADE = np.mean(temp2['output'])
sd_FSADE = np.std(temp2['output'])
afe_FSADE = np.mean(temp1['func_val'])
fsadeNcriterion_found = np.sum(temp1['Ncriterion_found'])

print ("#### FSADE ####\n")
print ("AFE = "+ str(afe_FSADE)+ "\n")
print ("SD = "+ str(sd_FSADE)+ "\n")
print ("output_mean = "+ str(mean_FSADE)+ "\n")
print ("Criterion found = "+ str(fsadeNcriterion_found)+ "\n")