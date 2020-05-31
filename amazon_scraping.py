def scrape(prod):
	dit={}
	import requests
	import re
	from bs4 import BeautifulSoup
	prod=prod.replace(" ","+")
	prod=prod.strip()
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	te=requests.get("https://www.amazon.in/s?k="+prod, headers=headers)
	print("https://www.amazon.in/s?k="+prod)
	content = te.content
	soup = BeautifulSoup(content,"html.parser")
	count=0
	a=0
	for d in soup.findAll('div', attrs={'class':'sg-row'}):
		if a==0:
			a=1
			continue
		name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
		price = d.find('span', attrs={'class':'a-offscreen'})
		rating = d.find('span', attrs={'class':'a-icon-alt'})
		link = re.search('href="([\w\W]{0,200})"\ target', str(d))
		image = re.search('src="([\w\W]{0,200})"\ srcset', str(d))
		try:
			name1 = re.findall("([\w\ \W]*)\ \(([\w+\W+]*)\)",str(name.text))
			linkk="https://www.amazon.in"+link.group(1)
			dit[name1[0][0]]=[name1[0][1], linkk, image.group(1), price.text, rating.text]
			count+=1
		except:
			print("",end="")
	return dit