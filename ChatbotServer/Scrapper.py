from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


URL = "https://www.finder.com/cryptocurrency-glossary"

page = requests.get(URL)
soap = BeautifulSoup(page.content, 'html.parser')

tds = []
dictio = {}


for glos in soap.find('table'):
    for i in glos.find_all('tr'):
        for z in i.find_all('td'):
            tds.append(z.text)

for x in range(0, len(tds), 2):
    dictio[tds[x].lower()] = tds[x+1]

with open('scrap.json', 'w') as fp:
    json.dump(dictio, fp)

inte = json.loads(open('scrap.json').read())

while True:
    msg = input()
    for i in inte:
        if i in msg.lower():
            print(inte[i])