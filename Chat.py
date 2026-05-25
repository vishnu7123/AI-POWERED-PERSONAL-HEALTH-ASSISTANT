# ======================== IMPORT PACKAGES ===============================

import streamlit as st

import base64
import numpy as np
import matplotlib.pyplot as plt 
from tkinter.filedialog import askopenfilename

import streamlit as st

import matplotlib.image as mpimg

import streamlit as st
import base64

import pandas as pd
import sqlite3

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
add_bg_from_local('chat.jpg')

# --------

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:30px;">{"Clinical decision support system Using RNN"}</h1>', unsafe_allow_html=True)


# ============== CHATBOT


col1, col2, col3 = st.columns(3)

col4, col5, col6 = st.columns([3,2,1])

clickk=col6.checkbox("CHAT")

speak=col5.checkbox("VOICE")




if clickk:

    a1=st.text_input("Chat Here")
    
    if a1=="Hi" or a1=="hi":
       st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{"Hi! How Can I Help You?"}</h1>', unsafe_allow_html=True)
              
       a2=st.text_input("Chat")
       # 
       if not a2:
           st.warning("Please enter some text!")
       else:
           st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{"Yes Sure, Kindly fill the Below Symptoms"}</h1>', unsafe_allow_html=True)
           
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
        
           symp1 = st.text_input("Enter Symptoms 1")
        
        
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
          
           symp2 = st.text_input("Enter Symptoms 2")
          
          
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
          
          
           symp3 = st.text_input("Choose Symptoms 3")
          
          
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
          
           symp4 = st.text_input("Choose Symptoms 4")
          
          
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
           
           symp5 = st.text_input("Choose Symptoms 5")
          
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
          
           symp6 = st.text_input("Choose Symptoms 6")
          
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
          
           symp7 = st.text_input("Choose Symptoms 7")
          
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
          
           symp8 = st.text_input("Choose Symptoms 8")
          
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
          
           symp9 = st.text_input("Choose Symptoms 9")
          
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
          
           symp10 = st.text_input("Choose Symptoms 10")
          
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
          
           symp11 = st.text_input("Choose Symptoms 11")
          
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
          
           symp12 = st.text_input("Choose Symptoms 12")
          
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
          
           symp13 = st.text_input("Choose Symptoms 13")
          
           symp13 = symp13_1_inv.get(symp13, "Status not found")
          
          ##################################################################
          
          
          
           butt = st.button("Submit")
           
           if butt:
               
               
               # try:
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
                 st.text(Data)
                 import pickle
                 with open('model.pickle', 'rb') as f:
                    dt = pickle.load(f)
                  
                 pred_rf = dt.predict(Data)
                 
                 pred_rf = int(pred_rf)
                 
                 # st.text(pred_rf)
                 
                  
                 pred_rf = predd.get(pred_rf, "Status not found")
              
                 fin = "You have " + str(pred_rf)  
                 
                 result = str(pred_rf)  
                
                 # st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Jokerman;">{fin}</h1>', unsafe_allow_html=True)
              
                
                 st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{fin}</h1>', unsafe_allow_html=True)
    
               
    
                
                 import pandas as pd
                
                 data_frame=pd.read_csv("Symptoms.csv")
                
                 data_label = data_frame['Disease']
                
                 x1=data_label
                
                 for i in range(0,len(data_frame)):
                    if x1[i]==result:
                        idx=i
                
                
                 data_frame1_c=data_frame['Precaution_1']
                 data_frame1_fat=data_frame['Precaution_2']
                 data_frame1_fib=data_frame['Precaution_3']
                 data_frame1_cal=data_frame['Precaution_4']
                
                
                 Req_data_c=data_frame1_c[idx]
                 Req_data_fat=data_frame1_fat[idx]
                 Req_data_fib=data_frame1_fib[idx]
                 Req_data_cal=data_frame1_cal[idx]
                
                
                 precaution = str(Req_data_c) + str(Req_data_fat) + str(Req_data_fib) + str(Req_data_cal)
                
                 st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{precaution}</h1>', unsafe_allow_html=True)
                 
                 
                 doctor = pd.read_csv("Doctor.csv")
                 
                 import random
                 
                 aa = random.randint(0,38)
                 
                 
                 doc_name = doctor['Name'][aa]
                 
                 doc1 = "Recommended Doctor Name " + str(doc_name)
                 
                 
                 st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{doc1}</h1>', unsafe_allow_html=True)

                 
                 doc_link = doctor['Link'][aa]
                 
                 doc2 = "Recommended Location " + str(doc_link)



                 st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{doc2}</h1>', unsafe_allow_html=True)
                
                 
                 
                 
           
               # except:  
                 
               #   st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{"Sorry i cant understand !!!"}</h1>', unsafe_allow_html=True)
 
                 
            
                
  
if speak:              
    
    import streamlit as st
    import sounddevice as sd
    import numpy as np
    import os
    from scipy.io.wavfile import write as wavwrite
    
    def record_voice(duration=5, sample_rate=44100):
        st.write("Recording...")
    
        # Record audio
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
    
        st.write("Recording complete!")
    
        return audio_data.flatten(), sample_rate
    
    def save_audio_to_file(audio_data, sample_rate, save_folder="recordings"):
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
    
        file_path = os.path.join(save_folder, "recorded_audio.wav")
    
        # Save the audio data as a WAV file
        wavwrite(file_path, sample_rate, audio_data.astype(np.int16))
    
        return file_path
    
    # def main():
        # st.title("Voice Input Streamlit App")
    
    # st.write("Press the button to start recording your voice.")

    if st.button("Record Voice"):
        audio_data, sample_rate = record_voice()
        file_path = save_audio_to_file(audio_data, sample_rate)

        st.audio(audio_data, format="audio/wav", start_time=0, sample_rate=sample_rate)
            # st.markdown(f"**Recording saved to:** `{file_path}`")
    
    # if __name__ == "__main__":
    #     main()
    import speech_recognition as sr
    
    # def extract_telugu_audio(audio_file_path):
    recognizer = sr.Recognizer()
    
    audio_file_path = "recordings/recorded_audio.wav"
    
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data, language="en")
        # print("Extracted Telugu Text:")
        print(text)
        # st.write("Extracted Telugu Text:",text)
        file = open ('writeme.txt', 'w', encoding="utf-8")    
        file.write(text)  
        file.close()  
        # with open('Extracted.txt', 'w') as f:
        #     f.write(text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")    
        
        
        
        
        
# if __name__ == "__main__":
    audio_file_path = "recordings/recorded_audio.wav"
    # extract_telugu_audio(audio_file_path)

    import codecs
    with codecs.open("writeme.txt", "r", "utf-8") as f:
            a1 = f.read()         
    # st.write("User said:", a1)
    
    
    from gtts import gTTS 
  
    language = 'en'

    myobj = gTTS(text="Hi! How can i help you?", lang=language, slow=False) 

    myobj.save("Output.mp3") 
    
  # Playing the converted file 
  # os.system("mpg321 welcome.mp3") 
          
    import streamlit as st
    import numpy as np
  
    audio_file = open('Output.mp3', 'rb')
    audio_bytes = audio_file.read()
  
    st.write("Bot")

    st.audio(audio_bytes, format='audio/mp3')     
    
    
############################################### -------------------------------------------------

    # import streamlit as st
    # import sounddevice as sd
    # import numpy as np
    # import os
    # from scipy.io.wavfile import write as wavwrite
    
    def record_voice(duration=5, sample_rate=44100):
        st.write("Recording...")
    
        # Record audio
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
    
        st.write("Recording complete!")
    
        return audio_data.flatten(), sample_rate
    
    def save_audio_to_file(audio_data, sample_rate, save_folder="recordings"):
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
    
        file_path = os.path.join(save_folder, "recorded_audio1.wav")
    
        # Save the audio data as a WAV file
        wavwrite(file_path, sample_rate, audio_data.astype(np.int16))
    
        return file_path
    
    # def main():
        # st.title("Voice Input Streamlit App")
    
    # st.write("Press the button to start recording your voice.")

    if st.button("Record next"):
        audio_data, sample_rate = record_voice()
        file_path = save_audio_to_file(audio_data, sample_rate)

        st.audio(audio_data, format="audio/wav", start_time=0, sample_rate=sample_rate)
            # st.markdown(f"**Recording saved to:** `{file_path}`")
    
    # if __name__ == "__main__":
    #     main()
    import speech_recognition as sr
    
    # def extract_telugu_audio(audio_file_path):
    recognizer = sr.Recognizer()
    
    audio_file_path = "recordings/recorded_audio1.wav"
    
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data, language="en")
        # print("Extracted Telugu Text:")
        print(text)
        # st.write("Extracted Telugu Text:",text)
        file = open ('writeme.txt', 'w', encoding="utf-8")    
        file.write(text)  
        file.close()  
        # with open('Extracted.txt', 'w') as f:
        #     f.write(text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")    
        
        
        
        
        
# if __name__ == "__main__":
    audio_file_path = "recordings/recorded_audio1.wav"
    # extract_telugu_audio(audio_file_path)

    import codecs
    with codecs.open("writeme.txt", "r", "utf-8") as f:
            a1 = f.read()         
    # st.write("User said:", a1)
    
    
    from gtts import gTTS 
  
    language = 'en'

    myobj = gTTS(text="Kindly enter the below symptoms?", lang=language, slow=False) 

    myobj.save("Output1.mp3") 
    
  # Playing the converted file 
  # os.system("mpg321 welcome.mp3") 
          
    import streamlit as st
    import numpy as np
  
    audio_file = open('Output1.mp3', 'rb')
    audio_bytes = audio_file.read()
  
    st.write("Bot")

    st.audio(audio_bytes, format='audio/mp3')     
    
    ###################################
    
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
 
    symp1 = st.text_input("Enter Symptoms 1")
 
 
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
   
    symp2 = st.text_input("Enter Symptoms 2")
   
   
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
   
   
    symp3 = st.text_input("Choose Symptoms 3")
   
   
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
   
    symp4 = st.text_input("Choose Symptoms 4")
   
   
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
    
    symp5 = st.text_input("Choose Symptoms 5")
   
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
   
    symp6 = st.text_input("Choose Symptoms 6")
   
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
   
    symp7 = st.text_input("Choose Symptoms 7")
   
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
   
    symp8 = st.text_input("Choose Symptoms 8")
   
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
   
    symp9 = st.text_input("Choose Symptoms 9")
   
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
   
    symp10 = st.text_input("Choose Symptoms 10")
   
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
   
    symp11 = st.text_input("Choose Symptoms 11")
   
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
   
    symp12 = st.text_input("Choose Symptoms 12")
   
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
   
    symp13 = st.text_input("Choose Symptoms 13")
   
    symp13 = symp13_1_inv.get(symp13, "Status not found")
   
   ##################################################################
   
   
   
    butt = st.button("Submit")
    
    if butt:
        
        
        try:
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
           
          import pickle
          with open('model.pickle', 'rb') as f:
             dt = pickle.load(f)
           
          pred_rf = dt.predict(Data)
          
          pred_rf = int(pred_rf)
          
          # st.text(pred_rf)
          
           
          pred_rf = predd.get(pred_rf, "Status not found")
       
          fin = "You have " + str(pred_rf)  
          
          result = str(pred_rf)  
         
          # st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Jokerman;">{fin}</h1>', unsafe_allow_html=True)
          from gtts import gTTS
          import os
        
          predictedtext = fin
            
          language = 'en'
            
          myobj = gTTS(text=predictedtext, lang=language, slow=False)
        
          print("conversion starting ...........")
          print()
        
          myobj.save("finalres.mp3")
        
         
          # st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{fin}</h1>', unsafe_allow_html=True)

          
          audio_file = open('finalres.mp3', 'rb')
          audio_bytes = audio_file.read()
      
          st.write("Bot")
    
          st.audio(audio_bytes, format='audio/mp3')     

         
          import pandas as pd
         
          data_frame=pd.read_csv("Symptoms.csv")
         
          data_label = data_frame['Disease']
         
          x1=data_label
         
          for i in range(0,len(data_frame)):
             if x1[i]==result:
                 idx=i
         
         
          data_frame1_c=data_frame['Precaution_1']
          data_frame1_fat=data_frame['Precaution_2']
          data_frame1_fib=data_frame['Precaution_3']
          data_frame1_cal=data_frame['Precaution_4']
         
         
          Req_data_c=data_frame1_c[idx]
          Req_data_fat=data_frame1_fat[idx]
          Req_data_fib=data_frame1_fib[idx]
          Req_data_cal=data_frame1_cal[idx]
         
         
          precaution = str(Req_data_c) + str(Req_data_fat) + str(Req_data_fib) + str(Req_data_cal)
          
          
          predictedtext = precaution
            
          language = 'en'
            
          myobj = gTTS(text=predictedtext, lang=language, slow=False)
        
          print("conversion starting ...........")
          print()
        
          myobj.save("precaution.mp3")
        
         
          # st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{fin}</h1>', unsafe_allow_html=True)

          
          audio_file = open('precaution.mp3', 'rb')
          audio_bytes = audio_file.read()
      
          st.write("Bot")
    
          st.audio(audio_bytes, format='audio/mp3')   
          
          
          
         
          # st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{precaution}</h1>', unsafe_allow_html=True)
          
          
          
          doctor = pd.read_csv("Doctor.csv")
          
          import random
          
          aa = random.randint(0,38)
          
          
          doc_name = doctor['Name'][aa]
          
          doc1 = "Recommended Doctor Name " + str(doc_name)
          

        
          predictedtext = doc1
            
          language = 'en'
            
          myobj = gTTS(text=predictedtext, lang=language, slow=False)
        
          print("conversion starting ...........")
          print()
        
          myobj.save("doctname.mp3")
        
        
          
          audio_file = open('doctname.mp3', 'rb')
          audio_bytes = audio_file.read()
      
          st.write("Bot")
    
          st.audio(audio_bytes, format='audio/mp3')     
          
          
          # st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{doc1}</h1>', unsafe_allow_html=True)

          
          doc_link = doctor['Link'][aa]
          
          doc2 = "Recommended Location " + str(doc_link)

          predictedtext = doc2
            
          language = 'en'
            
          myobj = gTTS(text=predictedtext, lang=language, slow=False)
        
          print("conversion starting ...........")
          print()
        
          myobj.save("doctloc.mp3")
        
        
          
          # audio_file = open('doctloc.mp3', 'rb')
          # audio_bytes = audio_file.read()
      
          # st.write("Bot")
    
          # st.audio(audio_bytes, format='audio/mp3') 

          st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{doc2}</h1>', unsafe_allow_html=True)
         
          
          
          
    
        except:  
          
         # st.markdown(f'<h1 style="color:#000000;font-size:14px;text-align:right;">{"Sorry i cant understand !!!"}</h1>', unsafe_allow_html=True)

          
        
         predictedtext = "Sorry i cant understand"
           
         language = 'en'
           
         myobj = gTTS(text=predictedtext, lang=language, slow=False)
        
         print("conversion starting ...........")
         print()
        
         myobj.save("error.mp3")
        
        
         
         audio_file = open('error.mp3', 'rb')
         audio_bytes = audio_file.read()
        
         st.write("Bot")
        
         st.audio(audio_bytes, format='audio/mp3') 