import os, re
import pandas as pd

df2 = pd.read_csv('survey.csv')

print('[head]')
print(df2.head())

print('[mean]')
print(df2.mean())

print('[income mean]')
print(df2.income.mean())

print('[describe]')
print(df2.describe())

print('[counts of sex]')
print(df2.sex.value_counts())

print('[mean group by sex]')
print(df2.groupby(df2.sex).mean())
