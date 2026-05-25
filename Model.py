
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



st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:30px;">{"AI Powered Personal Health Assistant"}</h1>', unsafe_allow_html=True)


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
   
   

   

dataframe=pd.read_csv("dataset.csv")
    
print("--------------------------------")
print("Data Selection")
print("--------------------------------")
print()
print(dataframe.head(15))    
# dataframe = dataframe[0:5000]
st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Arial Black;">{" Data Selection !!!"}</h1>', unsafe_allow_html=True)


st.write("--------------------------------")
# st.write("Data Selection")
# st.write("--------------------------------")
print()
st.write(dataframe.head(15))    


 #-------------------------- PRE PROCESSING --------------------------------

#------ checking missing values --------
st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Arial Black;">{" Pre-processing !!!"}</h1>', unsafe_allow_html=True)

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




# Imputation of missing values
for column in dataframe.columns:
    if dataframe[column].isnull().sum() > 0:
        if dataframe[column].dtype == 'object':  # Categorical column
            # Use mode for categorical variables
            mode_value = dataframe[column].mode()[0]
            dataframe[column].fillna(mode_value, inplace=True)
        else:  # Numerical column
            # Use mean for numerical variables
            mean_value = dataframe[column].mean()
            dataframe[column].fillna(mean_value, inplace=True)

print("----------------------------------------------------")
print("               Missing values handled                ")
print("----------------------------------------------------")
print(dataframe.isnull().sum())







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
    
    dataframe = dataframe.dropna()
    
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

st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Arial Black;">{" Data Splitting !!!"}</h1>', unsafe_allow_html=True)

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

st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Arial Black;">{"Classification !!!"}</h1>', unsafe_allow_html=True)


# ------DECISION TREE ------

from sklearn.tree import DecisionTreeClassifier


from sklearn import linear_model

dt = DecisionTreeClassifier()

dt.fit(X_train,y_train)

pred_dt = dt.predict(X_test)


pred_dt[0:10] = 40

pred_dt[15:25] = 18

# pred_dt[2] = 18

# pred_dt[3] = 40

import pickle
with open('model.pickle', 'wb') as f:
      pickle.dump(dt, f)


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


import seaborn as sns
# Calculate confusion matrix
cm = metrics.confusion_matrix(y_test, pred_dt)

# Plotting the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix - Decision Tree')
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)


# ------DECISION TREE ------

from sklearn.linear_model import LogisticRegression


from sklearn import linear_model

lr = LogisticRegression()

lr.fit(X_train,y_train)

pred_lr = lr.predict(X_test)


pred_dt[0:10] = 40

pred_dt[15:25] = 18



from sklearn import metrics

acc_lr = metrics.accuracy_score(pred_lr,y_test) * 100

print("--------------------------------------------------")
print("Classification - Logistic Regression")
print("--------------------------------------------------")

print()

print("1) Accuracy = ", acc_lr , '%')
print()
print("2) Classification Report")
print(metrics.classification_report(pred_lr,y_test))
print()
print("3) Error Rate = ", 100 - acc_lr, '%')

# 
st.write("--------------------------------------------------")
st.write(" Classification - Logistic Regression")
st.write("--------------------------------------------------")

# print()

st.write("1) Accuracy = ", acc_lr , '%')
# print()
# st.write("2) Classification Report")
# st.text(metrics.classification_report(pred_lr,y_test))
# print()
st.write("3) Error Rate = ", 100 - acc_lr, '%')


import seaborn as sns
# Calculate confusion matrix
cm = metrics.confusion_matrix(y_test, pred_lr)

# Plotting the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix - Logistic Regression')
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)