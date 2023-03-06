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

df = pd.read_csv(r'C:\Users\taura\Downloads\adult.csv')

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

data1 = pd.read_csv(r'C:\Users\taura\Downloads\adult.csv', names=columns)

df.info()
## Paziurime kiek ir ko yra
test_par = 'sex'
df_test = data[['age', test_par]].groupby(test_par).count().reset_index()

## Uzkoduojam lyti - vyras ar moteris
SexEncoder = OrdinalEncoder()
SexEncoder.fit(data[['sex']])

SexEncoder.categories_
data['sex_encoded'] = SexEncoder.transform(data[['sex']])
df=data[['sex', 'sex_encoded']]
df['sex_enc2'] = df['sex'].apply(lambda x: (x==' Male')*1)

test_par = 'education'
df_test = data[['age', test_par]].groupby(test_par).count().reset_index()
### Uzkoduosime Education su Ordinal Encoder

#EduEnc = OrdinalEncoder()
#EduEnc.fit(data[['education']])
#SexEncoder.categories_
#data['edu_encoded'] = EduEnc.transform(data[['education']])
#df=data[['education', 'edu_encoded']]

EduEncoder = OneHotEncoder(sparse=False)
EduEncoder.fit(data[['education']])
EduEncoder.categories_
edu = EduEncoder.transform(data[['education']])
edu_df = pd.DataFrame(data=edu, columns=EduEncoder.categories_)
data.merge(edu_df)

#### marital status

test_par = 'marital-status'
df_test = data[['age', test_par]].groupby(test_par).count().reset_index()

test_par = 'income'
df_test = data[['age', test_par]].groupby(test_par).count().reset_index()


enc = LabelEncoder()
enc.fit(data['income'])
enc.classes_
y = enc.transform(data['income'])

data['income_encoded'] = data['income'].apply(lambda x: (x==' >50K')*1) ##dauginam is 1 kad nebutu Boolean
data = data.drop('income_enc', axis=1)

########## Susiencodiname categorical values
data1.info()

categorical_features = ['workclass']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([('one_hot',
                                  one_hot,
                                  categorical_features)],
                                remainder='passthrough')
transformed_X = transformer.fit_transform(data1)
transformed_X
f = pd.DataFrame(transformed_X)

df_joined = data.join(edu_df)

dummies = pd.get_dummies(data1[['workclass']])

naujas = df_joined.join(dummies)
naujas.columns
naujas.iloc[:,18:].ren


def encode_age(x):
    if x < 25:
        group = 0
    else:
        group = 1
    return group

data['age'].apply(encode_age(x=data['age']))