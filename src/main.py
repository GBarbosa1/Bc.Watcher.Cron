from Api.CheckDateGet import GetDate
from Json.JsonHandler import json_load
from Helpers.StringHelper import check_string_in_list
import time
dates = json_load("Settings\Copom_dates.json")
dateList = []

for itens in dates['dates']:
    dateList.append(dates['dates'][itens][0]['day01'])
    dateList.append(dates['dates'][itens][0]['day02'])
    

while True:
    todayDateObject, todayDateString  = GetDate()
    isCopomDate = check_string_in_list(todayDateString,dateList)
    time.sleep(3)
    
    