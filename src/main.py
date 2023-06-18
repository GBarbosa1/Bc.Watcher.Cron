from Api.CheckDateGet import GetDate
from Api.GetIpca import getIpca
from Json.JsonHandler import json_load
from Helpers.StringHelper import check_string_in_list
import time
copomDates = json_load("Settings\Copom_dates.json")
ipcaDates = json_load("Settings\Ipca_dates.json")
ipcaDates = ipcaDates['dates']

dateList = []

for itens in copomDates['dates']:
    dateList.append(copomDates['dates'][itens][0]['day01'])
    dateList.append(copomDates['dates'][itens][0]['day02'])

    

while True:
    todayDateObject, todayDateString, status  = GetDate()
    print(status)
    isCopomDate = check_string_in_list(todayDateString,dateList)
    isIpcaDate = check_string_in_list(todayDateString,ipcaDates)
    time.sleep(3)
    
    if isIpcaDate == True:
        try:
            response, statusCode = getIpca()
        except Exception as error:
            print("Sorry we couldn't get the IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
            
        