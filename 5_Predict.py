# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:20:55 2023

@author: sbhadwal
"""
from pycaret.classification import load_model, predict_model
import streamlit as st
import os
import pandas as pd

st.title("Predict Online")  #Prediction Page

model = load_model('deployment_28042020')  #Loading the saved model

path = 'C:/Users/sbhadwal/sol1/streamapp/data_mod' #Defining path
dir_list = os.listdir(path)
path_final = path + "/" + dir_list[0]

target1 = st.session_state.tkey
target1 = str(target1)
#Debugging
# st.write(target1)
# st.write(type(target1))

data = pd.read_csv(path_final) #Reading the data into a datframe
cols = list(data.columns) #Lisitng all the columns
cols.remove(target1)
data_stat = data.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
#Table for statistics


def predict(model, input_df): #Function to predict from trained model
    predictions_df = predict_model(estimator=model, data = input_df) #Pycaret function
    predictions = predictions_df['Label'][0] #Label
    score = predictions_df['Score'][0] #Probability score
    return predictions, score

#Segregating columns based on their datatypes
object_columns = data.select_dtypes(include=['object']).columns #Columns with string dtype
cols2 = list(data_stat.columns) #All the numeric columns
cols2.remove(target1) #Making sure columns are in the same order

input_dict = {} #Creating an empty dictionary to store the variables. 

for b in object_columns: #For string dtype
    unique_vals = data[b].unique().tolist() #Mostly categorical, thus dropdown
    m = st.selectbox(b,unique_vals) #Display the selectbox.
    input_dict[b]=m #Adding the option selected for a particular varible in the list

#Number input for numeric columns, default value is the mean of the variable    
for a in cols2:
    m = st.number_input(a, value = float(data_stat.loc['mean'][a]))
    input_dict[a]=m #Adding the value selected for a particular variable in the dict. 

input_df = pd.DataFrame([input_dict]) #Converting dictionary into dataframe
input_df = input_df.loc[:,cols] #Rearranging the columns so that they match the original dataframe
# st.write(input_df) Debugging
output = ""

if st.button("Predict"): #Predict Button
    prediction, score = predict(model = model, input_df = input_df) #Calling the predict function
    
    if prediction==1:
        st.write("Customer at high risk of churn")
        st.write("Model Confidence: ")
        st.write(score)
    else:
        st.write("Customer at low risk of churn")
        st.write("Model Confidence: ")
        st.write(score)