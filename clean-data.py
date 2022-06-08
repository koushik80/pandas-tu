#Pandas - Cleaning Data
#----------------------

#Data cleaning means fixing bad data in your data set.

#Bad data could be:

    #*Empty cells
    #*Data in wrong format
    #*Wrong data
    #*Duplicates

#In this tutorial you will learn how to deal with all of them.

#---------------------------

#Empty Cells
#Empty cells can potentially give you a wrong result when you analyze data.

#Remove Rows
#One way to deal with empty cells is to remove rows that contain empty cells.

#This is usually OK, since data sets can be very big,
#and removing a few rows will not have a big impact on the result.

#Example
#Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
