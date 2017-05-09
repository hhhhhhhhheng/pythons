#Messenger
from twilio.rest import Client
import requests

ApiKey = 'f0fd380da1bf45b85760eac7cd5cbe32'
url = "http://api.openweathermap.org/data/2.5/weather?q=London"
response = requests.get(url,{"APPID":ApiKey,"lang":"zh_cn","units":"metric"})

account_sid = "AC3adbf3130fd941ac7ae7802b01279ece"# Your Account SID from twilio.com/console
                        
auth_token  = "60fb3583e2f7dba19eb15eb3874a33b8"# Your Auth Token from twilio.com/console
                        
client = Client(account_sid, auth_token)

r = response.json()
txt = "Today's weather is the following" + str(r)
message = client.messages.create(
    to="+447858759011", 
    from_="+441554260011",
    body= txt)

print(message.sid)
