import pandas as pd

def loadExcell(filePath):
    lastValues = pd.read_excel(filePath)
    return lastValues