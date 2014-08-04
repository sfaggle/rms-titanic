
# Built in Libraries
# none

# Third Party Libraries
import pandas as pd
import numpy as np
import pylab as P

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

def agehist(df):
    """Did you die due to old age? Heart attacks?"""
    df['Age'].hist()
    P.show()

def run():
    df = loaddata(FILENAME)
    printinfo(df)
    agehist(df)

if __name__ == "__main__":
    run()
