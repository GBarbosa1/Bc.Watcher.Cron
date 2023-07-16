import requests
from Json.JsonHandler import json_load

def monitoredPrices():
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/PrecosMonitoradosTotal'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    return responseRaw.json(), responseRaw.status_code

def durableGoods():
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/DurableGoods'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    return responseRaw.json(), responseRaw.status_code

def nonDurableGoods():
    url = json_load("Settings\settings.json")['endpoints'][0]['c.Watcher.Api/NonDurableGoods'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    return responseRaw.json(), responseRaw.status_code

def services():
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/Services'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    return responseRaw.json(), responseRaw.status_code