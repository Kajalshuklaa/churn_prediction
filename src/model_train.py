import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_data\x.csv')
y = pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_Data\y.csv')
import os

models = [
    LogisticRegression(),
    DecisionTreeClassifier(random_state=42),
    RandomForestClassifier(random_state=42),
    AdaBoostClassifier(random_state=42),
    GradientBoostingClassifier(random_state=42)
]

x_train, x_test, y_train, y_test = train_test_split(df,y,random_state=42, stratify=y)
from sklearn.metrics import accuracy_score

d = {}  # Store model performance
for model in models:
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    acc = accuracy_score(y_test, pred)
    if model not in d:
        d[model] = acc
print(d)  # Check accuracy of all models

model = [a for a,b in d.items() if b ==max(d.values())][0]

import joblib
joblib.dump(model,r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\models\model')