import pathlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv(r'C:\Users\taura\Downloads\pokemon_data.csv')

print(df['Name', 'Attack'])
## Duoda eilutes pagal pasirinkta column ir conditona
a = df.loc[(df['Attack'] > 100) % (df['Defense'] > 119)]
a = df.sort_values(["Speed"], ascending=False)

# Sukuriam nauja stulpeli - TOTAL

df['Total'] = df['Speed'] + df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def']

# ismetame stulpeli

df = df.drop(columns=['Total'])

# Kitas budas sukurti stulpeli su ILOC funkcija
df['Total'] = df.iloc[:,4:10].sum(axis=1)

#Pakeiciam stulpeliu tvarka
cols = list(df.columns.values)
df1 = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# save to csv
df1.to_csv('modified.csv', index=False)

#filtering on multiple conditions
# & - yra AND, OR -zenklas yra |

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

# 3 conditions including text condition
new = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# reset index

new = new.reset_index(drop=True)
print(new)

#Regexas
import re

# Filtruojam tuos Names kurie turi Mega
df.loc[df['Name'].str.contains('Mega')]
# Tie kurie neturi Mega
df.loc[~df['Name'].str.contains('Mega')]

df.loc[~df['Type 1'].str.contains('Fire | Grass', regex = True)]

#jei norim ignoruoti didziasias/mazasias raides:
df.loc[df['Type 1'].str.contains('fire | grass', flags=re.I, regex = True)]
# Tik tie kuriu Name yra PI
df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex = True)]

# Prasideda is PI
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)]


ps = df.loc[(df['Type 1'] == 'Fire'), 'Legendary'] == 'Lala'
print(df.iloc[1:3,1:5])


import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)

print(clf.predict([[-0.6, -1]]))
df.columns = [x.lower().strip() for x in df.columns]

def new(row):
    row['First'] = row['Name'].split(" ")[0]
    row['Last'] = row['Name'].split(" ")[-1]
    return row

df=df.apply(new, axis='columns')
del(df['First'])
del(df['Last'])

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                         {'Name': 'Mike', 'School': 'Law'},
                         {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff_df)
print(student_df)

pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
pd.merge(staff_df, student_df, how='left',left_index=True, right_index=True)
pd.merge(staff_df, student_df, how='right',left_index=True, right_index=True)

staff_df=staff_df.reset_index()
student_df=student_df.reset_index()
lol = pd.merge(staff_df, student_df, how='right', on='Name')
del(lol['index'])

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 billiard avenue'},
                         {'Name': 'Mike', 'School': 'Law', 'Location': 'Frat House'},
                         {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Cescent'}])

pd.merge(staff_df, student_df, how='left', on='Name')