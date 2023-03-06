import pandas as pd
import numpy as np
import pathlib

df2015 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2015.csv')
df2016 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2016.csv')
df2017 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2017.csv')
df2018 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2018.csv')
df2019 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2019.csv')
df2020 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2020.csv')
df2021 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2021.csv')
df2022 = pd.read_csv(r'C:\Users\taura\Downloads\archive\2022.csv')

df2023 = [df2015, df2016, df2017, df2018, df2019, df2020, df2021, df2022]
df2023z = pd.concat(df2023, keys=['2015','2016','2017','2018','2019','2020','2021','2022'])

def happiness(x):
    i = x
    for i in df2015, df2016:
        i = df2015.loc[df2015['Country'] == x, 'Happiness Score'].iloc[0]

df2015n = df2015[['Country', 'Happiness Score', 'Happiness Rank']]
df2016n = df2016[['Country', 'Happiness Score', 'Happiness Rank']]
dfn = pd.merge(df2015n,df2016n)

df2016n.rename(columns={'Country':'Country2016'}, inplace=True)

dfn = pd.merge(df2015n,df2016n)