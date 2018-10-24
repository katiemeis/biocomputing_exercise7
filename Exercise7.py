#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:50:35 2018

@author: stephaniearaki
"""
pwd
cd Desktop/biocomputing_exercise7

import pandas as pd
iris=pd.read_csv('iris.csv')

#Question 1
#write function that returns odd rows of any pandas dataframe
def oddnumbers(x):
        return [x[1: :2]] #skips every second row
oddnumbers(iris)

#Question 2
#get number of observations for given species in data
def speciescounter(data,column,speciesname):
    species=data[data[column]==speciesname]
    value=len(species)
    return [speciesname, value]
speciescounter (iris,'Species','setosa')
speciescounter (iris,'Species','versicolor')
    
#get dataframe for flowers with Sepal.Width greater than value specified by user
def sepalcounter(data,n):
        width=data.loc[data['Sepal.Width']>n]
        return [width]
sepalcounter(iris,4)
sepalcounter(iris,3)

#write data for a given species to .csv with species name as filename
def speciesdata(data,speciesname):
    file=data.loc[data['Species']==speciesname]
    file.to_csv(speciesname+'.csv')
    return file
speciesdata(iris,'virginica')
speciesdata(iris,'setosa')
