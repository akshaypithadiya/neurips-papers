import json
import re
import string 
import random 
import requests
from bs4 import BeautifulSoup


def data_to_json(paper_link_list):

	list_of_dic = []

	count = 0

	for paper_link in paper_link_list:

		res = requests.get(paper_link)
		src = res.content
		soup = BeautifulSoup(src, 'lxml')

		title = soup.find('h2',{'class':'subtitle'}).text
		string_title = title.replace('\n','').replace('\r','')
		#print(string_title)

		authors_list = []
		authors = soup.find("ul", {"class", "authors"})
		for a_tags in authors.find_all('a'):
			authors_list.append(a_tags.text)
		authors_string = ', '.join(authors_list)
		authors_string = authors_string.replace('\n','').replace('\r','')
		#print(authors_string)

		summary = soup.find('p', {"class", "abstract"}).text
		summary_string = summary.replace('\n','').replace('\r','')
		#print(summary_string)

		all_links = soup.find_all('a')
		for pdf_link in all_links:
			if "[PDF]" in pdf_link.text:
				pdf = "https://papers.nips.cc"+pdf_link.attrs['href']
		pdf_string = pdf
		#print(pdf_string)

		dic = {

		'title' : string_title,
		'authors' : authors_string,
		'summary' : summary_string,
		'link' : pdf_string

		}

		count+=1
		print("Number of links done: ", count)
		
		list_of_dic.append(dic)

	return list_of_dic


def paper_url(year_url):

	paper_url_list = []

	res = requests.get(year_url)
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	container = soup.find("div", {"class", "main-container"})

	for li_tags in container.find_all('li'):
		a_tag = li_tags.find('a')
		paper_url = 'https://papers.nips.cc'+a_tag.attrs['href']
		paper_url_list.append(paper_url)

	#return paper_url_list

	json_list = data_to_json(paper_url_list)

	#return json_list

	ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))

	path = 'json/'+f'{str(ran_str)}_nips.json'

	with open(path, 'w') as fp:
		json.dump(json_list, fp)



if __name__ == '__main__':

	res = requests.get('https://papers.nips.cc/')
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	year_urls = []

	container = soup.find("div", {"class", "main-container"})

	for li_tags in container.find_all('li'):
		a_tag = li_tags.find('a')
		year_urls.append('https://papers.nips.cc'+a_tag.attrs['href'])

	#print(year_urls)

	#for year_url in year_urls:
	#	print(year_url)

	for year_url in year_urls:
		#print(year_url)
		x = paper_url(year_url)
		print(x)



