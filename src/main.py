from Api.CheckDateGet import GetDate
from Api.sendMessage import sendMessage
from Api.GetIpca import monitoredPrices, durableGoods, nonDurableGoods, services
from Json.JsonHandler import json_load
from Helpers.dataframeHelper import loadExcell
from Helpers.StringHelper import check_string_in_list
from Helpers.dateHelper import dateConverter
import time
import pandas as pd

copomDates = json_load("Settings\Copom_dates.json")
ipcaDates = json_load("Settings\Ipca_dates.json")
settings = json_load("settings\settings.json")
ipcaDates = ipcaDates['dates']
dateList = []

for itens in copomDates['dates']:
    dateList.append(copomDates['dates'][itens][0]['day01'])
    dateList.append(copomDates['dates'][itens][0]['day02'])


while True:
    lastValues = loadExcell("last_values.xlsx")
    todayDateObject, todayDateString, status  = GetDate()
    isCopomDate = check_string_in_list(todayDateString,dateList)
    isIpcaDate = check_string_in_list(todayDateString,ipcaDates)
    print("Control")
    time.sleep(3)

    if isIpcaDate == True:
        try:
            responseMonitoredPrices, statusCode = monitoredPrices(1)
            responseMonitoredPrices = responseMonitoredPrices[0]
            
            if (todayDateObject==lastValues.iloc[0,1]) == False:
                try:
                    sendMessage("Olá parece que identificamos uma novo valor de: IPCA monitorados")
                    responseMonitoredPrices, monitoredPricesStatusCode = monitoredPrices(13)
                    sendMessage(str(responseMonitoredPrices[12]))
                    lastValues.iloc[0,1] = todayDateObject
                    lastValues.to_excel("last_values.xlsx", index=False)
                except Exception as error:
                    print("Error while sending message: "+error)
            
            else:
                pass
            
        except Exception as error:
            print("Sorry we couldn't get the monitored IPCA Prices, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        
        try:
            responseDurableGoods, durableGoodsResponseStatusCode = durableGoods(1)
            responseDurableGoods = responseDurableGoods[0]
            if(todayDateObject == lastValues.iloc[1,1]) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA para bens duárveis")
                responseDurableGoods, durableGoodsStatusCode = durableGoods(13)
                sendMessage(str(responseDurableGoods[12]))
                lastValues.iloc[1,1] = todayDateObject
                lastValues.to_excel("last_values.xlsx", index=False)
            
        except Exception as error:
            print("Sorry we couldn't get the monitored durable goods IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        try:
            responseNonDurableGoods, NonDurableGoodsStatusCode = nonDurableGoods(1)
            responseNonDurableGoods = responseNonDurableGoods[0]
            if(todayDateObject == lastValues.iloc[2,1]) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA para bens não duárveis")
                responseNonDurableGoods, NonDurableGoodsStatusCode = nonDurableGoods(13)
                sendMessage(str(responseNonDurableGoods[12]))
                lastValues.iloc[2,1] = todayDateObject
                lastValues.to_excel("last_values.xlsx", index=False)
            
        except Exception as error:
            print("Sorry we couldn't get the monitored non durable goods IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        try:
            responseServices, servicesStatusCode = services(1)
            responseServices = responseServices[0]
            if(todayDateObject == lastValues.iloc[3,1]) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA de serviços")
                responseServices, servicesStatusCode = durableGoods(13)
                sendMessage(str(responseServices[12]))
                lastValues.iloc[3,1] = todayDateObject
                lastValues.to_excel("last_values.xlsx", index=False)
                
                
        except Exception as error:
            print("Sorry we couldn't get the monitored durable service IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))