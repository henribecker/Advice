import requests, json

def get():
    obj = requests.get('https://api.adviceslip.com/advice')
    mjson = json.loads(obj.text)
    for n in mjson.values():
        num = str(n['advice'])
        return num