import re

e = '''Chandler: All right Joey, be nice. So does he have a hump? A hump and a hair-piece? Phoebe: Wait, does he eat chalk? Phoebe: Just, because, I don't want her to go through what I went through with Carl- oh!'''
m = re.findall('[A-Z][a-z]+:', e)
print(m)
M = list(set(m))
print(M)
