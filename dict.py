fh=open('mbox-short.txt')
j=0
a=list()
str1=list()
for line in fh:
    if line.startswith('From '):
        str1=line.split()
        a.append(str1[1])

counts=dict()
for word in a:
    counts[word]=counts.get(word,0) + 1
bigkey=None
bigval=None
for key1,val1 in counts.items():
    if bigval is None or val1 > bigval:
        bigkey = key1
        bigval = val1
print(bigkey,bigval)
