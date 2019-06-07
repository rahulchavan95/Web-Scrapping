import os
import bs4
import requests
from sys import *
from urllib.request import urlopen
from urllib.parse import urlparse


def is_downloadable(url):
	h=requests.head(url,allow_redirects=True)
	header=h.headers
	content_type=header.get('content-type')
	
	if 'text' in content_type.lower():
		return False

	if 'html' in content_type.lower():
		return False

	return True


def get_filename_from_cd(cd):
	a=urlparse(cd)

	return os.path.basename(a.path)

def Download(url):

	url="http:" +url
	allowed=is_downloadable(url)

	if allowed:
		try:
			res=requests.get(url,allow_redirects=True)
			res.raise_for_status()
			filename=get_filename_from_cd(url)

			fd=open(filename,'wb')
	
			for buffer in res.iter_content(1024):
				fd.write(buffer)
			

			fd.close()
			return True

		except Exception as E:
			return False

def WebScrapper(url):
	try:
		connection=urlopen(url)
		raw_html=connection.read()

		connection.close()
	
		page_soup=bs4.BeautifulSoup(raw_html,"html.parser")
	
		container=page_soup.find_all("div",{"class":"item-container"})
	
		for elements in container:
			ret=Downolad(elements.a.img['data-src'])
			if ret==False:
				break
	
		return ret

	except Exception as E:
		return False


def main():
		
	print("File Downloader")

	url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=Video%20card"
	try:
		bret=WebScrapper(url)
		if bret==True:
			print("Files successfully download")

		else:
			print("Files successfully download")


	except Exception:
		print("Failed to download")


if __name__=="__main__":
	main()






















