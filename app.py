import streamlit as st
import numpy as np
import string
import pickle
from sklearn.svm import SVC
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model.pkl','rb'))
def main():
    st.sidebar.header("Heart Attack Risk Prediction")
    st.sidebar.header("Just fill in the information below")
    st.sidebar.text("Support Vector Machine Classifier")
    
Age = st.slider("Please Input Your Age ", 10, 100)
Blood_Pressure= st.slider("Please Input Your Resting Blood Pressure",110,200)









if __name__ =='__main__':
    main()