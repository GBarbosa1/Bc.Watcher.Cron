import requests
from Json.JsonHandler import json_load

def monitoredPrices(last):
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/PrecosMonitoradosTotal'] + str(last)
    responseRaw = requests.request("GET", url, headers={}, data={}).json()
    return responseRaw

# def durableGoods(last):
#     url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/DurableGoods'] + str(last)
#     responseRaw = requests.request("GET", url, headers={}, data={})
#     return responseRaw, responseRaw.status_code

# def nonDurableGoods(last):
#     url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/NonDurableGoods'] + str(last)
#     responseRaw = requests.request("GET", url, headers={}, data={})
#     return responseRaw.json(), responseRaw.status_code

# def services(last):
#     url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/Services'] + str(last)
#     responseRaw = requests.request("GET", url, headers={}, data={})
#     return responseRaw.json(), responseRaw.status_code
