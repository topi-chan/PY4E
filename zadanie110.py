#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
fh = open('regex_sum_972820.txt')
l = []
import re
for f in fh:
    x = re.findall('([0-9]+)', f)
    l.append(x)
res = []
[res.extend(el) for el in l]
res = [int(i) for i in res]
xxx = sum(res)
print(xxx)
