from flask import Flask, render_template, request
import numpy as np
import os
import pickle

app = Flask(__name__, template_folder="Front-End")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about-page.html")


@app.route('/predict')
def predict():
    return render_template('input-page.html')


@app.route("/result", methods=['POST', 'GET'])
def result():
    gender = int(request.form['gender'])
    age = int(request.form['age'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    ever_married = int(request.form['ever_married'])
    work_type = int(request.form['work_type'])
    Residence_type = int(request.form['Residence_type'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = int(request.form['smoking_status'])

    trans = np.array([gender, age, hypertension, heart_disease, ever_married, work_type,
                  Residence_type, avg_glucose_level, bmi, smoking_status]).reshape(1, -1)

    scaler_file = os.path.join('ML-Models/scaler.pkl')

    with open(scaler_file, 'rb') as scaler_pkl:
        scaler = pickle.load(scaler_pkl)

    trans = scaler.transform(trans)

    model_file = os.path.join('ML-Models/model.pkl')
    
    with open(model_file, 'rb') as model_pkl:
        model = pickle.load(model_pkl)

    pred = model.predict(trans)

    return render_template('result-page.html', result=pred[0])


@app.route("/article")
def article():
    return render_template("artikel-page.html")


@app.route("/article_detail", methods=['GET'])
def article_detail():
    return render_template("artikel-detail.html")


if __name__ == "__main__":
    app.run(debug=True, port=7456)
