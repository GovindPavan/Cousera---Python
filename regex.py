fh=open('regex_sum.txt')
sum1=0
count=0
import re
for line in fh:
    y=re.findall('[0-9]+',line)
    for i in y:
        if i >= '0':
            sum1=sum1+int(i)
            count = count + 1
print(count,sum1)
