## Data Manipulation/Wrangling
import numpy as np
import pandas as pd

from os import listdir, path

## Preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

## Importing NLP Text Preprocessing Libraries
# !pip install nltk
import re
import nltk
# nltk.download('wordnet')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download('stopwords')
#from nltk.corpus import stopwords

## An alternative library of English stop-words in "sklearn" library rather than 'nltk'
# from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS # Google colab

## Classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from catboost import Pool, CatBoostClassifier

# Loading and saving trained models
import pickle


MODEL_PATH = 'models'

def clean_news(news_item, to_lower=False, rmv_stop_words=False, stem=False, lang='english'):
    # Removing all numbers, punctuations and special characters, and links. Extract only alphabets
    news = re.sub("@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+",' ', news_item)

    if to_lower:
        # Converting all text to lowercase
        news = news.lower().strip()
        news = news.split()

    if lang == 'english' and rmv_stop_words:
        eng_stop_words = set(ENGLISH_STOP_WORDS)
        # Remove English stop-words
        news = [word for word in news if (word not in eng_stop_words)]

    if stem:
        # Stemming (Using only the root word of every polymorphic words. e.g. Loved, Loving = Love; Eat, Ate, Eaten = Eat; etc)
        #ps = PorterStemmer()
        lemmatizer = WordNetLemmatizer()

        # Removing all common words e.g. Preposition, article, conjunction, etc.
        #news = [ps.stem(word) for word in news if word not in set(stopwords.words('english'))]
        #news = [ps.stem(word) for word in news if word not in set(ENGLISH_STOP_WORDS)]
        news = [lemmatizer.lemmatize(word, pos='n') for word in news]
        news = [lemmatizer.lemmatize(word, pos='v') for word in news]
        news = [word for word in news if len(word) > 2]

    news = ' '.join(news) if type(news) == list else news

    return news

def save_model(model, filename):
    try:
        pickle.dump(model, open(f'{MODEL_PATH}/{filename}', 'wb'))
        print('Saved')
    except Exception as err:
        print(err)

def load_model_pickle(filename):
    try:
        model = pickle.load(open(f'{MODEL_PATH}/{filename}', 'rb'))
        return model
    except Exception as err:
        print(err)
        return None
    

def predict(news_article, model_type='rf'):
    model = None
    model_name = ''
    if model_type == 'cb':
        model = load_model_pickle('cb_Model.pickle')
        model_name = 'CatBoost'
    elif model_type == 'logreg':
        model = load_model_pickle('LogReg_Model.pickle')
        model_name = 'Logistic Regresion'
    else: # if model_type == 'rf' or 'best'
        model = load_model_pickle('rf_Model.pickle')
        model_name = 'Random Forest'
    
    if model is not None:
        # Preprocess news
        # vectorize/encode news text into numbers
        # cleaned_news = clean_news(news_article, to_lower=False)
        cleaned_news = news_article
        encoder = load_model_pickle('tfidf_vectorizer.pickle')
        encoded_news = encoder.transform([cleaned_news])
        # Make Prediction
        pred_prob = model.predict_proba(encoded_news)[0]
        pred_value = int(pred_prob.argmax())
        category = 'Real News' if pred_value == 0 else 'Fake News'

        results = {
            'model': model_name,
            'confidence': f'{round(pred_prob.max() * 100, 2)}%',
            'predicted_value': pred_value,
            'predicted_category': category
        }
        
        
        return results
    
