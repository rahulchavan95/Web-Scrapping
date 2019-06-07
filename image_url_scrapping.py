import os
import bs4
import requests
from sys import *
from urllib.request import urlopen


def ImageUrlScrapper(url):

	connection=urlopen(url)
	raw_html=connection.read()

	connection.close()
	
	page_soup=bs4.BeautifulSoup(raw_html,"html.parser")
	
	container=page_soup.find_all("div",{"class":"item-container"})
	
	return container

def main():
	print("fetch image urls from given url")
	
	try:
		url="https://www.newegg.com/global/in-en/Video-Cards-Video-Devices/Category/ID-38?Tpk=Video%20card"

		listout=ImageUrlScrapper(url)

		print("urls of all images----\n")

		for elements in listout():
			print(elements.a.img['data-src'])	
			print()

	except Exception as E:
		print("invalid input",E)


if __name__=="__main__":
	main()
