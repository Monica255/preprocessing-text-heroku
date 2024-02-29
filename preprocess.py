import numpy as np
import nltk
nltk.download('punkt')
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

def sentence_split(paragraph):
    return nltk.sent_tokenize(paragraph)

def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res

def sentence_weight(data,wordfreq):
    weights = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights

def preprocess_text(text):
    # Remove symbols
    # text = re.sub(r'[^\w\s]', '', text)

    # Remove question words in Indonesian
    question_words = ['bagaimana', 'apa', 'dimana', 'siapa', 'kapan', 'berapa', 'mengapa','itu']
    text = ' '.join(word for word in text.split() if word.lower() not in question_words)

    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # stemming process
    text   = stemmer.stem(text)

    # case folding
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans("","",string.punctuation))

    # remove white space
    text = text.strip()

    return text

def sum(text):
    data = sentence_split(text)
    wordfreq = word_freq(data)
    rank = sentence_weight(data,wordfreq)
    print("aa",text)
    n = 2
    result = ''
    sort_list = np.argsort(rank)[::-1][:n]
    for i in range(n):
        result += '{} '.format(data[sort_list[i]])

    print(result)
    return result

print(preprocess_text("apa itu hama"))