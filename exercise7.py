#BIOCOMPUTING EXERSIZE 7 
import pandas as pd 
data=pd.read_csv('iris.csv',header=0,sep=',')

#Task 1: function that returns the odd (1, 3, 5, etc.) rows of any pandas dataframe
def oddrows(variable):
    odd=variable[1::2]
    
    return odd

oddrows(data)

#Task 2a: function that return the number of observations for a given species included in the data set
def sp_obs(variable,species):
    species=variable.loc[variable.Species==species]
    length=len(species)
    
    return length 
   
sp_obs(data,'setosa')

#Task 2b: dataframe for flowers with Sepal.Width greater than a value specified by the function user
def Sepal_Width(variable,n):
    Width=variable.loc[variable['Sepal.Width']>n]
    
    return Width

Sepal_Width(data,3.5)
    
#Task 2c: data for a given species to a comma-delimited file with the given species name as the file name
def species(variable, name):
    sp=variable.loc[variable['Species']==name]
    sp.to_csv(path_or_buf=name+'.csv')
    return sp

species(data, 'virginica')
species(data,'setosa')
species(data,'versicolor')























































