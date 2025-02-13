# -*- coding: utf-8 -*-
"""Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rzYfVPbN1dEX5PRMouK65RORnl1qRwq-
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Importing the data
train = pd.read_csv('/train.csv')
train

# Importing the data
test = pd.read_csv('/test.csv')
test

# Finding the number of missing (NaN) values in a DataFrame
train.isna().sum()

# Finding the number of missing (NaN) values in a DataFrame
test.isna().sum()

# General information about DataFrame
train.info()

# General information about DataFrame
test.info()

# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Correlation Matrix
correlation_matrix = train.corr()
plt.figure(figsize=(30, 24))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Create input properties by dropping id and FloodProbability columns
X = train.drop(['id', 'FloodProbability'], axis=1)
y = train['FloodProbability']

# Separating X and y data sets into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from xgboost import XGBRegressor

# Creating the XGBoost regressor and fitting the training data to the model
regressor = XGBRegressor()
regressor.fit(X_train, y_train)

# Making predictions based on input features (X_test) in the test set using a trained classifier model
y_pred = regressor.predict(X_test)
y_pred

# Assessing model accuracy
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

# Remove 'id' column from DataFrame named test
test = test.drop(['id'], axis=1)

# Making predictions based on input features (test) in the test set using a trained classifier model
y_predX = regressor.predict(test)
y_predX

# Importing the data
submission = pd.read_csv('/sample_submission.csv')
submission

# Adding a new column to a pandas DataFrame named submission and assigning the values of the variable named y_predX to this column
submission['FloodProbability'] = y_predX

submission.head()

# Convert to the format required by the submission file (for example, CSV format)
submission.to_csv('submission.csv', index=False)