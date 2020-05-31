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
	prod=prod.replace(' ','%20')
	my_url = 'https://paytmmall.com/shop/search?q='+prod+'&from=organic&child_site_id=6&site_id=2'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	container = page_soup.findAll("div", {"class": "_2i1r"})
	dit={}	
	a=0
	count=0
	for i in container:
		count+=1
		try:
			if a!=0:
				name = i.find("img")["alt"]
				price=i.find("div", {"class": "_1kMS"}).text
				#fp1.write(str(name)+":"+str(price[0])+"\n")
				dit[str(name)]=str(price)
		except:
			print("",end="")
		a+=1
	return dit
