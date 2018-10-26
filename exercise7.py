# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:26:57 2018

@author: bretl
"""

# odd rows in pandas

import pandas as pd
#make up any pandas dataframe in the line below
df = pd.DataFrame({'a':['paris','basil','berlin'],
                   'b':['france','switzerland','germany'],
                   'c':[1,2,3]})
def odd(df):
    oddr = df.iloc[::2]
    print oddr
    
odd(df)

#iris species count
iris = pd.read_csv("iris.csv",header=0,sep=',')

def speccount(iris):
    specc=iris.Species.value_counts()
    print specc
    
speccount(iris)

# sepal width greater than x

def bigsep(iris):
    x=3.5
    largesep=iris[iris['Sepal.Width']>x]
    print largesep
    
bigsep(iris)

#write all rows for a single species as csv file with speciesname
def indspec(iris):
    spec = iris[iris.Species == 'setosa' ]
    spec.to_csv('setosa.csv')
    
indspec(iris)

