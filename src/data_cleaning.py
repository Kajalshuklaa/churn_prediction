import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sklearn
from sklearn.preprocessing import LabelEncoder
import os
import joblib

from data_collection import datacollection
class datacleaning():
    def __init__(self):
         pass
    def data_cleaning(self):
         df=pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\raw_data\raw.csv')
         df
         df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
         label_enc = LabelEncoder()
                 # Apply LabelEncoder to all categorical columns
    categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                            'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                            'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                            'PaperlessBilling', 'PaymentMethod', 'Churn']
    df.drop(columns=['customerID'], inplace=True)
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    os.makedirs(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\cleaned_Data',exist_ok=True)
    df.to_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\cleaned_Data\cleaned_Data.csv',index=False)


if __name__=='__main__':
    try:
        obj=datacleaning()
        obj.data_cleaning()
    except Exception as e:
        raise e



    
          



