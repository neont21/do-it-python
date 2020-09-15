import re

total = ['종로구', '151,767', '11,093', '27,394']
for i in total:
    if re.search(',', i):
        total[total.index(i)] = int(re.sub(',', '', i))

print(total)
