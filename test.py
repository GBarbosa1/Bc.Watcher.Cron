import requests

url = "http://127.0.0.1:8000/Ipca/PrecosMonitoradosTotal/13"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(str(response[12]))

