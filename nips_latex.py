import json
import re
import string 
import random 
import requests
from bs4 import BeautifulSoup


#res = requests.get('http://papers.nips.cc/book/advances-in-neural-information-processing-systems-20-2007')
res = requests.get('http://papers.nips.cc/paper/87-high-order-neural-networks-for-efficient-associative-memory-design')


src = res.content
soup = BeautifulSoup(src, 'lxml')
#
#
#abatract = soup.find("p", {"class", "abstract"}).text.replace("$","")
#
#print(abatract)


#file name


authors = []
auths = soup.find("ul", {"class", "authors"})
for a in auths.find_all('a'):
	authors.append(a.text)
authors = ', '.join(authors)
print(authors)

file_name = soup.find("h2", {"class":"subtitle"}).text
print(file_name)

