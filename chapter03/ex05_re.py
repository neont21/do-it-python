import re

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Mot a match!')

pattern = r'Life'
script = 'Life is so cool'
print(pattern, ',', script,  ':')
refinder(pattern, script)

pattern = r'life'
script = 'Life is so cool'
print(pattern, ',', script,  ':')
refinder(pattern, script)

pattern = r'cool'
script = 'Life is so cool'
print(pattern, ',', script, '(match)', ':')
refinder(pattern, script)

def refinder2(pattern, script):
    if re.search(pattern, script):
        print('Match!')
    else:
        print('Mot a match!')

pattern = r'cool'
script = 'Life is so cool'
print(pattern, ',', script, '(search)',  ':')
refinder2(pattern, script)
