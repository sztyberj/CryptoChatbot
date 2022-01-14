from bs4 import BeautifulSoup
import requests
import os
import ChatbotServer.Database.db_operations as op
import json

URL_glossary = "https://www.finder.com/cryptocurrency-glossary"

glossary = requests.get(URL_glossary)
soap_glossary = BeautifulSoup(glossary.content, 'html.parser')
tds = []
table = []
dictio = {}

def scrap_website():
    #Scrap glossary
    for glos in soap_glossary.find('table'):
        for i in glos.find_all('tr'):
            for z in i.find_all('td'):
                tds.append(z.text)

    for x in range(0, len(tds), 2):
        dictio[tds[x].lower()] = tds[x+1]
        table = [(tds[x].lower(), tds[x+1])]
        op.insert_glossary('Glossary', table)


if op.count_glossary() < 117:
    op.delete_all('Glossary')
    scrap_website()
    print("Zasilono bazę pojęciami")

if not os.path.exists('../Files/scrap.json'):
    for i in op.select_all_gloss('Glossary'):
        dictio[i[0]] = i[1]
    with open('../Files/scrap.json', 'w') as fp:
        json.dump(dictio, fp)
        print("Zapisano wyniki z bazy do pliku scrap.json")


