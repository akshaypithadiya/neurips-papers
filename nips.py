from bs4 import BeautifulSoup
import requests
import json
import re


def data_to_json(paper_list):

	list_dic = []

	papers_scraped = 0

	for paper_url in paper_list:

		res = requests.get(paper_url)
		src = res.content
		soup = BeautifulSoup(src, 'lxml')
		
		title = soup.find('h2',{'class':'subtitle'}).text

		authors = []
		auths = soup.find("ul", {"class", "authors"})
		for a in auths.find_all('a'):
			authors.append(a.text)
		authors = ', '.join(authors)

		summary = soup.find("p", {"class", "abstract"}).text.replace("$","")

		alla = soup.find_all('a')
		for pdf_link in alla:
			if "[PDF]" in pdf_link.text:
				pdf = "http://papers.nips.cc"+pdf_link.attrs['href']
		pdf_link = pdf

		dic = {
			'title' : title,
			'authors' : authors,
			'summary' : summary,
			'link' : pdf_link
		}

		papers_scraped+=1

		print("Papers scraped :", papers_scraped)
		
		list_dic.append(dic)

	return list_dic	



def papers(year_link):

	paper_list = []

	res = requests.get(year_link)
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	container = soup.find("div", {"class", "main-container"})

	for li in container.find_all('li'):
		a = li.find('a')
		paper = 'http://papers.nips.cc'+a.attrs['href']
		paper_list.append(paper)
	
	#return paper_list

	json_list = data_to_json(paper_list)
	#return json_list

	file_name = soup.find("h2", {"class":"subtitle"}).text
	path = 'json/'+f'{str(file_name)}.json'
	with open(path, 'w') as fp:
		json.dump(json_list, fp, sort_keys=True, indent=4)




if __name__ == '__main__':

	res = requests.get('http://papers.nips.cc/')
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	year_list = []

	container = soup.find("div", {"class", "main-container"})

	for li in container.find_all('li'):
		a = li.find('a')
		year_list.append('http://papers.nips.cc'+a.attrs['href'])

	#print(year_list)

	#for year in year_list:
	#	print(year)

	year_list = ['http://papers.nips.cc/book/neural-information-processing-systems-1987']

	for year in year_list:
		#print(year_url)
		x = papers(year)
		print(x)



