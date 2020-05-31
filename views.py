from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	res=""
	websites={}
	if request.method == 'POST' and 'run_script' in request.POST:
		from . import flipkart_scraping
		from . import ebay_scraping
		from . import paytm_mall_scraping
		from . import amazon_scraping
		prod=request.POST.get('name')
		res_flipkart=flipkart_scraping.scrape(str(prod))
		websites['Flipkart']=res_flipkart
		res_amazon=amazon_scraping.scrape(str(prod))
		websites['Amazon']=res_amazon
		#res_ebay=ebay_scraping.scrape(str(prod))
		#websites['Ebay']=res_ebay
		#res_paytm=paytm_mall_scraping.scrape(str(prod))
		#websites['paytm']=res_paytm
		return render(request, 'home.html', {'websites': websites})
	return render(request, 'home.html')
