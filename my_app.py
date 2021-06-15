# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:08:44 2021

@author: Senthil
"""

import flask
import pickle
import pandas as pd


my_model=pickle.load(open('full_pipeline','rb'))

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        
    

        age=int(flask.request.form['age'])
        sex=int(flask.request.form['sex'])
        cp=int(flask.request.form['cp'])
        trestbps=int(flask.request.form['trestbps'])
        chol=int(flask.request.form['chol'])
        fbs=int(flask.request.form['fbs'])
        restecg=int(flask.request.form['restecg'])
        thalach=int(flask.request.form['thalach'])
        exang=int(flask.request.form['exang'])
        oldpeak=int(flask.request.form['oldpeak'])
        slope=int(flask.request.form['slope'])
        ca=int(flask.request.form['ca'])
        thal=int(flask.request.form['thal'])
     
        # Make DataFrame for model
        test=pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]],
                          columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                                   'exang', 'oldpeak', 'slope', 'ca', 'thal'],
                          dtype=int,
                          index=['input'])
        
    
        y_pred=my_model.predict(test)
    
        return flask.render_template('main.html',
                                     original_input={'Age':age,
                                                     'sex':sex, 
                                                     'cp':cp, 
                                                     'trestbps':trestbps, 
                                                     'chol':chol, 
                                                     'fbs':fbs, 
                                                     'restecg':restecg, 
                                                     'thalach':thalach,
                                                     'exang':exang, 
                                                     'oldpeak':oldpeak, 
                                                     'slope':slope, 
                                                     'ca':ca, 
                                                     'thal':thal
                                                     
                                                     
                                                     
                                                     
                                                     },
                                     
                                     result=str(y_pred)
                                     )


if __name__ == '__main__':
    app.run()
