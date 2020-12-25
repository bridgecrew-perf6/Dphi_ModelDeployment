import pickle
import json
import numpy as np
import os
import pandas as pd

__model = None

def load_model():
    global __model
    if __model is None:
        with open('model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print(__model)
    print("loading saved artifacts...done")



def get_prediction(gender, married, dependents, education, self_employed, appincome, coappincome, loanamount, loanterm, credithistory, propertyarea):
    columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    """
    print('IMPRIMO VALOREEEEEEEEE')
    print(gender)
    print(married)
    print(dependents)
    print(education)
    print(self_employed)
    print(type(appincome))
    print(coappincome)
    print(loanamount)
    print(loanterm)
    print(credithistory)
    print(propertyarea)
    """
    data = np.array([gender, married, dependents, education, self_employed, int(appincome), int(coappincome), int(loanamount), int(loanterm), int(credithistory), propertyarea])
    x = pd.DataFrame(data = [data], columns = columns)
    return __model.predict(x)[0]



load_model()
