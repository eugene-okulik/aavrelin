from datetime import datetime
from time import sleep
import requests

while True:
    requests.get('https://ya.ru/')
    print(datetime.now())
    sleep(2)
    