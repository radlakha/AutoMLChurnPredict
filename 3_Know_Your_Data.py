# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 17:48:08 2023

@author: sbhadwal
"""

import streamlit as st
from pycaret.classification import *
import os 
import pandas as pd

path = 'C:/Users/sbhadwal/sol1/streamapp/data_mod' #Defining paths
dir_list = os.listdir(path)
path_final = path + "/" + dir_list[0]

st.title("Visualiziation and Simple Statistics") #Title
data = pd.read_csv(path_final) #Read the data into a dataframe
cols = list(data.columns) #Columns list

st.write("Simple Statistics on Your Data")
data_stat = data.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))) #Describe data
st.write(data_stat) #Display obtained dataframe on screen

#Ignore

#target = st.session_state.target
# st.write(st.session_state) Debugging

#count = st.selectbox("Distribution of", cols, key='count')


