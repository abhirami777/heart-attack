import streamlit as st
import pandas as pd
st.title('heart attack')
age = st.number_input("Enter your age",value=0,key=0)
gender = st.number_input("Enter your gender",value=0,key=1)
impluse = st.number_input("Enter your impulse ",value=0,key=2)
pressurehight = st.number_input("Enter your high pressue",value=0,key=3)
pressurelow = st.number_input("Enter your low pressure",value=0,key=4)
glucose = st.number_input("Enter your glucose",value=0,key=5)
kcm = st.number_input("Enter your kcm",value=0,key=6)
troponin = st.number_input("Enter your troponin",value=0,key=7)

test = pd.DataFrame({'age':age,'gender':gender,
                     'impluse':impluse,
                     'pressurehight':pressurehight,
                     'pressurelow ':pressurelow ,
                     'glucose':glucose,
                     'kcm':kcm,'troponin':troponin},index=[0])

import pickle
model = pickle.load(open("C:\\Users\\DELL\\Downloads\\Heart Attack.pkl",'rb'))
st.write(model.predict(test))
