import os, re, usecsv

total = usecsv.opencsv('popSeoul.csv')

#k = []
for i in total[:5]:
    #tmp = []
    for j in i:
        if re.search('[a-z가-힣]', j):
            i[i.index(j)] = j
            #tmp.append(j)
        else:
            i[i.index(j)] = float(re.sub(',', '', j))
            #tmp.append(float(re.sub(',', '', j)))
    #k.append(tmp)
    print(i)

#print(k)
print(total[:5])
