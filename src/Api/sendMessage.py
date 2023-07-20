import requests
import json
from Json.JsonHandler import json_load
from datetime import datetime

def sendMessage(message):
    payload = json.dumps({
  "text": message
    })
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/sendmessage'] 
    responseRaw = requests.request("POST", url, headers={}, data=payload)
    return responseRaw.status_code