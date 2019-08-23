from flask import Flask, render_template, url_for, request
import pickle
#from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	#deserialisation
	model = pickle.load(open('RF_tweet_clas.pkl','rb'))

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = model.predict(data)[0]
	return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=12345)
