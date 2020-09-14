import os, re, codecs

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
sentences = f.readlines()
f.close()

def select(keyword):
    texts = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search(keyword, i) ]
    return texts

os.chdir('./target')

keyword = 'take'
f = open(keyword+'.txt', 'w')
f.writelines(select(keyword))
f.close()

keyword = 'would'
f = open(keyword+'.txt', 'w')
f.writelines(select(keyword))
f.close()
