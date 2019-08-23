from flask import Flask, render_template, url_for, request
import pickle
from sklearn.externals import joblib

# #import dependencies
# import pandas as pd
# import re

# import nltk
# nltk.download('stopwords'); from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize 
# nltk.download('punkt'); nltk.download('averaged_perceptron_tagger');nltk.download('wordnet')
   
# from nltk.stem import WordNetLemmatizer    
    
# from sklearn.utils import resample
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.ensemble import RandomForestClassifier

# import seaborn as sns
# import matplotlib.pyplot as plt

# from sklearn.metrics import confusion_matrix

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	#deserialisation
	#create the .pkl file (already provided in repository)
	RF_tweet_clas = open('RF_tweet_clas.pkl','rb')
	model = joblib.load(RF_tweet_clas)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = model.predict(data)[0]
	return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=12345)
