#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:59:55 2018

@author: lcampbe3

exercise #7
"""

import pandas as pd
import numpy as np

#1 - print a dataframe odd rows
def odds(df):
    return (df[1: :2])
            
#2
#number of observations for a given species
def species_counts(df, species):
    sub_spec = df.loc[df["Species"] == species]
    sp_count = sub_spec["Species"].value_counts().to_frame()
    return sp_count

#test the function
iris_data = pd.read_csv("iris.csv", sep = ",")
species_counts(iris_data, "setosa")

#dataframe for specific width
def width(df, wth):
    row = df.loc[df["Sepal.Width"] > wth]
    return row

#test the function
width(iris_data, 3.5)

#function for given species -> file
def species_file(df, species):
    sp = df.loc[df["Species"] == species]
    str1 = ".csv"
    species += str1
    sp.to_csv(species, sep=",")

#test the function
species_file(iris_data, "setosa")


