# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        systolic = int(request.form['systolic'])
        cholestrol = int(request.form['cholestrol'])
        is_smoke = request.form['smoke']
        if (is_smoke=='yes'):
            smoke=1
        else:
            smoke=0
        filename = '/Users/tanvirislamullash/PycharmProjects/Cardio Vascular Disease/cardiovascular_model.pickle'
        classifier = pickle.load(open(filename, 'rb'))
        
        # data = np.array([[age, systolic, cholestrol, smoke]])
        my_prediction = classifier.predict([[age, systolic, cholestrol, smoke]])
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8001,debug=True)
	#app.run(debug=True)