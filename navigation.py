
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
     
import sqlite3

# ================ Background image ===



def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    
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
    add_bg_from_local('1.jpg')

    st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:30px;">{"AI Powered Personal Health Assistant"}</h1>', unsafe_allow_html=True)
    
    print()
    print()

    print()

    st.text("                 ")
    st.text("                 ")
    a = "  * This project aims to develop an advanced Clinical Decision Support System (CDSS) using DT and LR to enhance the accuracy of disease prediction based on health data inputs. The system will integrate robust data preprocessing techniques to ensure high-quality input for effective model training by addressing missing values, encoding categorical variables, and filtering out irrelevant information. In addition to predictive capabilities, the system will feature an interactive, multilingual chatbot that supports both text and voice inputs in languages such as Tamil and English. This chatbot will offer personalized medical advice, including disease predictions, treatment recommendations, and doctor referrals. To further improve user experience and healthcare accessibility, the system will also include functionality to identify and display the nearest medical facilities based on the predicted diagnosis and recommended treatments. This comprehensive approach aims to provide users with accurate, accessible, and actionable medical guidance. * "
    
    st.markdown(f'<h1 style="color:#000000;text-align: justify;font-size:30px;font-family:Caveat, sans-serif;">{a}</h1>', unsafe_allow_html=True)

    st.text("                 ")
    st.text("                 ")
    
    st.text("                 ")
    st.text("                 ")
    



elif navigation()=='reg':
    
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
    add_bg_from_local('2.jpg')

   
    st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:30px;">{"AI Powered Personal Health Assistant"}</h1>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Register Here !!!"}</h1>', unsafe_allow_html=True)
    
    import streamlit as st
    import sqlite3
    import re
    
    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    # Function to create a new user
    def create_user(conn, user):
        sql = ''' INSERT INTO users(name, password, email, phone)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    
    # Function to check if a user already exists
    def user_exists(conn, email):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        if cur.fetchone():
            return True
        return False
    
    # Function to validate email
    def validate_email(email):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.match(pattern, email)
    
    # Function to validate phone number
    def validate_phone(phone):
        pattern = r'^[6-9]\d{9}$'
        return re.match(pattern, phone)
    
    # Main function
    def main():
        # st.title("User Registration")
    
        # Create a database connection
        conn = create_connection("dbs.db")
    
        if conn is not None:
            # Create users table if it doesn't exist
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT NOT NULL UNIQUE,
                         phone TEXT NOT NULL);''')
    
            # User input fields
            
            st.markdown(
                """
                <style>
                .custom-label {
                    font-size: 13px; /* Change the font size */
                    color: #000000;  /* Change the color */
                    font-weight: bold; /* Optional: make text bold */
                    display: inline-block; /* Make label inline with the input */
                    margin-right: 10px; /* Adjust the space between label and input */
                }
                .custom-input {
                    vertical-align: middle; /* Align input vertically with label */
                }
                </style>
                <label class="custom-label">Enter your name:</label>
                """,
                unsafe_allow_html=True
            )
            name = st.text_input("")
            
    
            # Create the text input field and password field
            # name = st.text_input("Your name")
            
            st.markdown(
                """
                <style>
                .custom-label {
                    font-size: 13px; /* Change the font size */
                    color: #000000;  /* Change the color */
                    font-weight: bold; /* Optional: make text bold */
                    display: inline-block; /* Make label inline with the input */
                    margin-right: 10px; /* Adjust the space between label and input */
                }
                .custom-input {
                    vertical-align: middle; /* Align input vertically with label */
                }
                </style>
                <label class="custom-label">Enter your Password:</label>
                """,
                unsafe_allow_html=True
            )
            
            password = st.text_input("",type="password")
    
            
            st.markdown(
                """
                <style>
                .custom-label {
                    font-size: 13px; /* Change the font size */
                    color: #000000;  /* Change the color */
                    font-weight: bold; /* Optional: make text bold */
                    display: inline-block; /* Make label inline with the input */
                    margin-right: 10px; /* Adjust the space between label and input */
                }
                .custom-input {
                    vertical-align: middle; /* Align input vertically with label */
                }
                </style>
                <label class="custom-label">Enter your Confirm Password:</label>
                """,
                unsafe_allow_html=True
            )
            
            confirm_password = st.text_input(" ",type="password")
            
            # ------
    
            st.markdown(
                """
                <style>
                .custom-label {
                    font-size: 13px; /* Change the font size */
                    color: #000000;  /* Change the color */
                    font-weight: bold; /* Optional: make text bold */
                    display: inline-block; /* Make label inline with the input */
                    margin-right: 10px; /* Adjust the space between label and input */
                }
                .custom-input {
                    vertical-align: middle; /* Align input vertically with label */
                }
                </style>
                <label class="custom-label">Enter your Email ID:</label>
                """,
                unsafe_allow_html=True
            )
    
            email = st.text_input("  ")
            
            
            st.markdown(
                """
                <style>
                .custom-label {
                    font-size: 13px; /* Change the font size */
                    color: #000000;  /* Change the color */
                    font-weight: bold; /* Optional: make text bold */
                    display: inline-block; /* Make label inline with the input */
                    margin-right: 10px; /* Adjust the space between label and input */
                }
                .custom-input {
                    vertical-align: middle; /* Align input vertically with label */
                }
                </style>
                <label class="custom-label">Enter your Phone Number:</label>
                """,
                unsafe_allow_html=True
            )
            
            
            phone = st.text_input("   ")
    
            col1, col2 , col3 = st.columns(3)
    
            with col2:
                    
                aa = st.button("REGISTER")
                
                if aa:
                    
                    if password == confirm_password:
                        if not user_exists(conn, email):
                            if validate_email(email) and validate_phone(phone):
                                user = (name, password, email, phone)
                                create_user(conn, user)
                                st.success("User registered successfully!")
                            else:
                                st.error("Invalid email or phone number!")
                        else:
                            st.error("User with this email already exists!")
                    else:
                        st.error("Passwords do not match!")
                    
                    conn.close()
                    # st.success('Successfully Registered !!!')
                # else:
                    
                    # st.write('Registeration Failed !!!')     
            

    
    
      
    if __name__ == '__main__':
        main()


if navigation() == "admin":
    
    st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:30px;">{"AI Powered Personal Health Assistant"}</h1>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Login Here !!!"}</h1>', unsafe_allow_html=True)

    
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
    add_bg_from_local('1.jpg')
    
    
    
    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    # Function to create a new user
    def create_user(conn, user):
        sql = ''' INSERT INTO users(name, password, email, phone)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    
    # Function to validate user credentials
    def validate_user(conn, name, password):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
        user = cur.fetchone()
        if user:
            return True, user[1]  # Return True and user name
        return False, None
    
    # Main function
    def main():
        # st.title("User Login")
        # st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Login here"}</h1>', unsafe_allow_html=True)
    
    
        # Create a database connection
        conn = create_connection("dbs.db")
    
        if conn is not None:
            # Create users table if it doesn't exist
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT NOT NULL UNIQUE,
                         phone TEXT NOT NULL);''')
    
            st.write("Enter your credentials to login:")
            name = st.text_input("User name")
            password = st.text_input("Password", type="password")
    
            col1, col2 = st.columns(2)
    
            with col1:
                    
                aa = st.button("Login")
                
                if aa:
    
    
            # if st.button("Login"):
                    is_valid, user_name = validate_user(conn, name, password)
                    if is_valid:
                        st.success(f"Welcome back, {user_name}! Login successful!")
                        
                        import subprocess
                        subprocess.run(['python','-m''streamlit','run','Chat.py'])
                        
                        
                        
                    else:
                        st.error("Invalid user name or password!")
                        
            with col2:
                      
                  aa = st.button("Back")
                  
                  if aa:
                      import subprocess
                      subprocess.run(['python','-m''streamlit','run','Student.py'])
                      # st.success('Successfully Registered !!!')          
    
            # Close the database connection
            conn.close()
        else:
            st.error("Error! cannot create the database connection.")
    
    if __name__ == '__main__':
        main()
       
if navigation() == "graphs":
    
    
    import subprocess
    
    subprocess.run(['python','-m''streamlit','run','Model.py'])
    
    
if navigation() == "pred":
    
    
         import pickle
        
         with open('model.pickle', 'rb') as f:
            dt = pickle.load(f)  
             
    
         st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Arial Black;">{" Prediction !!!"}</h1>', unsafe_allow_html=True)
         
         
         
         
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
         
         
            # st.text(symp1)
            
            # st.text(symp2)
            
            # st.text(symp3)

 
            # st.text(symp4)
            
            # st.text(symp5)
            
            # st.text(symp6)
            
            # st.text(symp7)
            
            # st.text(symp8)
            
            # st.text(symp9)

 
            # st.text(symp10)
            
            # st.text(symp11)
            
            # st.text(symp12)
            
            # st.text(symp13)
  
            
            
            
            
            
                    
            Data = np.array([symp1, symp2,symp3,symp4,symp5,symp6,symp7,symp8,symp9,symp10,symp11,symp12,symp13]).reshape(1, -1)
         
             
            pred_rf = dt.predict(Data)
            
            pred_rf = int(pred_rf)
            
            st.text(symp1)
            
             
            pred_rf = predd.get(pred_rf, "Status not found")
         
            fin = "Identified Disease = " + str(pred_rf)  
           
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Jokerman;">{fin}</h1>', unsafe_allow_html=True)
         
           
         
         
            
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      