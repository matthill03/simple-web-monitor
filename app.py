import imp
import time
import hashlib
from urllib import response
from urllib.request import urlopen, Request
from twilio.rest import Client

with open('acount.txt') as file:
    lines = file.readlines()
    print(lines[0].strip())

account_sid = lines[0].strip()
auth_token = lines[1]
client = Client(account_sid, auth_token)

def send_message(message):
    message = client.messages \
        .create(
            body=message,
            from_='<Twillio Phone Number>',
            to='<Phone Number>'
        )

    print(message.sid)

url = Request('https://www.bbc.co.uk/sport/football/transfers', headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

currentHash = hashlib.sha224(response).hexdigest()
send_message('I am running!!')
print('Running!!')
time.sleep(1800)

while True:
    try:
        response = urlopen(url).read()

        currentHash = hashlib.sha224(response).hexdigest()
        print(currentHash)

        time.sleep(3600)

        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()
        print(newHash)

        if newHash == currentHash:
            send_message('Nothing has changed!!')
            continue

        else:
            print('Something has changed!!')
            
            send_message('Something has changed!!')

            response = urlopen(url).read()

            currentHash = hashlib.sha224(response).hexdigest()

            time.sleep(3600)
            continue
    
    except Exception as e:
        print(e)
