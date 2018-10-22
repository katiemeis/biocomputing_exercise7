#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:59:43 2018

@author: Mac
"""
#Question 1 - print odd rows
import pandas as pd

data = pd.read_csv('iris.csv')

def oddRows(dataFrame):
    dfOdd=dataFrame[dataFrame.index % 2 != 0]
    print(dfOdd)
    
print(oddRows(data))
 
#Question 2 with functions
#Part 1: Return # observations for a species in the dataset

def numObs(pickSpecies):
    species=data[data['Species'] == pickSpecies]
    print('The number of the chosen species oberved is:')
    print(len(species.index))

print(numObs('setosa'))

#Part 2: Return a dataframe for flowers with Sepal.Width greater than a certain value

def largeSW(threshold):
    s_w = data[data['Sepal.Width'] > threshold]
    print(s_w)

print(largeSW(2.0))

#Part 3: Write the data for a given species to a comma delimited file with the name of the species    

def newCSV(pickSpecies):
    species=data[data['Species'] == pickSpecies]
    print(species)
    species.to_csv(pickSpecies + '.csv')
    
print(newCSV('virginica'))
    
