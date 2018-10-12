import pandas as pd
import numpy as np

data = pd.read_csv('../biocomputing_exercise6/iris.csv', header =0 )

#Problem 1
def odder(data):
    return data[1::2]


#Problem 2
def speciesCounter(data,species):
    speciesCount=0
    for i in range(len(data.iloc[:,4])):
        if data.iloc[i,4] ==species:
            speciesCount+=1

    return speciesCount

def sepalSizer(data,size):
    newData = data.loc[data['Sepal.Width']>size]
    return newData

def speciesData(data,species):
    rowSpecies = data.loc[data['Species']=='setosa']
    rowSpecies.to_csv(species+'.csv', sep=',')
