import csv, os

f = open('a.csv', 'r')
a_list = []
new = csv.reader(f)
for i in new:
    print(i)
    a_list.append(i)

f.close()

print(a_list)
