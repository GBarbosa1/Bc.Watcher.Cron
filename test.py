import polars as pl
import datetime

def loadExcell(filePath):
    lastValues = pl.read_excel(filePath)
    return lastValues

def readVar(dataframe,column, indicator):
    value  = dataframe[dataframe[column]] == indicator
    return value

lastValues = loadExcell("last_values_copy.xlsx")
a = lastValues['value'][0]
a = datetime.datetime.strptime(a, '%m-%d-%y').strftime('%m/%d/%Y')
print(a)

