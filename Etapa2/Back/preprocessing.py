import unicodedata
from joblib import load
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import re
import ftfy
import nltk
from nltk import word_tokenize
from sklearn.pipeline import FunctionTransformer
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


  
def remove_non_ascii(text):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in text:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words
  
def to_lowercase(text):
    new_words = []
    for word in text:
        new_word = word.lower()  # Convierte la palabra a minúsculas
        new_words.append(new_word)
    return new_words

def remove_punctuation(text):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in text:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words
  
def remove_stopwords(text):
    stop_words = set(stopwords.words('spanish'))
    new_words = [word for word in text if word.lower() not in stop_words]
    return new_words

def preprocessingTransformation(words):
    preprocessed_sentences = []
    for X in words:  # Flatten the list of lists
        X = to_lowercase(X)
        X = remove_punctuation(X)
        X = remove_non_ascii(X)
        X = remove_stopwords(X)
        preprocessed_sentences.append(X)
    return preprocessed_sentences

preprocessing_trans = FunctionTransformer(preprocessingTransformation)

def tokenize_words(X):
    return [word_tokenize(x) for x in X]

tokenization_trans = FunctionTransformer(tokenize_words)

stemmer = SnowballStemmer("spanish")
lemmatizer = WordNetLemmatizer()

def stem_and_lemmatize(sentences):
    return [[stemmer.stem(word) for word in words] + [lemmatizer.lemmatize(word, pos='v') for word in words] for words in sentences]

stem_and_lemm_trans = FunctionTransformer(stem_and_lemmatize)

def juntar(sentences):
    return [' '.join(map(str, x)) for x in sentences]

join_trans = FunctionTransformer(juntar)

#dataframeExample = pd.DataFrame({'Review': ['Hola, como estas? Estoy bien, gracias.', 'Seugnda fila con texto']})
#tokenizado = tokenization_trans.transform(dataframeExample['Review'])
#preprocesado = preprocessing_trans.transform(tokenizado)
#lematizado = stem_and_lemm_trans.transform(preprocesado)
#junto = join_trans.transform(lematizado)
#tfidf_vectorizer = TfidfVectorizer()
#tfidf_vectorizer.fit_transform(junto)
#print(junto)

#dataframeExample = pd.DataFrame({'Review': ['Hola, como estas? Estoy bien, gracias.', 'Seugnda fila con texto', 'mal horrible olor feo caro', 'que esta pasando aca horrible']})
#print(dataframeExample)
#model = load("modelo.joblib") ##Model.joblib fallando, estamos haciendo mal el pipeline.
#resultado = model.predict(dataframeExample["Review"])
#print(resultado)
