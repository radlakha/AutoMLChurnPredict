# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:45:44 2023

@author: sbhadwal
"""

import streamlit as st
import os.path
import pathlib
import pandas as pd

st.title('Manage Your Data')   #Title

st.subheader("Upload File")  #SubHeader

#Widget to upload file
uploaded_file = st.file_uploader("Choose a CSV file", 
                                 type = 'csv', help = 'Should contain data') 

if uploaded_file is not None: #If a file is selected
    
    dataframe = pd.read_csv(uploaded_file)  #Read it into a dataframe
    st.write(dataframe) #Display table on screen
    cols = list(dataframe.columns) #List of all columns in the dataframe
    
    st.subheader("Select Columns to Delete") #Subheader
    
    #Option to delete columns
    st.write("We recommend deleting columns which do not have meaningful data.")
    st.write("\n These might include columns like Name, RowIDs, Customer IDs, Phone Numbers etc.")
    
    #Creating a multiselect widget
    options2 = st.multiselect('Columns to Delete', cols)
    st.session_state.delkey = options2
    #Debuggin session_state: st.write(st.session_state)
    
    cols_exclude = st.session_state.delkey #List of excluded columns
    cols_include = [] #Empty List of intended included columns
    for i in cols:
        if i not in cols_exclude:
            cols_include.append(i) #Appending all the included columns
     
    #Creating a new dataframe which does NOT include the exluded columns        
    dataframe_new = dataframe.loc[:,cols_include] 
    
    st.subheader("Select Target Column")     #Creating a subheading
    #Target variable widget
    option1 = st.selectbox("What do you want to predict?", cols_include, key='target') 
    st.session_state.tkey = option1 #Saving it to session state 
    st.write('You selected:', option1)
    
    st.write(dataframe_new) #Displaying modified dataframe

def upload(): #Function for uploading the data file
    if uploaded_file is None:
        st.session_state["upload_state"] = "Upload a file first!"
        
    else:
        #Defining path variables
        parent_path = pathlib.Path(__file__).parent.parent.resolve()           
        save_path = os.path.join(parent_path, "data")
        complete_name = os.path.join(save_path, uploaded_file.name)
        with open(complete_name,"wb") as f:
            f.write(uploaded_file.getbuffer())  #Wrtitng the file (unmodified)
        
        #Code to save dataframe_new
        save_path2 = os.path.join(parent_path, "data_mod")
        complete_name = os.path.join(save_path2, uploaded_file.name)
        dataframe_new.to_csv(complete_name, index = False)
            
        return st.success("Saved File") 
    
#Option to delete columns to be added
        
st.button("Upload file", on_click=upload) #Call function when clicked on Upload file button.
