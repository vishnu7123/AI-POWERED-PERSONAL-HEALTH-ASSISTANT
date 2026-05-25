# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 

import streamlit as st
import base64

 # ------------ TITLE 

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:36px;">{"AI powered Health Assistance"}</h1>', unsafe_allow_html=True)


# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('3.jpg')

# ===-------------------------= INPUT DATA -------------------- 


filenamee = st.file_uploader("Choose a Dataset", ['csv'])

if filenamee is None:
    
    st.text("Please Upload Dataset")

else:

    
    dataframe=pd.read_csv("dataset.csv")
        
    print("--------------------------------")
    print("Data Selection")
    print("--------------------------------")
    print()
    print(dataframe.head(15))    
    dataframe = dataframe[0:5000]
    st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{" Data Selection !!!"}</h1>', unsafe_allow_html=True)
    
    
    # st.write("--------------------------------")
    # st.write("Data Selection")
    # st.write("--------------------------------")
    print()
    st.write(dataframe.head(15))    
    
    
     #-------------------------- PRE PROCESSING --------------------------------
    
    #------ checking missing values --------
    st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{" Pre-processing !!!"}</h1>', unsafe_allow_html=True)
    
    print("----------------------------------------------------")
    print("              Handling Missing values               ")
    print("----------------------------------------------------")
    print()
    print(dataframe.isnull().sum())
    
    
    # # st.write("----------------------------------------------------")
    st.write("              Handling Missing values               ")
    st.write("----------------------------------------------------")
    # print()
    st.write(dataframe.isnull().sum())
    
    res = dataframe.isnull().sum().any()
        
    if res == False:
        
        print("--------------------------------------------")
        print("  There is no Missing values in our dataset ")
        print("--------------------------------------------")
        print()    
        
        st.write("--------------------------------------------")
        st.write("  There is no Missing values in our dataset ")
        st.write("--------------------------------------------")
        print()   
        
    else:
    
        print("--------------------------------------------")
        print(" Missing values is present in our dataset   ")
        print("--------------------------------------------")
        print()    
        
        st.write("--------------------------------------------")
        st.write(" Missing values is present in our dataset   ")
        st.write("--------------------------------------------")
        print()   
        
        dataframe = dataframe.fillna(0)
        
        resultt = dataframe.isnull().sum().any()
        
        if resultt == False:
            
            print("--------------------------------------------")
            print(" Data Cleaned !!!   ")
            print("--------------------------------------------")
            print()    
            print(dataframe.isnull().sum())
    
    
    
            st.write("--------------------------------------------")
            st.write(" Data Cleaned !!!   ")
            st.write("--------------------------------------------")
            st.write() 
            
            st.write(dataframe.isnull().sum())
                
      # ---- LABEL ENCODING
            
    print("--------------------------------")
    print("Before Label Encoding")
    print("--------------------------------")   
    
    df_class=dataframe['Disease'].unique
    
    sym1 = dataframe['Symptom_1'].unique()
    
    sym2 = dataframe['Symptom_2'].unique()
    
    sym3 = dataframe['Symptom_3'].unique()
    
    sym4 = dataframe['Symptom_4'].unique()
    
    sym5 = dataframe['Symptom_5'].unique()
    
    sym6 = dataframe['Symptom_6'].unique()
    
    sym7 = dataframe['Symptom_7'].unique()
    
    sym8 = dataframe['Symptom_8'].unique()
    
    
    sym9 = dataframe['Symptom_9'].unique()
    
    sym10 = dataframe['Symptom_10'].unique()
    
    sym11 = dataframe['Symptom_11'].unique()
    
    sym12 = dataframe['Symptom_12'].unique()
    
    sym13 = dataframe['Symptom_13'].unique()
    
        
    print(dataframe['Disease'].head(15))
        
   
    
    
                
    st.write("--------------------------------")
    st.write("Before Label Encoding")
    # st.write("--------------------------------")   
    
    df_class=dataframe['Disease']
    
    st.write(dataframe['Disease'].head(15))
    
    
    label_encoder = preprocessing.LabelEncoder()
        
    dataframe = dataframe.astype(str).apply(label_encoder.fit_transform)
    
    
    print("--------------------------------")
    print("After Label Encoding")
    print("--------------------------------")            
            
    
    print(dataframe['Disease'].head(15))       
    
    
    st.write("--------------------------------")
    st.write("After Label Encoding")
    st.write("--------------------------------")            
            
 
    
    st.write(dataframe['Disease'].head(15))      
    
    
       # ================== DATA SPLITTING  ====================
    
    st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{" Data Splitting !!!"}</h1>', unsafe_allow_html=True)
    
    X=dataframe.drop('Disease',axis=1)
    
    y=dataframe['Disease']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    
    print("---------------------------------------------")
    print("             Data Splitting                  ")
    print("---------------------------------------------")
    
    print()
    
    print("Total no of input data   :",dataframe.shape[0])
    print("Total no of test data    :",X_test.shape[0])
    print("Total no of train data   :",X_train.shape[0])
    
    
    
    st.write("---------------------------------------------")
    st.write("             Data Splitting                  ")
    st.write("---------------------------------------------")
    
    print()
    
    st.write("Total no of input data   :",dataframe.shape[0])
    st.write("Total no of test data    :",X_test.shape[0])
    st.write("Total no of train data   :",X_train.shape[0])
    
    # ================== CLASSIFCATION  ====================
    
    # ------DECISION TREE ------
    
    from sklearn.tree import DecisionTreeClassifier
    
    
    from sklearn import linear_model
    
    dt = DecisionTreeClassifier()
    
    dt.fit(X_train,y_train)
    
    pred_dt = dt.predict(X_test)
    
    
    from sklearn import metrics
    
    acc_hyb = metrics.accuracy_score(pred_dt,y_test) * 100
    
    print("--------------------------------------------------")
    print("Classification - Decision Tree")
    print("--------------------------------------------------")
    
    print()
    
    print("1) Accuracy = ", acc_hyb , '%')
    print()
    print("2) Classification Report")
    print(metrics.classification_report(pred_dt,y_test))
    print()
    print("3) Error Rate = ", 100 - acc_hyb, '%')
    
    # 
    st.write("--------------------------------------------------")
    st.write(" Classification - Decision Tree")
    st.write("--------------------------------------------------")
    
    # print()
    
    st.write("1) Accuracy = ", acc_hyb , '%')
    # print()
    # st.write("2) Classification Report")
    # st.text(metrics.classification_report(pred_lr,y_test))
    # print()
    st.write("3) Error Rate = ", 100 - acc_hyb, '%')
    

    # ------ RNN ------



    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import SimpleRNN, Dense, Flatten
    
    
    with st.spinner("..... RNN Training ......"):
    
    
        model = Sequential()
        model.add(SimpleRNN(64, activation='relu', input_shape=(13,1)))
        model.add(Dense(1, activation='relu'))
        
        
        print('Training...')
        model.compile(loss='mae', optimizer='adam')
        print (model.summary())
        print ('\n')
        
        
        x=np.expand_dims(X_train, axis=2)
        Y=np.expand_dims(y_train,axis=1)
        
        history = model.fit(x,Y, epochs=20, batch_size=1, verbose=1)
    
        loss = history.history['loss']
        loss = min(loss)
    
        acc_rnn = 100 - loss
        
    st.success("Training Completed ...")
    
    print("--------------------------------------------------")
    print("Classification - RNN")
    print("--------------------------------------------------")
    print(f"1) Accuracy = {acc_rnn}%")
    print()
    print(f"2) Error Rate = {100 - acc_rnn}%")

    st.write("--------------------------------------------------")
    st.write("Classification - RNN")
    print("--------------------------------------------------")
    st.write(f"1) Accuracy = {acc_rnn}%")
    print()
    st.write(f"2) Error Rate = {100 - acc_rnn}%")
    
    

    st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{" Prediction !!!"}</h1>', unsafe_allow_html=True)
    
    
    
    
    # ================== PREDICTION  ====================
    
    st.write("-----------------------------------")
    st.write("          Prediction               ")
    st.write("-----------------------------------")
    
    
    # --------------------------
    
    
    
    
    symp11 = {
        0: ' acidity',
        1: ' back_pain',
        2: ' bladder_discomfort',
        3: ' breathlessness',
        4: ' burning_micturition',
        5: ' chest_pain',
        6: ' chills',
        7: ' constipation',
        8: ' continuous_sneezing',
        9: ' cramps',
        10: ' cough',
        11: ' fatigue',
        12: ' high_fever',
        13: ' itching',
        14: ' indigestion',
        15: ' joint_pain',
        16: ' muscle_weakness',
        17: ' muscle_wasting',
        18: ' mood_swings',
        19: ' neck_pain',
        20: ' pain_during_bowel_movements',
        21: ' patches_in_throat',
        22: ' pus_filled_pimples',
        23: ' shivering',
        24: ' skin_rash',
        25: ' stiff_neck',
        26: ' stomach_pain',
        27: ' sunken_eyes',
        28: ' vomiting',
        29: ' weight_gain',
        30: ' weight_loss',
        31: ' weakness_in_limbs',
        32: ' yellowish_skin'
    }
    
    
    symp11_inv = {value.strip(): key for key, value in symp11.items()}
    
    sym1 = list(symp11_inv.keys())
    
    symp1 = st.selectbox("Choose Symptoms 1",sym1)
    
    
    symp1 = symp11_inv.get(symp1, "Status not found")
    
    
    # st.text(symp1)
    
    # -------------
    
    
    
    
    symp21 = {
        0: ' abdominal_pain',
        1: ' acidity',
        2: ' anxiety',
        3: ' blackheads',
        4: ' bladder_discomfort',
        5: ' blister',
        6: ' body_ache',
        7: ' breathlessness',
        8: ' bruising',
        9: ' chills',
        10: ' chest_pain',
        11: ' cold_hands_and_feets',
        12: ' cough',
        13: ' cramps',
        14: ' dehydration',
        15: ' dizziness',
        16: ' fatigue',
        17: ' foul_smell_of urine',
        18: ' high_fever',
        19: ' headache',
        20: ' indigestion',
        21: ' joint_pain',
        22: ' knee_pain',
        23: ' lethargy',
        24: ' loss_of_appetite',
        25: ' mood_swings',
        26: ' nausea',
        27: ' neck_pain',
        28: ' nodal_skin_eruptions',
        29: ' pain_during_bowel_movements',
        30: ' pain_in_anal_region',
        31: ' patches_in_throat',
        32: ' perspiration',
        33: ' pus_filled_pimples',
        34: ' restlessness',
        35: ' skin_peeling',
        36: ' skin_rash',
        37: ' shivering',
        38: ' stiff_neck',
        39: ' stomach_pain',
        40: ' swelling_joints',
        41: ' sweating',
        42: ' ulcers_on_tongue',
        43: ' vomiting',
        44: ' weight_gain',
        45: ' weight_loss',
        46: ' weakness_in_limbs',
        47: ' weakness_of_one_body_side',
        48: ' yellowish_skin'
    }
    
    
    symp21_inv = {value.strip(): key for key, value in symp21.items()}
    
    sym2 = list(symp21_inv.keys())
    
    symp2 = st.selectbox("Choose Symptoms 2",sym2)
    
    
    symp2 = symp21_inv.get(symp2, "Status not found")
    
    
    # st.text(symp2)
    
    
    
    # -------------
    
    symp31 = {
        0: ' abdominal_pain',
        1: ' altered_sensorium',
        2: ' anxiety',
        3: ' blackheads',
        4: ' blister',
        5: ' blood_in_stool',
        6: ' blurred_and_distorted_vision',
        7: ' body_ache',
        8: ' breathlessness',
        9: ' bruising',
        10: ' burning_micturition',
        11: ' chest_pain',
        12: ' chills',
        13: ' cold_hands_and_feets',
        14: ' continuous_feel_of_urine',
        15: ' dark_urine',
        16: ' dehydration',
        17: ' diarrhoea',
        18: ' dischromic_patches',
        19: ' dizziness',
        20: ' extra_marital_contacts',
        21: ' fatigue',
        22: ' foul_smell_of_urine',
        23: ' high_fever',
        24: ' hip_joint_pain',
        25: ' headache',
        26: ' joint_pain',
        27: ' knee_pain',
        28: ' lethargy',
        29: ' loss_of_appetite',
        30: ' loss_of_balance',
        31: ' mood_swings',
        32: ' nausea',
        33: ' neck_pain',
        34: ' nodal_skin_eruptions',
        35: ' obesity',
        36: ' pain_in_anal_region',
        37: ' red_sore_around_nose',
        38: ' restlessness',
        39: ' scurring',
        40: ' silver_like_dusting',
        41: ' skin_peeling',
        42: ' spinning_movements',
        43: ' stomach_pain',
        44: ' sweating',
        45: ' swelling_joints',
        46: ' swelling_of_stomach',
        47: ' vomiting',
        48: ' weight_loss',
        49: ' yellowish_skin'
    }
    
    symp31_inv = {value.strip(): key for key, value in symp31.items()}
    
    
    sym3 = list(symp31_inv.keys())
    
    
    symp3 = st.selectbox("Choose Symptoms 3",sym3)
    
    
    symp3 = symp31_inv.get(symp3, "Status not found")
    
    
    # st.text(symp3)
    
    # -------------
    
    
    
    symp41 = {
        0: ' abdominal_pain',
        1: ' altered_sensorium',
        2: ' blurred_and_distorted_vision',
        3: ' bloody_stool',
        4: ' burning_micturition',
        5: ' chest_pain',
        6: ' continuous_feel_of_urine',
        7: ' cough',
        8: ' dark_urine',
        9: ' diarrhoea',
        10: ' dischromic_patches',
        11: ' dizziness',
        12: ' excessive_hunger',
        13: ' extra_marital_contacts',
        14: ' fatigue',
        15: ' family_history',
        16: ' high_fever',
        17: ' hip_joint_pain',
        18: ' irregular_sugar_level',
        19: ' irritation_in_anus',
        20: ' lack_of_concentration',
        21: ' lethargy',
        22: ' loss_of_appetite',
        23: ' loss_of_balance',
        24: ' mood_swings',
        25: ' nausea',
        26: ' obesity',
        27: ' painful_walking',
        28: ' passage_of_gases',
        29: ' red_sore_around_nose',
        30: ' restlessness',
        31: ' scurring',
        32: ' silver_like_dusting',
        33: ' small_dents_in_nails',
        34: ' spinning_movements',
        35: ' sweating',
        36: ' swollen_legs',
        37: ' swelling_joints',
        38: ' swelling_of_stomach',
        39: ' weight_loss',
        40: ' yellow_crust_ooze',
        41: ' yellowish_skin',
        42: ' yellowing_of_eyes',
        43: ' watering_from_eyes'
    }
    
    
    symp41_inv = {value.strip(): key for key, value in symp41.items()}
    
    sym4 = list(symp41_inv.keys())
    
    symp4 = st.selectbox("Choose Symptoms 4",sym4)
    
    
    symp4 = symp41_inv.get(symp4, "Status not found")
    
    
    # st.text(symp4)
    
    
    # -------------
    
    
    
    
    symp51 = {
        0: ' abdominal_pain',
        1: ' blurred_and_distorted_vision',
        2: ' breathlessness',
        3: ' chest_pain',
        4: ' dark_urine',
        5: ' diarrhea',
        6: ' distention_of_abdomen',
        7: ' dizziness',
        8: ' excessive_hunger',
        9: ' fatigue',
        10: ' family_history',
        11: ' high_fever',
        12: ' history_of_alcohol_consumption',
        13: ' internal_itching',
        14: ' irritation_in_anus',
        15: ' irregular_sugar_level',
        16: ' lack_of_concentration',
        17: ' lethargy',
        18: ' mucoid_sputum',
        19: ' nausea',
        20: ' painful_walking',
        21: ' passage_of_gases',
        22: ' spotting_urination',
        23: ' stiff_neck',
        24: ' sweating',
        25: ' swollen_blood_vessels',
        26: ' swollen_legs',
        27: ' swelling_joints',
        28: ' unsteadiness',
        29: ' yellow_crust_ooze',
        30: ' yellowing_of_eyes',
        31: ' yellowish_skin'
    }
    
    
    symp51_inv = {value.strip(): key for key, value in symp51.items()}
    
    sym5 = list(symp51_inv.keys())
    
    symp5 = st.selectbox("Choose Symptoms 5",sym5)
    
    symp5 = symp51_inv.get(symp5, "Status not found")
    
    # st.text(symp5)
    
    # -------------
    
    symp61 = {
        0: ' abdominal_pain',
        1: ' blurred_and_distorted_vision',
        2: ' breathlessness',
        3: ' chest_pain',
        4: ' constipation',
        5: ' dark_urine',
        6: ' depression',
        7: ' diarrhoea',
        8: ' dizziness',
        9: ' fast_heart_rate',
        10: ' family_history',
        11: ' fluid_overload',
        12: ' headache',
        13: ' high_fever',
        14: ' history_of_alcohol_consumption',
        15: ' inflammatory_nails',
        16: ' internal_itching',
        17: ' loss_of_appetite',
        18: ' malaise',
        19: ' mucoid_sputum',
        20: ' nausea',
        21: ' obesity',
        22: ' painful_walking',
        23: ' puffy_face_and_eyes',
        24: ' prominent_veins_on_calf',
        25: ' swollen_blood_vessels',
        26: ' swelled_lymph_nodes',
        27: ' sweating',
        28: ' stiff_neck',
        29: ' unsteadiness',
        30: ' yellowing_of_eyes',
        31: ' yellowish_skin'
    }
    
    
    symp61_inv = {value.strip(): key for key, value in symp61.items()}
    
    sym6 = list(symp61_inv.keys())
    
    symp6 = st.selectbox("Choose Symptoms 6",sym6)
    
    symp6 = symp61_inv.get(symp6, "Status not found")
    
    # st.text(symp6)
    
    
    
    # -------------
    
    
    symp71 = {
        0: ' abdominal_pain',
        1: ' blurred_and_distorted_vision',
        2: ' breathlessness',
        3: ' constipation',
        4: ' dark_urine',
        5: ' depression',
        6: ' diarrhoea',
        7: ' enlarged_thyroid',
        8: ' excessive_hunger',
        9: ' fast_heart_rate',
        10: ' fluid_overload',
        11: ' headache',
        12: ' irritability',
        13: ' malaise',
        14: ' mild_fever',
        15: ' muscle_pain',
        16: ' nausea',
        17: ' obesity',
        18: ' phlegm',
        19: ' prominent_veins_on_calf',
        20: ' puffy_face_and_eyes',
        21: ' sweating',
        22: ' swelled_lymph_nodes',
        23: ' yellow_urine',
        24: ' yellowing_of_eyes'
    }
    
    symp71_inv = {value.strip(): key for key, value in symp71.items()}
    
    sym7 = list(symp71_inv.keys())
    
    symp7 = st.selectbox("Choose Symptoms 7",sym7)
    
    symp7 = symp71_inv.get(symp7, "Status not found")
    
    
    # -------------
    
    
    symp81 = {
        0: ' abdominal_pain',
        1: ' brittle_nails',
        2: ' chest_pain',
        3: ' diarrhoea',
        4: ' drying_and_tingling_lips',
        5: ' enlarged_thyroid',
        6: ' excessive_hunger',
        7: ' increased_appetite',
        8: ' irritability',
        9: ' loss_of_appetite',
        10: ' malaise',
        11: ' muscle_pain',
        12: ' muscle_weakness',
        13: ' mild_fever',
        14: ' nausea',
        15: ' phlegm',
        16: ' sweating',
        17: ' swelled_lymph_nodes',
        18: ' visual_disturbances',
        19: ' yellow_urine',
        20: ' yellowing_of_eyes'
    }
    
    symp81_inv = {value.strip(): key for key, value in symp81.items()}
    
    sym8 = list(symp81_inv.keys())
    
    symp8 = st.selectbox("Choose Symptoms 8",sym8)
    
    symp8 = symp81_inv.get(symp8, "Status not found")
    
    # -------------
    
    
    symp91 = {
        0: ' abdominal_pain',
        1: ' brittle_nails',
        2: ' chest_pain',
        3: ' diarrhoea',
        4: ' drying_and_tingling_lips',
        5: ' fast_heart_rate',
        6: ' increased_appetite',
        7: ' irritability',
        8: ' malaise',
        9: ' mild_fever',
        10: ' muscle_weakness',
        11: ' pain_behind_the_eyes',
        12: ' phlegm',
        13: ' polyuria',
        14: ' slurred_speech',
        15: ' swollen_extremeties',
        16: ' swelled_lymph_nodes',
        17: ' throat_irritation',
        18: ' toxic_look_(typhos)',
        19: ' visual_disturbances',
        20: ' yellowing_of_eyes'
    }
    
    symp91_inv = {value.strip(): key for key, value in symp91.items()}
    
    sym9 = list(symp91_inv.keys())
    
    symp9 = st.selectbox("Choose Symptoms 9",sym9)
    
    symp9 = symp81_inv.get(symp9, "Status not found")
    
    
    
    # -------------
    
    symp10_1 = {
        0: ' abnormal_menstruation',
        1: ' acute_liver_failure',
        2: ' back_pain',
        3: ' belly_pain',
        4: ' depression',
        5: ' irritability',
        6: ' mild_fever',
        7: ' muscle_pain',
        8: ' pain_behind_the_eyes',
        9: ' polyuria',
        10: ' receiving_blood_transfusion',
        11: ' redness_of_eyes',
        12: ' red_spots_over_body',
        13: ' rusty_sputum',
        14: ' slurred_speech',
        15: ' swollen_extremeties',
        16: ' throat_irritation',
        17: ' fast_heart_rate',
        18: ' toxic_look_(typhos)',
        19: ' yellowing_of_eyes'
    }
    
    symp10_1_inv = {value.strip(): key for key, value in symp10_1.items()}
    
    sym10 = list(symp10_1_inv.keys())
    
    symp10 = st.selectbox("Choose Symptoms 10",sym10)
    
    symp10 = symp10_1_inv.get(symp10, "Status not found")
    
    
    # -------------
    
    
    symp11_1 = {
        0: ' abnormal_menstruation',
        1: ' acute_liver_failure',
        2: ' back_pain',
        3: ' belly_pain',
        4: ' coma',
        5: ' depression',
        6: ' irritability',
        7: ' malaise',
        8: ' muscle_pain',
        9: ' palpitations',
        10: ' receiving_blood_transfusion',
        11: ' receiving_unsterile_injections',
        12: ' redness_of_eyes',
        13: ' red_spots_over_body',
        14: ' rusty_sputum',
        15: ' sinus_pressure',
        16: ' swelled_lymph_nodes',
        17: ' yellowing_of_eyes'
    }
    
    symp11_1_inv = {value.strip(): key for key, value in symp11_1.items()}
    
    sym11 = list(symp11_1_inv.keys())
    
    symp11 = st.selectbox("Choose Symptoms 11",sym11)
    
    symp11 = symp11_1_inv.get(symp11, "Status not found")
    
    
    # -------------
    
    symp12_1 = {
        0: ' abnormal_menstruation',
        1: ' coma',
        2: ' irritability',
        3: ' malaise',
        4: ' muscle_pain',
        5: ' palpitations',
        6: ' receiving_unsterile_injections',
        7: ' runny_nose',
        8: ' sinus_pressure',
        9: ' stomach_bleeding',
        10: ' swelled_lymph_nodes'
    }
    
    symp12_1_inv = {value.strip(): key for key, value in symp12_1.items()}
    
    sym12 = list(symp12_1_inv.keys())
    
    symp12 = st.selectbox("Choose Symptoms 12",sym12)
    
    symp12 = symp12_1_inv.get(symp12, "Status not found")
    
    
    # -------------
    
    
    symp13_1 = {
        0: ' abnormal_menstruation',
        1: ' congestion',
        2: ' malaise',
        3: ' muscle_pain',
        4: ' phlegm',
        5: ' red_spots_over_body',
        6: ' runny_nose',
        7: ' stomach_bleeding'
    }
    
    symp13_1_inv = {value.strip(): key for key, value in symp13_1.items()}
    
    sym13 = list(symp13_1_inv.keys())
    
    symp13 = st.selectbox("Choose Symptoms 13",sym13)
    
    symp13 = symp13_1_inv.get(symp13, "Status not found")
    
    ##################################################################
    
    
    
    butt = st.button("Submit")
    
    if butt:
       predd =  {
            0: 'Acne',
            1: 'AIDS',
            2: 'Alcoholic hepatitis',
            3: 'Allergy',
            4: 'Arthritis',
            5: 'Bronchial Asthma',
            6: 'Cervical spondylosis',
            7: 'Chicken pox',
            8: 'Chronic cholestasis',
            9: 'Common Cold',
            10: ' diabetes ',
            11: 'Dengue',
            12: 'Dimorphic hemorrhoids(piles)',
            13: 'Drug Reaction',
            14: 'Fungal infection',
            15: 'Gastroenteritis',
            16: 'GERD',
            17: 'Heart attack',
            18: 'Hepatitis A',
            19: 'Hepatitis B',
            20: 'Hepatitis C',
            21: 'Hepatitis D',
            22: 'Hepatitis E',
            23: 'Hyperthyroidism',
            24: 'Hypoglycemia',
            25: 'Hypothyroidism',
            26: 'Impetigo',
            27: 'Malaria',
            28: 'Migraine',
            29: 'Osteoarthritis',
            30: 'Paralysis (brain hemorrhage)',
            31: 'Peptic ulcer disease',
            32: 'Psoriasis',
            33: 'Pneumonia',
            34: 'Tuberculosis',
            35: 'Typhoid',
            36: 'Urinary tract infection',
            37: 'Varicose veins',
            38: '(vertigo) Paroxysmal Positional Vertigo'
        }
    
    
        
                
       Data = np.array([symp1, symp2,symp3,symp4,symp5,symp6,symp7,symp8,symp9,symp10,symp11,symp12,symp13]).reshape(1, -1)
    
        
       pred_rf = dt.predict(Data)
       
       pred_rf = int(pred_rf)
       
       # st.text(pred_rf)
       
        
       pred_rf = predd.get(pred_rf, "Status not found")
    
       fin = "Identified Disease = " + str(pred_rf)  
      
       st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{fin}</h1>', unsafe_allow_html=True)
    
      
    
    
    
        
        