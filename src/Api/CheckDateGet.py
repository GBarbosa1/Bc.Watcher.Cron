import requests
from Json.JsonHandler import json_load
from datetime import datetime

def GetDate():
    url = json_load("Settings\settings.json")['endpoints'][0]['DateApiUrl'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    response = responseRaw.json()['datetime']
    datetimeObject = datetime.strptime(response, "%Y-%m-%dT%H:%M:%S.%f%z")
    formattedDate = datetimeObject.strftime("%Y-%m-%d")
    datetimeString = formattedDate
    datetimeObject = datetime.strptime(formattedDate, "%Y-%m-%d")
    return datetimeObject, datetimeString,responseRaw.status_code