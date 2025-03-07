import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\cleaned_Data\cleaned_data.csv')

import joblib
from sklearn.calibration import LabelEncoder


label_enc = LabelEncoder()

# Apply LabelEncoder to all categorical columns
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                    'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                    'PaperlessBilling', 'PaymentMethod']
y = df['Churn']
df.drop('Churn',axis=1,inplace=True)

for col in categorical_cols:
    df[col] = label_enc.fit_transform(df[col])  # Convert categorical values to numbers
joblib.dump(label_enc,r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\models\label')
import os
os.makedirs(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_data',exist_ok=True)
df.to_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_data\x.csv',index=False)
y.to_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_data\y.csv',index=False)