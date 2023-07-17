import polars as pl

def loadExcell(filePath):
    lastValues = pl.read_excel(filePath)
    return lastValues

def readVar(dataframe,column, indicator):
    value  = dataframe[dataframe[column]] == indicator
    return value