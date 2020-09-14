import os

os.chdir('./target')
f = open('a.txt', 'w')
f.write('나는 오늘 학교에 갔다.')
f.close()

f = open('a.txt', 'r')
print(f.read())
f.close()
