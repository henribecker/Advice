import requests, json

def get():
    obj = requests.get('https://api.adviceslip.com/advice')
    mjson = json.loads(obj.text)
    print(obj.status_code)
    for n in mjson.values():
        num = str(n['advice'])
        return num