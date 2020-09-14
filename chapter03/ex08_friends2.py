import os, re, codecs

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
f.close()

char = re.compile(r'[A-Z][a-z]+:')
y = set(re.findall(char, script101))
z = list(y)
character = []

for i in z:
    character += [i[:-1]]

print(character)
