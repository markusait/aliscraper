import bs4
from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as soup

my_url = "https://de.aliexpress.com/category/2118/printers.html?spm=2114.30011908.2.111.JJr1uH"

uClient = UReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")
#grabs each product
containers = page_soup.findAll("li",{"class":"list-item"})
filename = "products.csv"
f = open(filename, "w")

headers ="brand,product_name, shipping, price_real\n"

# f.write(headers) mmmg

for container in containers:
	detail_container = container.div.div 
	title = detail_container.div.h3.a["title"]
	price_container = detail_container.findAll("div", {"class":"info"})
	price_real = price_container[0].span.span.text

	print("title: "	+ title)
	print("price_real: " + price_real)

	# f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "," + price_real + "\n")

# f.close()
