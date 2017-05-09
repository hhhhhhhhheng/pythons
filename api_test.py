import requests
ApiKey = 'f0fd380da1bf45b85760eac7cd5cbe32'
url = "http://api.openweathermap.org/data/2.5/weather?q=London"
response = requests.get(url,{"APPID":ApiKey,"lang":"zh_cn"}, )
r = response.json()
txt = str(r)
print(r)
