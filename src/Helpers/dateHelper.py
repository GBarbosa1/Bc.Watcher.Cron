import datetime

def dateConverter(originDate, finalDate):
    finalDate = datetime.datetime.strptime(originDate, '%m-%d-%y').strftime('%m/%d/%Y')
    return finalDate