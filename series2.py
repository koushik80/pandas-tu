#Key/Value Objects as Series
#You can also use a key/value object, like a dictionary, when creating a Series.

#Example
#Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#Note: The keys of the dictionary become the labels.

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

#Example
#Create a Series using only data from "day1" and "day2":


        #calories = {"day1": 420, "day2": 380, "day3": 390}
        #myvar = pd.Series(calories, index=["day1", "day2"])
        #print(myvar)
