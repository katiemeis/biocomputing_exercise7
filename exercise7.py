#BIOCOMPUTING EXERSIZE 7 CODE 
import pandas as pd 
data=pd.read_csv('iris.csv',header=0,sep=',')

#Task 1: function that returns the odd (1, 3, 5, etc.) rows of any pandas dataframe
def oddrows(variable):
    odd=variable[1::2]
    
    return odd

oddrows(data)

#Task 2a: function that return the number of observations for a given species included in the data set
def sp_obs(variable,species):
    species=variable[data.Species=='species']
    length=len(species)
    
    return length 

sp_obs(data,'setosa')

#Task 2b: dataframe for flowers with Sepal.Width greater than a value specified by the function user
def Sepal_Width(variable,n):
    Width=variable.loc[variable['Sepal.Width']>n]
    
    return Width

Sepal_Width(data,3.5)
    
#Task 2c: data for a given species to a comma-delimited file with the given species name as the file name; Hint: look at using + or % to concatenate your species name and “.csv”































































