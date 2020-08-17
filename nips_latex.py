import json
import re
import string 
import random 
import requests
from bs4 import BeautifulSoup


res = requests.get('http://papers.nips.cc/book/advances-in-neural-information-processing-systems-20-2007')
src = res.content
soup = BeautifulSoup(src, 'lxml')
#
#
#abatract = soup.find("p", {"class", "abstract"}).text.replace("$","")
#
#print(abatract)


#file name

file_name = soup.find("h2", {"class":"subtitle"}).text
print(file_name)

