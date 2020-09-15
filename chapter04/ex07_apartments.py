import os, re, usecsv

apt = usecsv.switch(usecsv.opencsv('apt_201910.csv'), enc='latin1')

print(apt[:3], len(apt))

# Fail to solve encoding issue...
# I did `iconv` and `open(..., encoding=<encoding>)` but they do not worked.
