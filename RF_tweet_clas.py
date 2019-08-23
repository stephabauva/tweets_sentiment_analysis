#import dependencies
import pandas as pd
import re
import pickle

import nltk
nltk.download('stopwords'); from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize 
nltk.download('punkt'); nltk.download('averaged_perceptron_tagger');nltk.download('wordnet')
   
from nltk.stem import WordNetLemmatizer    
    
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier

#import model
tweets = pd.read_csv("tweet_data.csv")

#drop useless column
tweets.drop("Unnamed: 0", axis=1, inplace=True)

#set stopwords
stop = nltk.corpus.stopwords.words("english")
other_exclusions = ["#ff", "ff", "rt"]
stop.extend(other_exclusions)

#define function to clean tweets
def  clean_text(tweets, text_field):
    tweets["tweet"] = tweets["tweet"].str.lower()
    tweets["tweet"] = tweets["tweet"].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?|rt|amp|\d+", "", elem)) 
    tweets["tweet"] = tweets["tweet"].apply(lambda elem: re.sub(r'\s+|\s+[a-zA-Z]\s+',' ', elem))
    return tweets

#clean tweets
tweet_clean = clean_text(tweets, "tweet")

#define X and y
X = tweet_clean['tweet']
y = tweet_clean['class'].astype(int)

#lemmatize the text
X = [''.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]',' ',text)) for text in lis]) for lis in X]

#create train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#create a sci-kit learn pipeline with a Random Forest
pipeline_randomF = Pipeline([
    ('vect', CountVectorizer(max_features=1500, stop_words=stop)),
    ('tfidf',  TfidfTransformer()),
    ('nb', RandomForestClassifier(n_estimators=150, random_state=0)),
])

#the model
model = pipeline_randomF.fit(X_train, y_train)

#serializing our model 
pickle.dump(model, open('RF_tweet_clas.pkl','wb'))



