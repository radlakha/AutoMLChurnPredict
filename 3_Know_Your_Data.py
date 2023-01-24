# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 17:48:08 2023

@author: sbhadwal
"""

import streamlit as st
from pycaret.classification import *
import os 
import pandas as pd

path = 'C:/Users/sbhadwal/sol1/streamapp/data_mod'
dir_list = os.listdir(path)
st.title("Visualiziation and Simple Statistics")
path_final = path + "/" + dir_list[0]
data = pd.read_csv(path_final) 
cols = list(data.columns)

st.write("Simple Statistics on Your Data")
data_stat = data.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
st.write(data_stat)
target = st.session_state.target
# st.write(st.session_state) Debugging

#count = st.selectbox("Distribution of", cols, key='count')

cols2 = list(data_stat.columns)
choice = st.selectbox("Count Distribution of", cols2)

