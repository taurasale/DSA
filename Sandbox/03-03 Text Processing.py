import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay, roc_curve
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import pathlib
import re


data_path = pathlib.Path(r'C:\Users\taura\Downloads\smsspamcollection (1)\SMSSpamCollection.csv')
df = pd.read_csv(data_path, sep='\t', names=['label', 'text'], encoding='utf-8')
df['target'] = df['label'].apply(lambda x: (x == 'ham')*1)
df['length'] = df['text'].apply(lambda x: len(x))
df['count_digits'] = df['text'].apply(lambda x: len(re.findall('\d', x)))
df['count_Capital'] = df['text'].apply(lambda x: len(re.findall('[A-Z]', x)))
df['count_words'] = df['text'].apply(lambda x: len(re.findall('\w+', x)))
df['count_specials'] = df['text'].apply(lambda x: len(re.findall('[^a-zA-Z0-9]', x)))
df['digit_proportion'] = df['count_digits']/df['length']
df['letter_proportion'] = df['text'].apply(lambda x: len(re.findall('[a-zA-Z]', x))/ len(x))

Y = df['target']
X = df[['length',
'count_digits',
'count_Capital',
'count_words',
'count_specials',
'digit_proportion',
'letter_proportion']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

RF_model = RandomForestClassifier(n_estimators=50,
                            min_samples_split=5,
                            min_samples_leaf=2,
                            n_jobs=1)
RF = RF_model.fit(X_train, Y_train)
RF_prediction = RF.predict(X_test)

print(confusion_matrix(RF_prediction, Y_test))
print(classification_report(RF_prediction, Y_test))

### Naudojam TfIdf Vectorizeri

X1 = df['text']
Y1 = Y
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, test_size = 0.2, random_state = 42)



TfIdf_model = TfidfVectorizer()

TfIdf = TfIdf_model.fit(X1_train, Y1_train)
X_tfidf = TfIdf.transform(X1_train)
RF1_model = RandomForestClassifier(n_estimators=50,
                            min_samples_split=5,
                            min_samples_leaf=2,
                            n_jobs=1)

RF1 = RF1_model.fit(X_tfidf, Y1_train)
X_test_tfidf = TfIdf.transform(X1_test)

RF1_prediction = RF1.predict(X_test_tfidf)

print(confusion_matrix(RF1_prediction, Y1_test))
print(classification_report(RF1_prediction, Y1_test))