import os

os.chdir('./target')
with open('test.txt', 'w') as f:
    f.write('나는 오늘 학교에 갔다.')
