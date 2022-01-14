from newspaper import Article
import random
import pandas as pd
import datetime
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import ChatbotServer.Database.db_operations as op
warnings.filterwarnings('ignore')


intents = json.loads(open('../Files/intents.json').read())
new = json.loads(open('../Files/scrap.json').read())
list_of_deff = ''

for s in new:
    list_of_deff = list_of_deff + s + '\n'


cp = open('../Files/current_prices.txt', 'r')
cp = [line[:-1] for line in cp]
prices = ''
for x in cp:
    prices += (x +'\n')


user_greetings = []
user_bye = []
user_thanks = []

bot_greetings = []
bot_bye = []
bot_thanks = []

for i in intents['intents']:
    for pattern in i['patterns']:
        if i['tag'] == 'greetings':
            user_greetings.append(pattern)
        elif i['tag'] == 'goodbye':
            user_bye.append(pattern)
        elif i['tag'] == 'thanks':
            user_thanks.append(pattern)
    for resp in i['responses']:
        if i['tag'] == 'greetings':
            bot_greetings.append(resp)
        elif i['tag'] == 'goodbye':
            bot_bye.append(resp)
        elif i['tag'] == 'thanks':
            bot_thanks.append(resp)


def welcome(text):
    text = text.lower()

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def own_alg(user_input):
    user_input = user_input.lower()
    if user_input == '--help':
        return "Type --show def to display a list of definitions. \n Type --show prices to see cryptocurrency prices."
    if user_input == '--show prices':
        return prices
    if user_input == '--show def':
        return list_of_deff
    if user_input in new:
        return new[user_input]
    else:
        return "Sorry, i don't understand. Use --help for more information."


def talk(user_input):
    if user_input.lower() in user_bye:
        return(f"CryptoBot: {random.choice(bot_bye)}")
    if user_input.lower() in user_thanks:
        return(f"CryptoBot: {random.choice(bot_thanks)}")
    else:
        if welcome(user_input) != None:
            return(f"CryptoBot: {welcome(user_input)}")
        else:
            return(f"CryptoBot: {own_alg(user_input)}")






