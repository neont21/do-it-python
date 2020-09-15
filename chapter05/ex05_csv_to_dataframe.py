import pandas as pd
import re, os

df = pd.read_csv('apt.csv', encoding='cp949')
print(df.head())
print(df.tail())

print('[면적 > 130]')
print(df[df.면적 > 130])

print('가격[면적 > 130 AND 가격 < 15000]')
print(df.가격[(df.면적 > 130) & (df.가격 < 15000)])

print(df.loc[:10, ['아파트', '가격']])
print(df.loc[:, ['아파트', '가격']] [df.가격 > 40000])

df['단가'] = df.가격 / df.면적
print('[단가]')
print(df.loc[:10, ('가격', '면적', '단가')])
