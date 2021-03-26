import sklearn
import os
from bs4 import BeautifulSoup
from nltk import RegexpTokenizer, bigrams, download
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer
import re
import string
from random import randint
import numpy as np
import pandas as pd
import nltk
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
download('stopwords')
download('wordnet')


modelizer = pickle.load(open("./tagging_so/modelisation_obj", 'rb'))
vectorizer = modelizer.get("vectorizer")
transformer = modelizer.get("transformer")
model = modelizer.get("model")
get_tags = modelizer.get("mlb")

data = { "corpus" : 'I have a problem with a DATAFRAME with numpy <pre><code>xcode-select: Error: No Xcode folder is set. Run xcode-select -switch &lt;xcode_folder_path&gt; to set the path to the Xcode folder'}


tokenizer = RegexpTokenizer(r'\w+')
stopwords = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()

def main(data):
    data = data.get("corpus")
    print(data)
    data = to_lower(data)
    data = word_replace(data)
    text_2 = BeautifulSoup(data, 'html.parser').text
    text_3 = tokenize_body(text_2)
    txt_array=np.array([" ".join(text_3)])
    print(txt_array)
    x_vect = vectorizer.transform(txt_array)
    x_tfidf = transformer.transform(x_vect)
    y_pred = model.predict(x_tfidf)
    tags = get_tags.inverse_transform(y_pred)
    print(tags)
    if tags:
        tags = [item for sublist in tags for item in sublist]
    return tags


def to_lower(x):
    text = x.lower()
    return text


def tokenize_body(body_full):
    list_a = tokenizer.tokenize(body_full)
    token_list = [wordnet_lemmatizer.lemmatize(word) for word in list_a if (word not in stopwords and not word.isdigit())]
    return token_list



def join_body_tokens(body):
    return " ".join(body)

def word_replace(text):
    '''
    Replace words found in Worddict
    '''
    wordDict = {
    "c++": "cplusplus",
    'c#': 'csharp',
    '.net': 'dotnet',
    'd3.js': 'd3js',
    'node.js': 'nodejs'
    }
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text
