#Data Correlations:
#-----------------#

#Finding Relationships
#A great aspect of the Pandas module is the corr() method.

#The corr() method calculates the relationship between each column in your data set.

#Example
#Show the relationship between the columns:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())

#***Note: The corr() method ignores "not numeric" columns.
