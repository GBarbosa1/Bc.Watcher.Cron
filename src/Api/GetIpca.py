import requests
from Json.JsonHandler import json_load
from datetime import datetime

def getIpca():
    url = json_load("Settings\settings.json")['url'][0]['Bc.Watcher.Api'] 
    responseRaw = requests.request("GET", url, headers={}, data={})
    return responseRaw.json(), responseRaw.status_code