# Churn Prediction - End-to-End Machine Learning Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Dataset](#dataset)
4. [Machine Learning Pipeline](#machine-learning-pipeline)
5. [Model Training](#model-training)
6. [Hyperparameter Tuning](#hyperparameter-tuning)
7. [Model Deployment](#model-deployment)
8. [How to Run the Project](#how-to-run-the-project)
9. [Requirements](#requirements)
10. [Results](#results)

## Project Overview
This project focuses on predicting customer churn using machine learning models. It follows a complete end-to-end pipeline from data collection to model deployment using Streamlit. Various machine learning models are trained, and the best-performing model is selected for deployment.

## Project Structure
```
ML_BOOTCAMP/
│── data/
│   ├── raw_Data/
│   │   ├── raw.csv
│   ├── cleaned_Data/
│   │   ├── cleaned_data.csv
│   ├── preprocess_Data/
│       ├── x.csv
│       ├── y.csv
│── models/
│   ├── label/
│   ├── model/
│── notebook/
│   ├── data_cleaning.ipynb
│   ├── data_collection.ipynb
│   ├── hyperparameter.ipynb
│   ├── model_train.ipynb
│   ├── preprocessing.ipynb
│── preprocess_data/
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   ├── y_test.csv
│── src/
│   ├── data_cleaning.py
│   ├── data_collection.py
│   ├── hy.py
│   ├── model_train.py
│   ├── preprocess.py
│   ├── App.py
│   ├── main.py
│── README.md
│── requirements.txt
```

## Dataset
The dataset contains customer information and their churn status. The data undergoes various preprocessing steps before model training. The key steps include:
- Data Cleaning
- Feature Engineering
- Splitting Data into Training and Testing Sets

## Machine Learning Pipeline
The project follows a structured pipeline:
1. **Data Collection**: The dataset is loaded into the project from `raw.csv`.
2. **Data Cleaning**: Missing values and duplicate entries are handled in `data_cleaning.py`.
3. **Data Preprocessing**:
   - Features are selected and transformed in `preprocessing.ipynb`.
   - Data is split into `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`.
4. **Model Training**:
   - The models trained include:
     - Logistic Regression
     - Decision Tree Classifier
     - Random Forest Classifier
     - AdaBoost Classifier
     - Gradient Boosting Classifier
   - Models are trained and stored in the `models` directory.
5. **Hyperparameter Tuning**:
   - Best model parameters are determined in `hyperparameter.ipynb`.
   - The best-performing model is selected and saved.
6. **Deployment**:
   - `App.py` loads the best model and uses it for predictions via a Streamlit-based UI.

## Model Training
The model training is performed using the following classifiers:
```python
models = [
    LogisticRegression(),
    DecisionTreeClassifier(random_state=42),
    RandomForestClassifier(random_state=42),
    AdaBoostClassifier(random_state=42),
    GradientBoostingClassifier(random_state=42)
]
```
After training, the models are evaluated, and the best one is selected based on accuracy and other performance metrics.

## Hyperparameter Tuning
Hyperparameter tuning is performed to optimize the best model. The fine-tuned model is then saved for deployment.

## Model Deployment
- The Streamlit app (`App.py`) allows users to input customer data and predict churn probabilities.
- The best model is loaded and used for real-time predictions.

## How to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/Kajalshuklaa/churn_prediction.git
   cd churn_prediction
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run App.py
   ```

## Requirements
Install the required Python libraries before running the project:
```sh
pip install -r requirements.txt
```

## Results
- The best model is deployed via Streamlit.
- Users can input customer data and receive churn predictions.
- The project follows a structured pipeline ensuring reproducibility and scalability.

---
This project showcases an end-to-end approach to churn prediction using machine learning, covering data preprocessing, model training, hyperparameter tuning, and deployment.

