#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:57:03 2018

@author: Samuel_Clarin
"""

##################################################################
#imports section
import pandas as pd



file_name='iris.csv'
data1=pd.read_csv(file_name,header=0,sep=",")

#problem 1
def odd(filename):
    data1=pd.read_csv(filename, header=0, sep=",")
    return data1.iloc[1::2]

odd('setosa.csv')
#observations
def obs(variable):
    return "Number of " +variable+" obs: " +str(len(data1[data1.Species==variable])) 
obs('setosa')

#get rows with Sepal.Width > number
def sepwidth(number):
    return data1[data1['Sepal.Width'] > number]
    
sepwidth(4)

def speciesfile(x):
    pathname= x+'.csv'
    data1[data1.Species==x].to_csv(path_or_buf=pathname)
    
speciesfile('virginica')