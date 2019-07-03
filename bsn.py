import urllib.request
from bs4 import BeautifulSoup

url1 = 'http://py4e-data.dr-chuck.net/comments_253225.htmls'
htm=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_253225.html')
#with urlopen(url1) as url:
#    html=url.read()
soup = BeautifulSoup(htm,'html.parser')
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)
