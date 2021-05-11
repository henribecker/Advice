import requests, json

def dolarget():
    obj = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    print(obj.status_code)
    print(obj.text)
    obj1 = json.loads(obj.text)
    for i in obj1.values():
        a = [i['bid'], i['high'], i['low']]
        return a
