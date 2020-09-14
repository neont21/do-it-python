import os

os.chdir('./target')
f = open('a.txt', 'a')
f.write(' 학교에 가지 않을 날이 올까?')
f.close()

f = open('a.txt', 'r')
print(f.read())
f.close()
