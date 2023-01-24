# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:58:25 2023

@author: sbhadwal
"""

import os
import pandas as pd
import streamlit as st
from pycaret.classification import *

path = 'C:/Users/sbhadwal/sol1/streamapp/data_mod' #Define path
dir_list = os.listdir(path)
path_final = path + "/" + dir_list[0]
data = pd.read_csv(path_final) 
# st.write(st.session_state) 
target = st.session_state.tkey #Use the target taken from the previous page

st.title("Model Results") #Title
s = setup(data, target = target, html=False, silent=True) #Data preprocessing function of Pycaret
best_model = compare_models() #Compare diff models
model_results = pull() #Pull them to display as a dataframe
st.write(model_results) #Display the table
save_model(best_model, model_name = 'deployment_28042020') #Save the best model