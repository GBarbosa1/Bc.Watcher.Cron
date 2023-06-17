import requests
from Json.JsonHandler import json_load
from datetime import datetime

def GetDate():
    url = json_load("Settings\settings.json")['url'][0]['DateApiUrl'] 
    response = requests.request("GET", url, headers={}, data={})
    response = response.json()['datetime']
    datetime_object = datetime.strptime(response, "%Y-%m-%dT%H:%M:%S.%f%z")
    formatted_date = datetime_object.strftime("%Y-%m-%d")
    datetime_string = formatted_date
    datetime_object = datetime.strptime(formatted_date, "%Y-%m-%d")
    return datetime_object, datetime_string