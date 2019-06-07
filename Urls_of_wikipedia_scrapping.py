import os
import bs4
import requests
from sys import *

def LinksDisplay(URL):

	res=requests.get(URL)
	print(type(res))

	soup=bs4.BeautifulSoup(res.text,'lxml')	
	print(type(soup))

	links=soup.find_all('a',href=True)
	return links

def main():

	print("this script is used to fetch URL from wikipedia")
	
	url="https://en.wikipedia.org/wiki/Python_(programming_language)"
	arr=LinksDisplay(url)

	print("links are\n")

	for element in arr:
		if '#' not in element['href']:
			print(element['href'])


if __name__=="__main__":
	main()
