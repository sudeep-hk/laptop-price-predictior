import streamlit as st
import pickle

#import the model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
st.title("Laptop Predictor")

#brand
company=st.selectbo