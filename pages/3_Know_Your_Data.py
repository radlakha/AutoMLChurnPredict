# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 17:48:08 2023

@author: sbhadwal
"""

import streamlit as st
from pycaret.classification import *
import os 
import pandas as pd
import pathlib

parent_path = pathlib.Path(__file__).parent.parent.resolve() #Defining paths.  
path = os.path.join(parent_path, "data_mod")
dir_list = os.listdir(path)
path_final = path + "/" + dir_list[0]

st.title("Visualiziation and Simple Statistics") #Title
data = pd.read_csv(path_final) #Read the data into a dataframe
cols = list(data.columns) #Columns list

st.write("Simple Statistics on Your Data")
data_stat = data.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))) #Describe data
st.write(data_stat) #Display obtained dataframe on screen

