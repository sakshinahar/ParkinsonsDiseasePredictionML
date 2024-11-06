# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:28:41 2022

@author: sradi
"""

import numpy as np
import pickle
import streamlit as st
import time



#load the saved model
load_model = pickle.load(open('C:/Users/sradi/Desktop/Parkinsons using svm/trained_model.sav','rb'))

#creating a function
def parkinsons_prediction(input_data):
    
    #input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the data
    #std_data = scaler.transform(input_data_reshaped)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
      return'The Person does not have Parkinsons Disease'

    else:
      return'The Person has Parkinsons'

def parkinsons_predictions(input_data):
    
    #input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the data
    #std_data = scaler.transform(input_data_reshaped)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
      return'The Person does not have Parkinsons Disease'

    else:
      return'The Person has Parkinsons'

def main():
    #Giving a title
    st.title('Parkinsons Prediction')
    
    #getting the binut data from the user
    
    #name = st.text_input('ASCII subject name and recording number')
    MDVP_Fo_in_Hz = st.text_input('Average vocal fundamental frequency')
    MDVP_Fhi_Hz = st.text_input('Maximum vocal fundamental frequency')
    MDVP_Flo_in_Hz = st.text_input('Minimum vocal fundamental frequency')
    MDVP_Jitter_in_percentage = st.text_input(' Several measures of variation in fundamental frequency')
    MDVP_Jitter_in_Abs = st.text_input(' Several measures of variation in fundamental frequency 1')
    MDVP_RAP = st.text_input(' Several measures of variation in fundamental frequency 2')
    MDVP_PPQ = st.text_input(' Several measures of variation in fundamental frequency 3')
    Jitter_DDP = st.text_input(' Several measures of variation in fundamental frequency 4')
    MDVP_Shimmer = st.text_input(' Several measures of variation in amplitude 5')
    MDVP_Shimmer_in_dB = st.text_input(' Several measures of variation in amplitude 6')
    Shimmer_APQ3 = st.text_input(' Several measures of variation in amplitude 7')
    Shimmer_APQ5 = st.text_input(' Several measures of variation in amplitude 8')
    MDVP_APQ = st.text_input(' Several measures of variation in amplitude 9')
    Shimmer_DDA = st.text_input(' Several measures of variation in amplitude 10')
    NHR = st.text_input(' Two measures of the ratio of noise to tonal components in the voice 11')
    HNR = st.text_input(' Two measures of the ratio of noise to tonal components in the voice 12')
    RPDE = st.text_input(' Two nonlinear dynamical complexity measures 13')
    D2 = st.text_input(' Two nonlinear dynamical complexity measures 14')
    DFA = st.text_input(' Signal fractal scaling exponent 15')
    spread1 = st.text_input(' Three nonlinear measures of fundamental frequency variation 16')
    spread2 = st.text_input(' Three nonlinear measures of fundamental frequency variation 17')
   # PPE = st.text_input(' Three nonlinear measures of fundamental frequency variation 18')
    PPE= st.selectbox( 'How would you like to be contacted?',('1', '0', ' 1.23'))
    
    #code for prediction
    diagnosis = ''
    diagnosiss = ''
    my_bar = st.progress(0)    
    #creating a button for prediction
    if st.button("Parkinsons Test Result"):
        for percent_complete in range(100):
            time.sleep(0.000009)
            my_bar.progress(percent_complete + 1)
        diagnosis = parkinsons_prediction([MDVP_Fo_in_Hz, MDVP_Fhi_Hz, MDVP_Flo_in_Hz, MDVP_Jitter_in_percentage, MDVP_Jitter_in_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_in_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, D2, DFA, spread1, spread2, PPE])
        diagnosiss = parkinsons_predictions([MDVP_Fo_in_Hz, MDVP_Fhi_Hz, MDVP_Flo_in_Hz, MDVP_Jitter_in_percentage, MDVP_Jitter_in_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_in_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, D2, DFA, spread1, spread2, PPE])

    st.success(diagnosis) 
    st.success(diagnosiss)
    
if __name__ == '__main__':
    main()
    
    