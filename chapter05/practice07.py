import pandas as pd

data = {'name': ['Mark', 'Jane', 'Chris', 'Ryan'],
        'age': [33, 32, 44, 42],
        'score': [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)
print(df.age.mean())
print(df.score.sum())
print(df.score.describe())
