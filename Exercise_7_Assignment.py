#I put importing pandas and reading the file first and outside of any of the functions for the sake of not being repititious
#I also made all of my functions ask for any necessary user input on the command line, except for the first one since it
#specified that it should be passed as an argument.  I personally simply like the clarity of the command line specifying what to input
import pandas as pd
iris = pd.read_csv("iris.csv")

#Problem 1
def return_odd(dataframe):
    print("\nQuestion 1:")
    print(dataframe.iloc[1::2])
return_odd()

#Problem 2
#Part 1
#As with the previous assignment, I opted to have my code return a data frame stating there are 50 values for
#each measurement for the given species,so you know that the number of observations (where each row is an observation)
#is 50 since each measurement returns a value of 50, meaning that there are 50 rows of observations for the species.
#I thought this made it easier to interpret and understand what is actually being printed than using .size() instead of .count()
def observations():
    print("\nQuestion 2:")
    print("\nPart 1:")
    species = input("Please enter the species (in quotation marks) you wish to know the number of observations for: ")
    species_observations = iris[iris["Species"] == species]
    print(species_observations.groupby("Species").count())
observations()

#Part 2
def sepal_width():
    print("\nPart 2:")
    width = input("Please enter the sepal width value you wish to know the observation values for, for all flowers with a width greater than your given value: ")
    print(iris[iris["Sepal.Width"] > width])
sepal_width()

#Part 3
def write_file():
    print("\nPart 3:")
    species = input("Please enter the species (in quotation marks) you wish to generate a new .csv file for containing all of its data: ")
    species_data = iris[iris["Species"] == species]
    species_data.to_csv(species + ".csv")
write_file()