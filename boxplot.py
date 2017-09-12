#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:06:23 2017

@author: luan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

name1 = 'DE_final_pop.csv';
name2 = 'FSADE_final_pop.csv';

columns = [];

n_param = 6

temp1 = pd.read_csv(name1, sep='\t', usecols=range(n_param))
temp2 = pd.read_csv(name2, sep='\t', usecols=range(n_param))


data = [temp1['output'],temp2['output']]

## don't show outlier points
#plt.figure()
#plt.xticks(range(2), ['DE', 'FSADE'])
#plt.boxplot(data, 0, '')

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data)

## Custom x-axis and y-axis labels
ax.set_xticklabels(['DE','FSADE'])
ax.set_ylabel('Average Function Evaluation')

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')