import requests, json

def get():
    obj = requests.get('https://api.adviceslip.com/advice')
    if obj.status_code != 200:
        return False
    else:
        # print(obj.status_code)
        mjson = json.loads(obj.text)
        for n in mjson.values():
            num = str(n['advice'])
            return num

def dolarget():
    obj = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    print(obj.status_code)
    print(obj.text)
    obj1 = json.loads(obj.text)
    for i in obj1.values():
        a = [i['bid'], i['high'], i['low']]
        return a
