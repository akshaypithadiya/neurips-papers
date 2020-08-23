from bs4 import BeautifulSoup
import requests
import json


def scrape(papers):

	list_data = []

	papers_scraped = 0

	for paper in papers:

		res = requests.get(paper)
		src = res.content
		soup = BeautifulSoup(src, 'lxml')
		
		title = soup.find('h2',{'class':'subtitle'}).text

		authors = []
		auth = soup.find("ul", {"class", "authors"})
		for a in auth.find_all('a'):
			authors.append(a.text)
		authors = ', '.join(authors)

		abstract = soup.find("p", {"class", "abstract"}).text.replace("$","")

		a = soup.find_all('a')
		for pdf_link in a:
			if "[PDF]" in pdf_link.text:
				pdf = "http://papers.nips.cc"+pdf_link.attrs['href']
		pdf_link = pdf

		dic = {
			'title' : title,
			'authors' : authors,
			'abstract' : abstract,
			'pdf' : pdf_link
		}

		papers_scraped+=1

		print("papers scraped :", papers_scraped)
		
		list_data.append(dic)

	return list_data	



def nips_papers(year):

	res = requests.get(year)
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	papers = []

	container = soup.find("div", {"class", "main-container"})

	for li in container.find_all('li'):
		a = li.find('a')
		paper = 'http://papers.nips.cc'+a.attrs['href']
		papers.append(paper)
	
	#return papers

	scraped_data = scrape(papers)
	#return scraped_data

	file_name = soup.find("h2", {"class":"subtitle"}).text
	file_name = file_name[-5:-1]
	path = 'papers/'+str(file_name)+'.json'

	with open(path, 'w') as file:
		json.dump(scraped_data, file, sort_keys=True, indent=4, ensure_ascii=False)



if __name__ == '__main__':

	res = requests.get('http://papers.nips.cc/')
	src = res.content
	soup = BeautifulSoup(src, 'lxml')

	years = []

	container = soup.find("div", {"class", "main-container"})

	for li in container.find_all('li'):
		a = li.find('a')
		years.append('http://papers.nips.cc'+a.attrs['href'])

	#print(years)

	years = ['http://papers.nips.cc/book/neural-information-processing-systems-1987']

	for year in years:
		nips_papers(year)



