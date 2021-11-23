import requests, time

while True:
    r = requests.get('http://kpalch.herokuapp.com/about')
    #print(r.text)
    print(r.status_code)
    time.sleep(3500)
