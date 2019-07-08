from tkinter import * 
from tkinter import ttk

import configparser
import json
import requests

config = configparser.ConfigParser()
config.read('config.ini')

inSymbol = input('Moneda a convertir :')
outSymbol = input('Moneda convertida :')

url = config['fixer.io']['ALL_SYMBOLS_EP']
api_key = config['fixer.io']['API_KEY']

url = url.format(api_key, inSymbol, outSymbol)
response = requests.get(url)

if response.status_code == 200:
    currencies = json.loads(response.text)
    print(currencies)
    print(currencies['symbols']['USD'])
else:
    print("Error en peticion ",response.status_code)
