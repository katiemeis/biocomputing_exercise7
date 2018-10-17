# This code Corresponds to exercise 7 for biocomputing
# For some reason Python deleted all of my code the first time through, so hopefully this works better

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:49:08 2018

@author: Cole
"""

# Part 1) write a function that returns the odd rows of any pandas datafram passed as an argument

import pandas as pd

wages=pd.read_csv('wages.csv', header=0, sep=',')

def oddReturn(data): # using 0-base indexing, returns odd-numbered rows of data set
    copydata=data
    column_names=copydata.columns.tolist()
    numCols=copydata.shape[1]
    print(numCols)
    for i in range (0,numCols):
        if i%2==0: # if the column number is an even number
            print(i)
            print(column_names[i])
            if i==0:
                newdata=copydata.drop([column_names[i]], axis=1)
            else:
                newdata=newdata.drop([column_names[i]], axis=1)
    return newdata
    
wages_odd_rows=oddReturn(wages) # returns the odd-numbered rows of wages USING 0-BASE INDEXING
    


# part 2: repeat a subset of last week's exercises, but write functions to accomplish these tasks
# 2a) Return the numberr of obersvations fro a given species included in the data set
# 2b) return a dataframe for flowers with Sepal.Width greater than a value specified by the function user
# 2c) write the data for a given species to a comma delimited file with the given 
# species name as the file name; hint, look at using + or % to concatenate the species name and .csv
# use iris data as values to work from
irisdata=pd.read_csv('iris.csv', header=0, sep=',')


# 2a)
def specObs(data,species): # data comes from irisdata, species could be either 'setosa', 'versicolor', or 'virginica'
    species_list=data[data.Species==species] # give all of the data for that species
    print('Number of observations of ',species) # allows for easily understood output
    print(species_list.Species.size) # count the number of instances of the current species
    obsCount=species_list.Species.size
    return obsCount

setosaCount=specObs(irisdata,'setosa') # returns number of observations of setosa in this case

# 2b

def enoughWidth(data,minWidth): # data comes from irisdata, minWidth is a float variable to set the lower bound of acceptable sepal width
    sufficientWidth=data[data['Sepal.Width']>minWidth] # save rows where width is sufficient and save
    return sufficientWidth

width4=enoughWidth(irisdata,4.0)


# 2c)

def writeSpec(data,species): # data comes from irisdata, species could be either 'setosa', 'versicolor', or 'virginica'
    species_data=data[data.Species==species]
    save_data=species_data.to_csv() # picks out data to be saved
    alt_save=open(species+'.csv','w') # opens a blank csv
    alt_save.write(save_data) # writes the dato to the open empty
    alt_save.close() # closes    


writeSpec(irisdata,'setosa') # writes data to csv file for setosa












