import joblib
import pandas as pd
model = joblib.load(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\models\model')

x = pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_Data\x.csv')

y = pd.read_csv(r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\data\preprocess_Data\y.csv')
param_grid = {
    'LogisticRegression()': {
        'C': [0.1, 1, 10],
        'penalty': ['l1', 'l2'],
        'solver': ['liblinear', 'lbfgs'],
        'max_iter': [100, 500, 1000]
    },

    'DecisionTreeClassifier(random_state=42)': {
        'criterion': ['gini', 'entropy'],
        'max_depth': [5, 10, 20, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    },

    'RandomForestClassifier(random_state=42)': {
        'n_estimators': [50, 100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    },

    'AdaBoostClassifier(random_state=42)': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.001, 0.01, 0.1, 1],
        'algorithm': ['SAMME', 'SAMME.R']
    },

    'GradientBoostingClassifier(random_state=42)': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.001, 0.01, 0.1, 1],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
}

param_grid = param_grid[str(model)]
from sklearn.model_selection import GridSearchCV

# Example: Applying GridSearchCV on Logistic Regression

grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid.fit(x, y)

# Best Parameters
print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)

best_model = grid.best_estimator_
import joblib
joblib.dump(best_model,r'C:\Users\kajal shukla\Desktop\Data Science\ML BOOTCAMP\models\best_model')