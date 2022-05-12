from flask import Flask, jsonify
from requests import request
from flask import request
import pickle
import numpy as np


model = pickle.load(open('model3.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def kideny():
    return "Kideny disease predictions"

@app.route('/kid',methods=["POST"])
def kideny():
    age =request.form.get(' age ')
    bp=request.form.get('bp')
    al=request.form.get('al')
    pcc=request.form.get('pcc')
    bgr=request.form.get('bgr')
    bu=request.form.get('bu')
    sc=request.form.get('sc')
    hemo =request.form.get('hemo')
    pcv =request.form.get('pcv')
    htn =request.form.get('htn')
    dm =request.form.get('dm')
    appet =request.form.get('appet')
    

    input_query=np.array([[age,bp,al,pcc,bgr,bu,sc,hemo,pcv,htn,dm,appet]])

    result =model.predict(input_query)[0]


   # result ={'Pregnancies':Pregnancies,'Glucose':Glucose,'BloodPressure':BloodPressure,'SkinThickness':SkinThickness,'Insulin':Insulin,'BMI':BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age':Age}

    return jsonify({'person is ':str(result)})






if __name__=='__main__':
    app.run(debug=True)