from newspaper import Article
import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

article = Article('https://www.finder.com/cryptocurrency-glossary')
article.download()
article.parse()
article.nlp()
corpus = article.text

text = corpus
sentense_list = nltk.sent_tokenize(text)

intents = json.loads(open('../Files/intents.json').read())

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

def index_sort(list_var):
    lenght = len(list_var)
    list_index = list(range(0, lenght))

    x = list_var
    for i in range(lenght):
        for j in range(lenght):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

def bot_response(user_input):
    user_input = user_input.lower()
    sentense_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentense_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentense_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response + ' ' + "Sorry, I dont understand."

    sentense_list.remove(user_input)

    return bot_response


def talk(user_input):
    if user_input.lower() in user_bye:
        return(f"CryptoBot: {random.choice(bot_bye)}")
    if user_input.lower() in user_thanks:
        return(f"CryptoBot: {random.choice(bot_thanks)}")
    else:
        if welcome(user_input) != None:
            return(f"CryptoBot: {welcome(user_input)}")
        else:
            return(f"CryptoBot: {bot_response(user_input)}")






