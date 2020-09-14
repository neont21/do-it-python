import re

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
print(re.findall(r'\d+.년', example1))

example2 = '이동민 교수는 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 학자는 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018).'
print(re.findall(r'\(.+?\)', example2))

sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', sentence))
print(re.sub(r'dog', 'cat', sentence))
print(re.findall(r'\w+ly', sentence))
