import json
#Functgion inteded to read the settings.json

def json_load(filePath):
    with open(filePath,"r") as file:
        jsonData = json.load(file)
    return jsonData

