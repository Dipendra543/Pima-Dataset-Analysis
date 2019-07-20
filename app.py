# Define a python framework for a REST API for diabetic prediction

from machinelearning import MachineLearning
from send_sms import send_sms

import pickle
import pandas as pd
from flask import Flask, request, render_template

trained_models = None
loaded_models = None  # Model Loaded from the pickle files
app = Flask(__name__)


@app.route('/trainmodel', methods=['POST'])
def train_model():
    if request.method == 'POST':
        success_status = True
        global trained_models
        ml_model = MachineLearning('./data/diabetes.csv')
        ml_model.svm()
        ml_model.logistic_regression()
        ml_model.decision_tree()
        ml_model.persist_model()  # This line will save the pickle files to the ./output/ directory
        trained_models = ml_model.filenames

        return render_template("trainmodels.html", success_status=success_status, trained_models=trained_models)


def get_model(type_to_learn):
    global loaded_models
    filename = './output/'+type_to_learn+'.pkl'
    #print(filename)
    with open(filename, 'rb') as f:
        loaded_models = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def get_prediction():
    if request.method == 'POST':
        output_values = ["Non-Diabetic", "Diabetic"]
        data = request.form
        data = dict(data)
        type_to_learn = data.pop("types_to_learn", None)
        get_model(type_to_learn)
        # print(data, types_to_learn)
        data = pd.DataFrame(data, index=[0])
        prediction = loaded_models.predict(data)
        prediction_string = str(output_values[prediction[0]])
        return_str = f'The Prediction is: {prediction_string}'
        send_sms(prediction_string, type_to_learn)
    return return_str


if __name__ == "__main__":
    # get_model()
    app.run(host="0.0.0.0")
