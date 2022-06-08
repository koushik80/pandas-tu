#Pandas - Cleaning Data:
#----------------------#

#Data cleaning means fixing bad data in your data set.

#Bad data could be:

    #*Empty cells
    #*Data in wrong format
    #*Wrong data
    #*Duplicates

#In this tutorial you will learn how to deal with all of them.

#---------------------------

#Empty Cells:
#Empty cells can potentially give you a wrong result when you analyze data.

#Remove Rows:
#One way to deal with empty cells is to remove rows that contain empty cells.

#This is usually OK, since data sets can be very big,
#and removing a few rows will not have a big impact on the result.

#Example
#Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#**Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

#If you want to change the original DataFrame, use the

          # inplace = True argument:

#import pandas as pd
#df = pd.read_csv('data.csv')

df.dropna(inplace=True)

#print(df.to_string())

#***Note: Now, the dropna(inplace = True) will NOT return a new DataFrame,
#but it will remove all rows containing NULL values from the original DataFrame.

#Replace Empty Values
#Another way of dealing with empty cells is to insert a new value instead.

#This way you do not have to delete entire rows just because of some empty cells.

#The fillna() method allows us to replace empty cells with a value:

#Example
#Replace NULL values with the number 130:

#import pandas as pd

#df = pd.read_csv('data.csv')

df.fillna(130, inplace=True)


#Replace Only For Specified Columns
#The example above replaces all empty cells in the whole Data Frame.

#To only replace empty values for one column,
#specify the column name for the DataFrame:

#Example
#Replace NULL values in the "Calories" columns with the number 130:

#import pandas as pd

#df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace=True)

#------------------------------------------------------------#

#Cleaning Data of Wrong Format:

#Data of Wrong Format
#Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

#To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

#Convert Into a Correct Format
#In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26,
#the 'Date' column should be a string that represents a date:

#Let's try to convert all cells in the 'Date' column into dates.

#Pandas has a to_datetime() method for this:

#Example
#Convert to date:

#import pandas as pd

#df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

#print(df.to_string())

#As you can see from the result,
#the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value,
#in other words an empty value. One way to deal with empty values is simply removing the entire row.

#Removing Rows
#The result from the converting in the example above gave us a NaT value,
#which can be handled as a NULL value, and we can remove the row by using the dropna() method.

#Example
#Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace=True)

#Replacing Values
#One way to fix wrong values is to replace them with something else.

#In our example,
#it is most likely a typo, and the value should be "45" instead of "450",
#and we could just insert "45" in row 7:

#Example
#Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45

#For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

#To replace wrong data for larger data sets you can create some rules,
#e.g. set some boundaries for legal values,
#and replace any values that are outside of the boundaries.

#Example
#Loop through all values in the "Duration" column.

#If the value is higher than 120, set it to 120:

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120


#Removing Rows
#Another way of handling wrong data is to remove the rows that contains wrong data.

#This way you do not have to find out what to replace them with,
#and there is a good chance you do not need them to do your analyses.

#Example
#Delete rows where "Duration" is higher than 120:

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)


#Discovering Duplicates
#Duplicate rows are rows that have been registered more than one time.

#By taking a look at our test data set,
#we can assume that row 11 and 12 are duplicates.

#To discover duplicates, we can use the duplicated() method.

#The duplicated() method returns a Boolean values for each row:

#Example
#Returns True for every row that is a duplicate, othwerwise False:

print(df.duplicated())

#Removing Duplicates
#To remove duplicates, use the drop_duplicates() method.

#Example
#Remove all duplicates:
df.drop_duplicates(inplace=True)

#***Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame,
#but it will remove all duplicates from the original DataFrame.
