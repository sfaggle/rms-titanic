
# Built in Libraries
# none

# Third Party Libraries
import pandas as pd
import numpy as np

# Local Libraries
# none

FILENAME = 'data/train.csv'

def loaddata(filename):
    """Computer, load data from the titanic"""
    df = pd.read_csv(filename,header=0)
    return df

def printinfo(df):
    """ Tell me more about my data Mr. Spock!"""

    print '---------- PANDAS Datatype Info --------------'
    print df.dtypes
    
    print '---------- PANDAS Defaul Info --------------'
    df.info()

    print '' 
    print '---------- PANDAS Description ----------------'
    df.describe()


if __name__ == "__main__":
    df = loaddata(FILENAME)
    printinfo(df)


