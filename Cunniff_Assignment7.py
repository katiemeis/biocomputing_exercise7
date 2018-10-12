# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:48:14 2018

@author: Patrick
"""

#NUMBER 1
#Return only the odd variables from a panda dataframe passed as a variable
#usage: odds(name_of_pandas_dataframe)

#The odd numbered rows have index=0,2,4,etc because that's how python indexes
#To select for only rows with odd index #, use data.iloc[1::2] instead of data.iloc [::2]
def odds(dataframe):
    oddrows=dataframe.iloc[::2]
    return oddrows


#NUMBER 2
import pandas as pd
data=pd.read_csv("iris.csv", header=0,sep=',')
data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
#Return number of observations for a given species included in the data set
#Usage: SpeciesObsrv('name_of_species_for_which_you_want_obervation_number')
def SpeciesObsrv(species_name):
    b=data.iloc[:,4]
    c=b.to_csv()
    spobs= c.count(species_name)
    print (species_name,":",spobs)
    return spobs


#Return a dataframe for flowers with Sepal Width greater than certain number
#Usage: wider_sepals(sepal width you want to specify larger than)
def wider_sepals(n):
    wide_sepals = data[data.Sepal_width > n]
    print (wide_sepals)
    return wide_sepals
    
#Write the data for a given species to a comma-delimited file with the given species name 
    #as the file name
#Usage: Save_species('species_name')
def Save_species(species_name):
    species=data[data.Species == species_name]
    save = species.to_csv()
    saving = open(species_name+'.csv','w')
    saving.write(save)
    saving.close()
    return saving



















