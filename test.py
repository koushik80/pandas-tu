#Pandas is usually imported under the pd alias.
#alias: In Python alias are an alternate name for referring to the same thing.

import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#Checking Pandas Version

# The version string is stored under __version__ attribute.

print(pd.__version__)
