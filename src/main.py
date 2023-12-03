from Api.CheckDateGet import GetDate
from Api.sendMessage import sendMessage, messageBuilder
from Api.GetIpca import monitoredPrices, durableGoods , nonDurableGoods, services
from Api.getRecord import getRecordDate, getRecordLink
from Json.JsonHandler import json_load
from Helpers.dataframeHelper import loadExcell
from Helpers.StringHelper import check_string_in_list
import time
import pandas as pd
from datetime import datetime

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
    pd.to_datetime(lastValues['value'])
    todayDateObject, todayDateString, status  = GetDate()
    isCopomDate = check_string_in_list(todayDateString,dateList)
    isIpcaDate = check_string_in_list(todayDateString,ipcaDates)
    
    if isCopomDate == True:
        print(isCopomDate)
        try:
            recordDate = getRecordDate()
            recordDate = datetime.strptime(recordDate, '%d/%m/%Y')
            if(recordDate == lastValues.iloc[4,1].to_pydatetime()) == False:
                sendMessage("Olá parece que identificamos uma nova ata do Copom, segue o link para download")
                recordLink = getRecordLink()
                sendMessage(recordLink)
                lastValues.iloc[4,1] = recordDate
                lastValues.to_excel("last_values.xlsx", index=False)
                    
        except Exception as error:
            print("Sorry we couldn't get the record on the COPOM meeting, we meet the following problems: " + str(error))

    if isIpcaDate == True:
        try:
            print(isIpcaDate)
            responseMonitoredPrices= monitoredPrices(1)
            responseMonitoredPrices = responseMonitoredPrices[0]['data']
            responseMonitoredPricesDate = datetime.strptime(responseMonitoredPrices, '%d/%m/%Y')
            
            if (responseMonitoredPricesDate==lastValues.iloc[0,1].to_pydatetime()) == False:
                try:
                    sendMessage("Olá parece que identificamos uma novo valor de: IPCA monitorados")
                    responseMonitoredPrices = monitoredPrices(13)
                    messageString = messageBuilder(responseMonitoredPrices)
                    sendMessage(messageString)
                    lastValues.iloc[0,1] = responseMonitoredPricesDate
                    lastValues.to_excel("last_values.xlsx", index=False)
                    
                except Exception as error:
                    print("Error while sending message: "+str(error))
            
            else:
                pass
            
        except Exception as error:
            print("Sorry we couldn't get the monitored IPCA Prices, we meet the following problems: " + str(error))
        
        
        try:
            responseDurableGoods = durableGoods(1)
            responseDurableGoods = responseDurableGoods[0]['data']
            responseDurableGoodsDate = datetime.strptime(responseDurableGoods, '%d/%m/%Y')
            
            if(responseDurableGoodsDate == lastValues.iloc[1,1].to_pydatetime()) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA para bens duárveis")
                responseDurableGoods = durableGoods(13)
                messageString = messageBuilder(responseDurableGoods)
                sendMessage(messageString)
                lastValues.iloc[1,1] = responseDurableGoodsDate
                lastValues.to_excel("last_values.xlsx", index=False)
            
        except Exception as error:
            print("Sorry we couldn't get the monitored durable goods IPCA, we meet the following problems: " + str(error))
        
        try:
            responseNonDurableGoods = nonDurableGoods(1)
            responseNonDurableGoods = responseNonDurableGoods[0]['data']
            responseNonDurableGoodsDate = datetime.strptime(responseNonDurableGoods, '%d/%m/%Y')
            
            if(responseNonDurableGoodsDate == lastValues.iloc[2,1].to_pydatetime()) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA para bens não duárveis")
                responseNonDurableGoods = nonDurableGoods(13)
                messageString = messageBuilder(responseNonDurableGoods)
                sendMessage(messageString)
                lastValues.iloc[2,1] = responseNonDurableGoodsDate
                lastValues.to_excel("last_values.xlsx", index=False)
            
        except Exception as error:
            print("Sorry we couldn't get the monitored non durable goods IPCA, we meet the following problems: " + str(error))
        
        try:
            responseServices = services(1)
            responseServices = responseServices[0]['data']
            responseServicesDate = datetime.strptime(responseServices, '%d/%m/%Y')
            if(responseServicesDate == lastValues.iloc[3,1].to_pydatetime()) == False:
                sendMessage("Olá parece que identificamos uma novo valor de: IPCA de serviços")
                responseServices = durableGoods(13)
                messageString = messageBuilder(responseServices)
                sendMessage(messageString)
                lastValues.iloc[3,1] = responseServicesDate
                lastValues.to_excel("last_values.xlsx", index=False)
                
                
        except Exception as error:
            print("Sorry we couldn't get the monitored durable service IPCA, we meet the following problems: " + str(error))
            
    
    print("Control")
    time.sleep(30)
    
            
            