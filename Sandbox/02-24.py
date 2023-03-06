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



# nuskaitome duomenys
df = pd.read_csv(r'C:\Users\taura\Downloads\archive (1)\water_potability.csv')

# greitam duomenu ivertinimui/ apziurejimui galime panaudoti info() metoda
df.info()
# taip pat galima apziureti ir skaitines duomenu characteristikas - descripbe()
stats = df.describe()

columns = df.columns
# pasaliname eilutes kur yra missing values
df.drop(['ph', 'Sulfate', 'Trihalomethanes'], axis=1, inplace=True)
# bendru atveju tai nebutinai geriausias budas. Bet missing values reikia vienokiu ar kitokiu budu tvarkyti
# Budai gali buti:
# - pasalinti duomenys missing values (eilutemis arba stulpeliais)
# - pakeisti missing values i aiskiai neteisinga reiksme (siuo atveju pvz i -1)
# - pakeisti i kintamojo vidurki arba mediana
# - naudoti koki nors duomenu iterpimo algoritma

# kadangi stulpeliu nedaug vizualiniam 'apziurejimui' galima 'nupiesti' duomenu scatter_plot'a, t.y. pasidestyma poromis
pozymiai = [col for col in columns if col not in ['ph', 'Sulfate', 'Trihalomethanes', 'Potability']]
pd.plotting.scatter_matrix(df[pozymiai])

# iskaidom duomenys i train ir test set'us
Y = df['Potability']
X = df[pozymiai]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# kuomet skirtingi kintamieji turi skirtingus mastelius, patartina naudoti vienoki ar kitoki scaler'i - transformacija
# kuri suvienodintu mastelius. Populiariausi yra realizuoti sklearn'e - StandardScaler, MinMaxScaler, MaxAbsScaler,
# RobustScaler ir t.t. Bet labai norint, galima prigalvoti ir kitokiu :)

# naudojant keleta skirtingu transformaciju, jas patogu apjungti i viena pipeline

#################################### SKIRTINGI MODELIAI ####################################
# Logistines regresijos pipeline - modelis
LR_model = Pipeline([('scaler', StandardScaler()),
                  ('predictor', LogisticRegression(n_jobs=-1))])

LR = LR_model.fit(X_train, Y_train)

#modelio skaitines charakteristikos
LR_prediction = LR.predict(X_test)
print('\t LOGISTIC REGRESSION')
print(confusion_matrix(LR_prediction, Y_test))
print(classification_report(LR_prediction, Y_test))
print('\n\n')
# [[412 244]
#  [  0   0]]
#               precision    recall  f1-score   support
#            0       1.00      0.63      0.77       656
#            1       0.00      0.00      0.00         0
#     accuracy                           0.63       656
#    macro avg       0.50      0.31      0.39       656
# weighted avg       1.00      0.63      0.77       656

############################################################################################
# Random forest pipeline - modelis
RF_model = Pipeline([('scaler', StandardScaler()),
                    ('predictor', RandomForestClassifier(n_estimators=50,
                                                        min_samples_split=5,
                                                        min_samples_leaf=2,
                                                        n_jobs=-1))])

RF = RF_model.fit(X_train, Y_train)

#modelio skaitines charakteristikos
RF_prediction = RF.predict(X_test)
print('\t RANDOM FOREST')
print(confusion_matrix(RF_prediction, Y_test))
print(classification_report(RF_prediction, Y_test))
print('\n\n')
RF_prob = RF.predict_proba(X_test)[:,1]
RF_pred1 = [(x>0.4)*1 for x in RF_prob]
print(confusion_matrix(RF_pred1, Y_test))
print(classification_report(RF_pred1, Y_test))
# [[339 191]
#  [ 73  53]]
#               precision    recall  f1-score   support
#            0       0.82      0.64      0.72       530
#            1       0.22      0.42      0.29       126
#     accuracy                           0.60       656
#    macro avg       0.52      0.53      0.50       656
# weighted avg       0.71      0.60      0.64       656

############################################################################################
# linear SVC pipeline
SVC_linear = Pipeline([('scaler', StandardScaler()),
                       ('predictor', SVC(kernel='linear', probability=True))])
SVC_linear = SVC_linear.fit(X_train, Y_train)

# apskaiciuojame modelio charakteristikas
SVC_prediction = SVC_linear.predict(X_test)
print('\t SVC LINEAR')
print(confusion_matrix(SVC_prediction, Y_test))
print(classification_report(SVC_prediction, Y_test))
print('\n\n')
# [[412 244]
#  [  0   0]]
#               precision    recall  f1-score   support
#            0       1.00      0.63      0.77       656
#            1       0.00      0.00      0.00         0
#     accuracy                           0.63       656
#    macro avg       0.50      0.31      0.39       656
# weighted avg       1.00      0.63      0.77       656

############################################################################################
# apmokome SVC modeli su rbf branduolio funkcija
SVC_rbf = Pipeline([('scaler', StandardScaler()),
                    ('predictor', SVC(kernel='rbf', probability=True))])
SVC_rbf = SVC_rbf.fit(X_train, Y_train)

# apskaiciuojame modelio charakteristikas
SVC_rbf_prediction = SVC_rbf.predict(X_test)
print('\t SVC RBF')
print(confusion_matrix(SVC_rbf_prediction, Y_test))
print(classification_report(SVC_rbf_prediction, Y_test))
print('\n\n')
# [[393 221]
#  [ 19  23]]
#               precision    recall  f1-score   support
#            0       0.95      0.64      0.77       614
#            1       0.09      0.55      0.16        42
#     accuracy                           0.63       656
#    macro avg       0.52      0.59      0.46       656
# weighted avg       0.90      0.63      0.73       656

############################################################################################
# apmokome SVC modeli su poly branduolio funkcija
SVC_poly = Pipeline([('scaler', StandardScaler()),
                    ('predictor', SVC(kernel='poly', degree=2, probability=True))])
SVC_poly = SVC_poly.fit(X_train, Y_train)

# apskaiciuojame modelio charakteristikas
SVC_poly_prediction = SVC_poly.predict(X_test)
print('\t SVC POLY2')
print(confusion_matrix(SVC_poly_prediction, Y_test))
print(classification_report(SVC_poly_prediction, Y_test))
print('\n\n')
# [[412 244]
#  [  0   0]]
#               precision    recall  f1-score   support
#            0       1.00      0.63      0.77       656
#            1       0.00      0.00      0.00         0
#     accuracy                           0.63       656
#    macro avg       0.50      0.31      0.39       656
# weighted avg       1.00      0.63      0.77       656

############################################################################################
# apmokome SVC modeli su sigmoid branduolio funkcija
SVC_sigm = Pipeline([('scaler', StandardScaler()),
                    ('predictor', SVC(kernel='sigmoid', probability=True))])
SVC_sigm = SVC_sigm.fit(X_train, Y_train)

# apskaiciuojame modelio charakteristikas
SVC_sigm_prediction = SVC_sigm.predict(X_test)
print('\t SVC SIGMOID')
print(confusion_matrix(SVC_sigm_prediction, Y_test))
print(classification_report(SVC_sigm_prediction, Y_test))
print('\n\n')
# [[270 169]
#  [142  75]]
#               precision    recall  f1-score   support
#            0       0.66      0.62      0.63       439
#            1       0.31      0.35      0.33       217
#     accuracy                           0.53       656
#    macro avg       0.48      0.48      0.48       656
# weighted avg       0.54      0.53      0.53       656
############################################################################################
# apmokome GaussianNB modeli
naiveBayes = Pipeline([('scaler', StandardScaler()),
                     ('predictor', GaussianNB())])
naiveBayes = naiveBayes.fit(X_train, Y_train)

# apskaiciuojame modelio charakteristikas
naiveBayes_prediction = naiveBayes.predict(X_test)
print('\t GAUSSIAN NAIVE BAYES')
print(confusion_matrix(naiveBayes_prediction, Y_test))
print(classification_report(naiveBayes_prediction, Y_test))
# [[377 211]
#  [ 35  33]]
#               precision    recall  f1-score   support
#            0       0.92      0.64      0.75       588
#            1       0.14      0.49      0.21        68
#     accuracy                           0.62       656
#    macro avg       0.53      0.56      0.48       656
# weighted avg       0.83      0.62      0.70       656



##### TO BE CONTINUED ... ON FRIDAY :D


SVC_rbf_prob = SVC_rbf.predict_proba(X_test)[:.1]
SVC_sigm_prob = SVC_sigm.predict_proba(X_test)[:.1]
naiveBayes_prob = naiveBayes.predict_proba(X_test)[:.1]

avg = []

for i in range(656):
    avg.append(np.mean(SVC_rbf_prob[i], SVC_sigm_prob[i], naiveBayes_prob[i]))