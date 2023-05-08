import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import joblib

# Load the model 
model = joblib.load(open('LinReg.pkl', 'rb'))

st.title('Heart Rate Test')
st.header('Built by Gomycode Scion')


st.write('Pls register your name for record of usage')
username = st.text_input('Enter your name')
if st.button('Submit name'):
    st.success(f'Welcome {username}. please use according to usage guidelines')

picture = st.sidebar.camera_input('position your face to use the webcam')

if picture:
    picture = st.sidebar.image(picture)

input_type = st.sidebar.selectbox('choose your preferred input type', ['Number Input', 'Slider'])

if input_type == 'Number Input':
    biking = st.sidebar.number_input('Biking', 1.1, 75.0, 38.0)
    smoking = st.sidebar.number_input('Smoking', 0.5, 30.0, 15.4)
else:
    biking = st.sidebar.slider('Biking', 1.1,75.0,38.0)
    smoking = st.sidebar.slider('Smoking', 0.5,30.0, 15.4)

input_values = {'biking': biking,
                'smoking': smoking}
input_df = pd.DataFrame(input_values, index=[0])

st.write('This is your inputted Data')
st.table(input_df)
# testing the model
prediction = model.predict(input_df)

if st.button('Predict'):
    input_df['Heart Rate'] = prediction
    st.table(input_df)
