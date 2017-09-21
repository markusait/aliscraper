import bs4
from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup


my_url = []

for x in range(10):
	my_url.append("https://de.aliexpress.com/category/2118/printers/" + str(x) + "html?site=deu&tag=")



for y in range(10):
	uClient = Ureq(my_url[y])
	page_html = uClient.read()
	uClient.close()


	page_soup = soup(page_html, "html.parser")
	#grabs each product
	#containers = page_soup.findAll("li",{"class":"list-item"})
	#filename = "printers.csv"
	#f = open(filename, "w")

	#headers ="brand,product_name, shipping, price_real\n"

	# f.write(headers)
	ullist = page_soup.findAll("div", {"class":"col-main"})
	error_p = page_soup.findAll("p", {"class":"ui-notice ui-notice-normal ui-notice-prompt"})
	error = []
	error.append(error_p)

	if error ==[[]]:
	        for ultag in ullist:
	            for litag in ultag.find_all("li"):
	                print (litag.text)
	else:
	    print("HeilHitler")
