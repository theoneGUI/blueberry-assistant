import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import data
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
from common_ground import *
with open("intents.json") as file:
    data = json.load(file)

try:
    #a
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    #a  
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat(inp):
    while True:
        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        resp="ok"
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        if tag=='knowitall':
            exec("import data ; data.knowledge(inp,False)")
        elif tag=='skip':
            exec("from pyautogui import * ; hotkey('nexttrack')")
        elif tag=='weather':
            exec("import data, common_ground; w=data.Weather(); common_ground.say(w.deepReport())")
        elif tag=='sleepytime':
            exec("import data ; data.sleepChild()")
        elif tag=='tyme':
            exec("import data; data.currentTimeandDate()")
        elif tag=="learning":
            say('Preparing to learn...')
            resp='.lern'
        elif tag=="restart":
            say('Preparing to restart...')
            resp='exitting. shutdown now'
        elif tag=="insult":
            resp=random.choice(responses)
            if resp=="o yeah lizzy boy":
                os.system('aplay lizzy.wav')
                resp='Take that'
            else:
                pass
        if resp=='exitting. shutdown now' or resp=='.lern':
            pass
        elif resp=='o yeah lizzy boy' or resp=="Take that":
            resp=''
        else:
            resp=random.choice(responses)
        return resp
