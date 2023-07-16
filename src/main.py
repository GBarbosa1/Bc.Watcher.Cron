from Api.CheckDateGet import GetDate
from Api.GetIpca import monitoredPrices, durableGoods, nonDurableGoods, services
from Json.JsonHandler import json_load
from Helpers.StringHelper import check_string_in_list
import time
import polars as pl


copomDates = json_load("Settings\Copom_dates.json")
ipcaDates = json_load("Settings\Ipca_dates.json")
ipcaDates = ipcaDates['dates']

dateList = []

for itens in copomDates['dates']:
    dateList.append(copomDates['dates'][itens][0]['day01'])
    dateList.append(copomDates['dates'][itens][0]['day02'])

    

while True:
    todayDateObject, todayDateString, status  = GetDate()
    isCopomDate = check_string_in_list(todayDateString,dateList)
    isIpcaDate = check_string_in_list(todayDateString,ipcaDates)
    print(isCopomDate, isIpcaDate)
    print(todayDateString)
    time.sleep(3)
    
    if isIpcaDate == True:
        try:
            response_monitored_prices, statusCode = monitoredPrices()
        except Exception as error:
            print("Sorry we couldn't get the monitored IPCA Prices, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        try:
            durableGoodsResponse, durableGoodsResponseStatusCode = durableGoods()
        except Exception as error:
            print("Sorry we couldn't get the monitored durable goods IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        # try:
        #     nonDurableGoodsResponse, nonDurableGoodsStatusCode = nonDurableGoods()
        # except Exception as error:
        #     print("Sorry we couldn't get the monitored non durable goods IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        try:
            servicesResponse, servicesStatusCode = services()
        except Exception as error:
            print("Sorry we couldn't get the monitored durable service IPCA, we meet the following problems: " + str(error) + "API status code were: "+ str(statusCode))
        
        print(response_monitored_prices, durableGoodsResponse, servicesResponse)