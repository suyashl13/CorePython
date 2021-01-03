import requests as rq
import json
import lxml


def getData(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print(e)


def load_json(data):
    j = json.loads(data)

    wind = j['wind']['speed']
    return wind


def main():
    url = "https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22"
    print("Wind Speed : ", load_json(getData(url)))
    

if __name__ == '__main__':
    main()