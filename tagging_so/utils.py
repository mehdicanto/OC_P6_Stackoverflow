# Import the `pandas` library as `pd`
import pandas as pd
# Import pyplot from matplotlib as plt
import matplotlib.pyplot as plt

import seaborn as sns

# Import the `numpy` library as `np`
import numpy as np

import random

from joblib import dump, load
from bs4 import BeautifulSoup
from nltk import RegexpTokenizer, bigrams, download
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer

import re
import string
from collections import Counter
from random import randint

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

from bs4 import BeautifulSoup
import nltk


download('stopwords')
download('wordnet')

from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle

modelizer = pickle.load(open("./tagging_so/modelisation_obj", 'rb'))

date = { "corpus" : 'I have a problem with a DATAFRAME <pre><code>xcode-select: Error: No Xcode folder is set. Run xcode-select -switch &lt;xcode_folder_path&gt; to set the path to the Xcode folder'}


tokenizer = RegexpTokenizer(r'\w+')
stopwords = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()

def main(data):
    data = to_lower(data)




def to_lower(x):
    text = x.lower()
    return text

x = to_lower(x)

text_2=BeautifulSoup(x, 'html.parser').text

def tokenize_body(body_full):
    list_a = tokenizer.tokenize(body_full)
    token_list = [wordnet_lemmatizer.lemmatize(word) for word in list_a if (word not in stopwords and not word.isdigit())]
    return token_list

text_3 = tokenize_body(text_2)


def join_body_tokens(body):
    return " ".join(body)

txt = tokenize_body(text_3)

