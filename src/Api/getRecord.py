import requests
from Json.JsonHandler import json_load

def getRecordDate():
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/record']
    responseRaw = requests.request("GET", url, headers={}, data={}).json()
    return responseRaw

def getRecordLink():
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/recordLink']
    responseRaw = requests.request("GET", url, headers={}, data={}).json()
    return responseRaw