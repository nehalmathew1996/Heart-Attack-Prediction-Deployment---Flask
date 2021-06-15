# Heart-Attack-Prediction-Deployment---Flask

## ML-Model-Flask-Deployment
This is a demo project that showcases how a Machine Learn Model is deployed on production environment using Flask API

## Prerequisites to run Files
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

## Project Structure
This project has four major parts :

my_flask.py - This contains code fot our Machine Learning model to predict if someone is likely to suffer from a heart attack or not based on training data in 'heart.csv' file.

app.py - This contains Flask APIs that receives test results through GUI or API calls, computes the precited value based on our model and returns it.

templates - This folder contains the HTML template to allow user to enter his/her report details so as to get a prediction of if someone is likely to suffer from a heart attack or not.

Pickle Files(Pipelines) - 

