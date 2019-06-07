import os
import bs4
import requests
from sys import *
from urllib.request import urlopen

def UrlScrapper(url):

	connection=urlopen(url)
	raw_html=connection.read()

	connection.close()
	
	page_soup=bs4.BeautifulSoup(raw_html,"html.parser")
	
	container=page_soup.find_all("a",{"class":"a-link-normal a-text-normal"})
	
	return container


def main():
	print("fetch urls from given url")
	
	try:
		url="https://www.amazon.in/b/?_encoding=UTF8&node=1389401031&ref_=sv_top_elec_mega_1"

		listout=UrlScrapper(url)

		print("url from website is\n")

		for elements in listout():
			print(elements['href'])	
			print()

	except Exception as E:
		print("invalid input",E)


if __name__=="__main__":
	main()
