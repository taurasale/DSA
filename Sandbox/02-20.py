import pathlib
import numpy as np
import pandas as pd
import sklearn.ensemble
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

df = pd.read_csv(r'C:\Users\taura\Downloads\archive (1)\water_potability.csv')

df.isna().sum()

#logistical, random forest, SVM, decision tree

df['ph'].fillna(df['ph'].mean(), inplace=True)
df['Sulfate'].fillna(df['Sulfate'].mean(), inplace=True)
df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean(), inplace=True)
df.isna().sum()

# Logistic regression

X = df.drop('Potability', axis = 1)
y = df['Potability']

model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   test_size=0.2)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)
print(f1)

########
# antras variantas - be tusciu values
df2= df.drop(['ph','Trihalomethanes', 'Sulfate'], axis=1)

X = df2.drop('Potability', axis = 1)
y = df2['Potability']

model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   test_size=0.2)
scaler = StandardScaler()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)

print(classification_report(y_test, y_pred))
# Random Forest Classifier

RF = RandomForestClassifier(n_estimators=500,
                            min_samples_split=50,
                            min_samples_leaf=10,
                            n_jobs=-1)

RF.fit(X_train, y_train)

y_pred = RF.predict(X_test)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

# Support Vector Machine
SV = SVC()

SV.fit(X_train, y_train)

y_pred = SV.predict(X_test)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))





pd.plotting.scatter_matrix(df)