from requests import get 
import requests
import time
from time import sleep
data = {
    'username': 'Status',
    'embeds': [{
        'title': 'Status',
        'description': "Down!"
    }]
}
provideurl = input("Url of your website:")
weburl = input("Url of webhook:")
url = get(provideurl).text
webhookurl = weburl
while True:
    
    if url == "up":
      
        print("The website is up !")
    else:
        print("The website is down ")
    
        result = requests.post(webhookurl,json=data)

    try:
        
        result.raise_for_status()
    except:
        pass
    time.sleep(10)