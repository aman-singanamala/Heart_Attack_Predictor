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
Resting_BP = st.slider("Please Input Your Resting Blood Pressure",110,200)
Cholesterol= st.slider("Please Input Your Cholestrol Level",100,500)
Fasting = st.slider("If you fast Select 1 . If You Dont Select 0",0,1)
HeartRate = st.slider("Input Your Input Heart Rate",45,220)
OLD_PEAK=st.slider("Input Your Old Peak",0.0,4.0)
SEX = st.slider("1 For Male - 0 For Female",0,1)
ChestPainType_ASY = st.slider(" ChestPainType_ASY :  1 For Yes - 0 For No",0,1)
ChestPainType_ATA = st.slider(" ChestPainType_ATA :  1 For Yes - 0 For No",0,1)
ChestPainType_TA = st.slider("ChestPainType_TA    :  1 For Yes - 0 For No",0,1)
RestingECG_LVH = st.slider("RestingECG_LVH        :  1 For Yes - 0 For No",0,1)
RestingECG_ST = st.slider("RestingECG_ST          :  1 For Yes - 0 For No",0,1)
ExerciseAngina_Y = st.slider("ExerciseAngina_Y    :  1 For Yes - 0 For No",0,1)
ST_Slope_Down = st.slider("ST_Slope_Down1         :  1 For Yes - 0 For No",0,1)
ST_Slope_Up = st.slider("ST_Slope_Up              :  1 For Yes - 0 For No",0,1)

inputs=[[Age, Resting_BP, Cholesterol, Fasting, HeartRate,OLD_PEAK,
       SEX, ChestPainType_ASY, ChestPainType_ATA,
       ChestPainType_TA, RestingECG_LVH, RestingECG_ST,
       ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Up]]

if st.button('Predict'):
    result=model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
        st.write("Sorry , Your Heart is not healthy, Reach your Doctor for a Checkup")
    else:
        st.write("You are Safe now. But take care of your Health.")

if __name__ =='__main__':
    main()