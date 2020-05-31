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
	dit={}
	import requests
	import re
	from selenium import webdriver
	from selenium.webdriver import ActionChains
	prod=prod.strip()
	prod=prod.replace(" ","%20")
	#chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument('headless')
	#chrome = webdriver.Chrome(chrome_options=chrome_options)
	#chrome.get("https://www.flipkart.com")
	#chrome.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(prod)
	#ele=chrome.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
	#actionChains = ActionChains(chrome)
	#actionChains.click(ele).perform()
	#actionChains.click(ele).perform()
	#print(chrome.current_url)
	te=requests.get("https://www.flipkart.com/search?q="+prod).text
	total=re.findall('({"category":[\w\W]*"type":"FEEDBACK)', str(te))
	link=re.findall('"smartUrl":"([\w\/\-\.\?\=\:]*)",', str(total))
	images=re.findall('{"images":\[{"aspectRatio":null,"contentInfo":null,"height":null,"url":"([\w\:\/\.\{\}\@\d\-]*\.jpeg)\?', str(total))
	for i in range(0,len(images)):
		images[i]=images[i].replace("{@width}","250")
		images[i]=images[i].replace("{@height}","200")
	title=re.findall('"title":"([\w\(\/\ \-\,\d\)\+]*)"},', str(total))
	price=re.findall('"finalPrice":[\w\W]{0,130}"([\d\.]*)"', str(total))
	rating = re.findall('"type":"RatingValue"[\w\W]{0,20}:([\d\.]+),', str(total))
	for i in range(0,len(title)):
		if "-" in title[i]:
			name = re.findall("([\w+\b \b]*)\-\W\(([\w+\W+]*)\)|([\w+\b \b]*)\W\(([\w+\W+]*)\)",str(title[i]))
		else:
			name = re.findall("([\w+\b \b]*)\W\(([\w+\W+]*)\)|([\w+\b \b]*)\-\W\(([\w+\W+]*)\)",str(title[i]))
		rating[i]+=" out of 5"
		price[i]="₹"+price[i]
		try:
			if len(name[0])<2:
				dit[name[0][0]]=["", link[i], images[i], price[i], rating[i]]
			else:
				dit[name[0][0]]=[name[0][1], link[i], images[i], price[i], rating[i]]
		except:
			print("",end="")
	return dit

