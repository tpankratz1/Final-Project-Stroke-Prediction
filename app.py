import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
cols=['factor1','factor2','factor3','factor4']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    feature_list = list(map(int, feature_list))
    final_features = np.array(feature_list).reshape(1, 10) 
    
    prediction = model.predict(final_features)
    int(prediction[0])

    return render_template('index.html', prediction_text='Effect on Mortality per 100,000 people with updates: {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)