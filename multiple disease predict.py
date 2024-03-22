# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:22:02 2024
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/amerp/OneDrive/Desktop/multiple disease predictive system/savedmodels/diabetes_model.sav','rb'))
heart_model = pickle.load(open('C:/Users/amerp/OneDrive/Desktop/multiple disease predictive system/savedmodels/heartdisease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/amerp/OneDrive/Desktop/multiple disease predictive system/savedmodels/parkinsons_model.sav','rb'))


#sidebar
with st.sidebar:
    selected = option_menu('Multiple Disese Predictive System', 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           
                           default_index=0)
    
#diabetyes page
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the Person")
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating button prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeeFunction,Age]])
        if (diab_prediction[0] ==1):
            diab_diagnosis = 'The Person Is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
            
    st.success(diab_diagnosis)
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3 =st.columns(3)
    with col1:
        age =st.text_input("Age")
    with col2:
        sex=st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest pain types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum cholestrol in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting electrocardiac results")
    with col2:
        thalach = st.text_input("Maximum heart rate achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels coloured by fluorosopy")
    with col1:
        thal = st.text_input("thal:0 = normal; 1= fixed defect; 2= reverse defect")
        
        
    heart_diagnosis= ""
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0]==1):
            heart_diagnosis = "The personn is having heart disease"
        else:
            heart_diagnosis="The person is not having heart disease"
    st.success(heart_diagnosis)
    
    
    
    
    
if (selected== 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        fo =st.text_input("MDVP: FO(Hz)")
    with col2:
        fhi =st.text_input("fhi(Hz)")
    with col3:
        flo =st.text_input("flo(Hz)")
    with col4:
        Jitter_percent =st.text_input("Jitter(%)")
    with col5:
        Jitter_Abs =st.text_input("Jitter(Abs)")
    with col1:
        RAP =st.text_input("RAP")
    with col2:
        PPQ =st.text_input("PPQ")
    with col3:
        DDP =st.text_input("DDP")
    with col4:
        Shimmer =st.text_input("Shimmer")
    with col5:
        Shimmer_db =st.text_input("Shimmer_db")
    with col1:
        APQ3 =st.text_input("Shimmer:APQ3")
    with col2:
        APQ5 =st.text_input("Shimmer:APQ5")
    with col3:
        APQ=st.text_input("MDVP:APQ")
    with col4:
        DDA = st.text_input("Shimmer : DDA")
    with col5:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1= st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE =st.text_input("PPE")
    
    parkinsons_diagnosis=""
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction= parkinsons_model.predict([[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis="The person has parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)
    