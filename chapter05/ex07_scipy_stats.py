import pandas as pd
from scipy import stats
import os

df2 = pd.read_csv('survey.csv')

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

ttest_result = stats.ttest_ind(male, female)
if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])

corr = df2.corr()
print(corr)

os.chdir('./target')
corr.to_csv('corr.csv')
