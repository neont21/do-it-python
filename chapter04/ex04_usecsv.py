import usecsv, os

os.chdir('./target')
a = [['국어', '영어', '수학'], [99, 88, 77]]
usecsv.writecsv('test.csv', a)
