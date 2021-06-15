# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:09:36 2021

@author: nehal
"""

from flask import Flask ,request
import pickle 
import pandas as pd

my_model=pickle.load(open('full_pipeline','rb'))

app=Flask(__name__)
#Default Address of app
@app.route('/')  

def hello():
    return 'Lets Explore Flask'



@app.route('/predict')
def pred():
    
    # To statically input value
    # http://127.0.0.1:5000/predict?age=50&sex=0&cp=0&trestbps=110&chol=254&fbs=0&restecg=0&thalach=159&exang=0&oldpeak=0&slope=2&ca=0&thal=2
    
    age=int(request.args.get('age'))
    sex=int(request.args.get('sex'))
    cp=int(request.args.get('cp'))
    trestbps=int(request.args.get('trestbps'))
    chol=int(request.args.get('chol'))
    fbs=int(request.args.get('fbs'))
    restecg=int(request.args.get('restecg'))
    thalach=int(request.args.get('thalach'))
    exang=int(request.args.get('exang'))
    oldpeak=int(request.args.get('oldpeak'))
    slope=int(request.args.get('slope'))
    ca=int(request.args.get('ca'))
    thal=int(request.args.get('thal'))
    
     

    test=pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]])
    test.columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']  
    
    y_pred=my_model.predict(test)
    
    return 'Probability of heart attack:'+str(y_pred)

if __name__=='__main__':
    app.run()
    
   


    
   
