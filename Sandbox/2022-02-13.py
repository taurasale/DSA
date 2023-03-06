import pathlib
import numpy as np
import pandas as pd
import sklearn.ensemble
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


df = pd.read_csv(r'C:\Users\taura\Downloads\Raisin_Dataset\Raisin_Dataset\Raisin_Dataset.csv')


train, test0 = train_test_split(df)
val, test = train_test_split(test0, test_size=0.5)

xcols = ['Area', 'MajorAxisLength', 'MinorAxisLength', 'Eccentricity', 'ConvexArea', 'Extent', 'Perimeter']
ycol = 'Class'

clf = LogisticRegression(random_state=0)
clf.fit(train.loc[:, xcols], train[ycol])

preds = clf.predict(val[xcols])
cm = confusion_matrix(val[ycol], preds)
ac = accuracy_score(val[ycol], preds)
print(cm), print(ac)

#######################################################


from sklearn.tree import DecisionTreeClassifier
dc = DecisionTreeClassifier()
dc.fit(train.loc[:, xcols], train[ycol])

preds = dc.predict(val[xcols])
cm = confusion_matrix(val[ycol], preds)
ac = accuracy_score(val[ycol], preds)
print(cm), print(ac)
sklearn.tree.plot_tree(dc)

######### Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(train.loc[:, xcols], train[ycol])

preds = rf.predict(val[xcols])
cm = confusion_matrix(val[ycol], preds)
ac = accuracy_score(val[ycol], preds)
print(cm), print(ac)

