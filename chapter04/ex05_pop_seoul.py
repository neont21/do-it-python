import os, re, usecsv

total = usecsv.opencsv('popSeoul.csv')

result = usecsv.switch(total)

print(result[:5])
