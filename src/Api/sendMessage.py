import requests
import json
from Json.JsonHandler import json_load
import numpy as np
from datetime import datetime

def sendMessage(message):
    payload = json.dumps({
  "text": message
    })
    url = json_load("Settings\settings.json")['endpoints'][0]['Bc.Watcher.Api/sendmessage'] 
    responseRaw = requests.request("POST", url, headers={}, data=payload)
    return responseRaw.status_code
  
def messageBuilder(jsonLoad):
  valueList = np.array([])
  for itens in jsonLoad:
      valueList = np.append(valueList,itens['valor'])
  pastMean = np.mean(valueList[:12].astype(float))
  actualMean = np.mean(valueList[1:13].astype(float))
  pastValue = valueList[11].astype(float)
  actualValue = valueList[12].astype(float)
  messageString = f"""
  O valor átual é {actualValue}, o valor passado foi de {pastValue}.
  A média de 12 meses passados é de {pastMean} contra a atual de {actualMean}
  """
  return messageString