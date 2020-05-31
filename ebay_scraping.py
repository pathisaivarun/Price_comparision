#!/usr/bin/env python3

#proxy = urllib.request.ProxyHandler({'https': 'http://'+'N140440'+':'+'password'+'@10.1.1.30:3128'})
#auth = urllib.request.HTTPBasicAuthHandler()
#opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
#urllib.request.install_opener(opener)
#conn = uReq('https://www.google.com/')

#r = requests.get('https://www.flipkart.com/search?q=laptop')
#content = r.content.decode(encoding='UTF-8')
#soup = soup(r.content.decode(encoding='UTF-8'), "lxml")

def scrape(prod):
	from bs4 import BeautifulSoup as soup
	import urllib.request
	from urllib.request import urlopen as uReq
	import requests
	import sys
	import re
	prod=prod.strip()
	prod=prod.replace(' ','+')
	my_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw='+prod+'&_sacat=0'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	container = page_soup.findAll("li", {"class": "s-item"})
	dit={}	
	count=0
	for i in container:
		count+=1
		try:
			name = i.find("img")["alt"]
			price=re.findall("INR\W[\d\,\.]+",str(i))
			aaa=[]
			if "-" in name:
				name1 = re.findall("([\w+\b \b]*)\-\W([\w+\W+]*)",str(name))
				aaa.append(name1[0][1])
				aaa.append(str(price[0]))
				dit[str(name1[0][0])]=aaa
			else:
				aaa.append(" ")
				aaa.append(str(price[0]))
				dit[str(name)]=aaa
			#fp1.write(str(name)+":"+str(price[0])+"\n")
		except:
			print("",end="")
	return dit
