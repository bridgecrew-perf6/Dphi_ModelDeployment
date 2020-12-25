import numpy as np
from flask import Flask, request, jsonify, render_template
import utils

app = Flask(__name__, template_folder='template',static_folder='template')
# Code to load ML model

@app.route('/')
def home():    
    if request.method=="GET":
        return render_template("index.html")

@app.route('/predict_loan', methods=['POST'])
def predict_loan():
    appincome = int(request.form['appincome'])
    coappincome = int(request.form['coappincome'])
    loanamount = int(request.form['loanamount'])
    loanterm = int(request.form['loanterm'])
    gender = request.form['gender']
    married = request.form['married']
    education = request.form['education']
    self_employed = request.form['self_employed']
    dependents = request.form['dependents']
    credit_history = int(request.form['credit_history'])
    property_area= request.form['property_area']
    pred = utils.get_prediction(gender, married, dependents, education, self_employed, appincome, coappincome, loanamount, loanterm, credit_history, property_area)
    if pred == 1:
        res = 'YES ! Nice! Probably you get Loan!'
        alert = 'alert alert-success'
    else:
        res = 'Sorry! ): Probably you do not get the Loan'
        alert = 'alert alert-danger'
    response = jsonify({
        'result': res,
        'alert' : alert
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


    
if __name__ == '__main__':
     app.run(debug = True)
