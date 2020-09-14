import os, re, codecs

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
line = re.findall(r'Monica:.+', script101)

for item in line[:3]:
    print(item)

f.close()

os.chdir('./target')
f = open('monica.txt', 'w', encoding='utf-8')
monica = ''

for i in line:
    monica += i+'\n'

f.write(monica)
f.close()
