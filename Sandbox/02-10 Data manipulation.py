import pathlib
import numpy as np
import pandas as pd
import matplotlib

from matplotlib import pyplot as plt
data_path = pathlib.Path(r'C:\Users\taura\Desktop\pythonProject1\Tennis-Major-Tournaments-Match-Statistics\AusOpen-men-2013.csv')

df = pd.read_csv(data_path)

df.info()

df.fillna(-1, inplace=True)

desc = df.describe()

df2 = df[['Player1', 'Player2', 'DBF.1', 'DBF.2']].copy()

gr = df[['Player1', 'DBF.1']].groupby('Player1').count().reset_index()

gr = df[['Player1', 'DBF.1']].groupby('Player1').mean()

gr2 = df[['Player1', 'DBF.1']].groupby('Player1').aggregate(np.mean)

df2['DBF'] = gr['DBF.1'] + df2['DBF.2']


sms_path = pathlib.Path(r'C:\Users\taura\Downloads\smsspamcollection\text.csv')

sms_df = pd.read_csv(sms_path, names=['label','text',], sep='\t', encoding='utf-8')

def to_binary(in_str):
    if in_str == 'ham':
        rez = 1
    else:
        rez = 0
    return rez

sms_df['binary_label'] = sms_df['label'].apply(to_binary)

sms_df['length'] = sms_df['text'].apply(lambda x: len(x))
sms_df['length'] = sms_df.apply(lambda x: len(x.text), axis=1)

import re           #skaiciuosime kiek didziuju, kiek mazuju raidziu yra
text = sms_df['text'].iloc[0]

re.findall('[A-Z]', text).__len__()
sms_df['COUNT'] = sms_df['text'].apply(lambda x: re.findall('[A-Z]', x).__len__())

sms_df['PROC'] = sms_df['COUNT'] / sms_df['length']
