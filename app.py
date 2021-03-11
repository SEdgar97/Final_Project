from flask import request, Flask, jsonify, render_template, redirect, json
import pandas as pd




app = Flask(__name__)

symptoms_df = pd.read_csv('symptom_clean.csv')

@app.route('/')
def hello():
    return render_template('example.html')


@app.route('/get_symptoms')
def page_population():

    symptoms_json = symptoms_df.to_json(orient = 'records')
    print('Hello there')
    return symptoms_json




@app.route('/visualization')
def contact():
    return render_template('visualize.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/diagnose/symptoms=<symptoms>', methods=['POST'])
def diagnosis(symptoms):

    sorted_df = symptoms_df.sort_values('colName', ascending = True)

    model_input = []
    for val in sorted_df['colName']:
        if val in symptoms:
            model_input.append("1")

        else:
            model_input.append("0")

    print(model_input)

    user_symptoms = pd.Series(symptoms)
    user_json = user_symptoms.to_json()


    return user_json


    

if __name__=="__main__":

    app.run(port = 5000)
