# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 00:55:10 2023

@author: Afroz
"""

import markdown
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns


st.title("Iris Flower Classifier") 
st.markdown('Use this Streamlit app to make your own scatterplot about Iris Flower') 
 
selected_x_var = st.selectbox('What do want the x variable to be?', 
  ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']) 
selected_y_var = st.selectbox('What about the y?', 
  ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']) 

# Import Data
st.title("Iris flower Classifier") 
Iris = pd.read_csv('Iris.csv')

sns.set_style('darkgrid')
markers = {"Iris-setosa": "X", "Iris-versicolor": "s", "Iris-virginica":'o'}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = Iris, x = selected_x_var, 
  y = selected_y_var, hue = 'Species', markers = markers,
  style = 'Species') 
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig) 
