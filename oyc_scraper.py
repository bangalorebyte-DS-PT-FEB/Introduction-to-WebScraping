#!/usr/bin/env python3.6

import requests # helps in sending HTTP requests to a webpage
from bs4 import BeautifulSoup # pulls data out of HTML files
import csv #helps read/write form CSV's

base_url = "https://oyc.yale.edu"
#target_url = 'https://oyc.yale.edu/political-science/plsc-114'

new_url = 'https://oyc.yale.edu/NODE/216'

r = requests.get(new_url) #send request to page // instead of urllib
#print(r)
	
content = r.content # render content from page
#print(content)
text = r.text # to extract text between tags, use .text
#print(text)

soup = BeautifulSoup(content, "html.parser") #parses html tags
#print(soup)


links = [] #create an empty list 
def collect_links():
	for link in soup.findAll('a'):	
		links.append((link.get('href')))
	remove_none = [x for x in links if x is not None]
	proper_links = [link for link in remove_none if "lecture" in link]
	full_links = [base_url + link for link in proper_links]
	print(full_links)

def write_to_csv():
	with open('oyc_links.csv', 'w') as csvfile:
		fieldnames = ['links']
		writer = csv.writer(csvfile)
		writer.writerow(fieldnames)# writing "links" in column header
		for i in collect_links():
			writer.writerow([i])
collect_links()
#write_to_csv()

