import requests, time

while True:
    r = requests.get('http://kpalch.herokuapp.com')
    print(r.text)
    time.sleep(3500)
