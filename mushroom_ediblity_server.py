import flask
from flask import Flask,render_template,url_for
import pandas as pd 
import numpy as np
import secrets
import os
from mushroom_edibility_form import mushroom_edibility_form1
import joblib

app=Flask(__name__)

app.config['SECRET_KEY']=os.getenv('SECRET_KEY',secrets.token_hex(32))

#load model and standerd scaler
model=joblib.load('mushroom_model.pkl')
scaler=joblib.load('mushroom_scaler.pkl')

@app.route('/',methods=['GET','POST'])

def predict():
    form=mushroom_edibility_form1()
    result_text=None
   
    if form.validate_on_submit():
        data=np.array([[
            form.capDiameter.data,
            form.capShape.data,
            form.gillAttachment.data,
            form.gillColor.data,
            form.stemHeight.data,
            form.stemWidth.data,
            form.stemColor.data,
            form.season.data
        ]])
        print(data)
        scaled_Data=np.array([[form.capDiameter.data,form.stemWidth.data]])
        user_data=scaler.transform(scaled_Data)

        data[0,0]=user_data[0,0]
        data[0,5]=user_data[0,1]        
        print(user_data)
        result=model.predict(data)
        print(result)

        if result[0]==0:
            result_text='Mushroom is edible'
        else:
            result_text='Mushroom is not edible'
    else:
        print('error')
        
    return render_template('mushroom_edibility.html',predict_text=result_text,form=form)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5002)