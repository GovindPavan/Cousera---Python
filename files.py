# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0
c=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find('0')
    num=line[pos:]
    num=float(num)
    s=s+num
    c=c+1
avg=s/c
print("Average spam confidence:",avg)
