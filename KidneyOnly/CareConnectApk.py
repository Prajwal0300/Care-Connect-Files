# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:09:03 2023

@author: prajw
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/prajw/OneDrive/Desktop/CareConnect/Saved Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/prajw/OneDrive/Desktop/CareConnect/Saved Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/prajw/OneDrive/Desktop/CareConnect/Saved Models/parkinsons_model.sav', 'rb'))

sarcoidosis_model = pickle.load(open('C:/Users/prajw/OneDrive/Desktop/CareConnect/Saved Models/sarcoidosis_model.sav', 'rb'))

kidney_model =  pickle.load(open('C:/Users/prajw/OneDrive/Desktop/CareConnect/Saved Models/kidney_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:

    selected = option_menu('CARE CONNECT',

                          ['Home Page',
                           'CKD Prediction',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Sarcoidosis Prediction'],
                          icons=['house','person','activity','heart','person','star'],
                          default_index=0)

# Home Page
if selected == 'Home Page':
    st.title('Welcome to CARE CONNECT')

    # About Section
    st.header('About')
    st.write('This is the CARE CONNECT application, a platform for medical predictions using Machine Learning.')
    st.write('Select an option from the sidebar to make predictions for different medical conditions.')

    # Models with Accuracy of Prediction Table
    st.header('Models with their Accuracy of Prediction')
    st.write('Below is the table containing models and their accuracy of prediction.')

    import pandas as pd

    # Create a table to display model information with custom headers and content
    model_info_table = []

    # Add rows to the table with user-defined content
    model_info_table.append(["Disease Name", "Model Type", "Accuracy"])
    model_info_table.append(["Disease 2", "Type of Model 2", "Accuracy 2"])
    model_info_table.append(["Disease 3", "Type of Model 3", "Accuracy 3"])
    model_info_table.append(["Disease 4", "Type of Model 4", "Accuracy 4"])

    # Create a DataFrame from the table data
    df = pd.DataFrame(model_info_table)

    # Set the first row as column headers and remove the row names
    df.columns = df.iloc[0]
    df = df[1:]

    # Display the table
    st.table(df)

    st.write('Add more information...')





# CKD Prediction Page
if (selected == 'CKD Prediction'):

    # page title
    st.title('CKD Prediction using ML')


    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Enter the Age')

    with col2:
        bp = st.text_input('Blood Pressure')

    with col3:
        sg = st.text_input('Specific Gravity')

    with col4:
        al = st.text_input('Albumin')

    with col1:
        su = st.text_input('Sugar')

    with col2:
        rbc = st.text_input('Red Blood Cells')

    with col3:
        pc = st.text_input('Pus Cell')

    with col4:
        pcc = st.text_input('Pus Cell Clumps')

    with col1:
        ba = st.text_input('Bacteria')

    with col2:
        bgr = st.text_input('Blood Glucose Random')

    with col3:
        bu = st.text_input('Blood Urea')

    with col4:
        sc = st.text_input('Serum Creatinine')

    with col1:
        sod = st.text_input('Sodium')

    with col2:
        pot = st.text_input('Potassium')

    with col3:
        hemo = st.text_input('Hemoglobin')

    with col4:
        pcv = st.text_input('Packed Cell Volume')

    with col1:
        wc = st.text_input('White Blood Cell Count')

    with col2:
        rc = st.text_input('Red Blood Cell Count')

    with col3:
        htn = st.text_input('Hypertension')

    with col4:
        dm = st.text_input('Diabetes Mellitus')

    with col1:
        cad = st.text_input('Coronary Artery Disease')

    with col2:
        appet = st.text_input('Appetite')

    with col3:
        pe = st.text_input('Pedal Edema')

    with col4:
        ane = st.text_input('Anemia')


    # code for Prediction
    ckd_diagnosis = ''

    # creating a button for Prediction

    if st.button('CKD Test Result'):
        ckd_prediction = kidney_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])

        if (ckd_prediction[0] == 0):
          ckd_diagnosis = 'The person has CKD'
        else:
          ckd_diagnosis = 'The person dose not have CKD'

    st.success(ckd_diagnosis)









# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')




    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)




# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')



    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)






# Sarcoidosis Prediction Page
if (selected == 'Sarcoidosis Prediction'):

    # page title
    st.title('Sarcoidosis Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Sex = st.text_input('Sex (0=male 1=female)')

    with col2:
        Histology = st.text_input('Histology ( 0=negative, 1=positive) ')

    with col3:
        Xthorax = st.text_input('X-thorax (Scaddinger scale)')

    with col1:
        CT = st.text_input('CT ( 0=negative, 1=positive)')

    with col2:
        SPECT = st.text_input('SPECT (0=negative, 1=positive)')

    with col3:
        SRS = st.text_input('SRS (0=negative, 1=positive)')

    with col1:
        PET = st.text_input('PET (0=negative, 1=positive)')

    with col2:
        lunginvolvement = st.text_input('lunginvolvement (1=yes, 0=no)')

    with col3:
        eyeinvolvement = st.text_input('eyeinvolvement (1=yes, 0=no)')

    with col1:
        neurological = st.text_input('neurological involvement (1=yes, 0=no)')

    with col2:
        skininvovlement = st.text_input('skin invovlement (1=yes, 0=no) ')

    with col3:
        SIL = st.text_input('SIL 2R (in pg/mL)')

    with col1:
        ACE = st.text_input('ACE (in U/ml)')


    # code for Prediction
    sarco_diagnosis = ''

    # creating a button for Prediction

    if st.button('Sarcoidosis Test Result'):
        sarco_prediction = sarcoidosis_model.predict(
            [[Sex, Histology, Xthorax, CT, SPECT, SRS, PET, lunginvolvement, eyeinvolvement, neurological, skininvovlement, SIL, ACE]])

        if (sarco_prediction[0] == 1):
            sarco_diagnosis = 'The person has Sarcoidosis'
        else:
            sarco_diagnosis = 'The person does not have Sarcoidosis'

    st.success(sarco_diagnosis)
