
#Take input from the user and search product in the search tab in amazon website.
#print list of product names,price and rating in csv file.Do it for two pages.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
from itertools import zip_longest
import time
#from bs4 import BeautifulSoup
#import urllib.parser,urllib.open

driver=webdriver.Chrome("C:\\Python_ByteAc\\Selenium_Webdriver\\chromedriver.exe")
driver.get('http://www.amazon.co.in')
wait=WebDriverWait(driver,5)
assert "Amazon.in" in driver.title
#inp=input("Enter search keyword ")
#print(inp)
elem=driver.find_element_by_id('twotabsearchtextbox')
elem.send_keys("iphone")
elem.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source

products_list=[]
price_list=[]

def search_prodcut():
	products=driver.find_elements(By.XPATH,'//h2')
	print(products)
#links=driver.find_elements(By.XPATH,'//a[@class="a-size-base s-inline  s-access-title  a-text-normal"]')
							#//div[@class='item-inner']/span[@class='title']"

	for product in products:
		products_list.append(product.text)


	price_list_elem=driver.find_elements(By.XPATH,'//span[@class="a-size-base a-color-price s-price a-text-bold"]')
	for price in price_list_elem:
		price_list.append(price.text)

#rating_list=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]/i[@class="a-icon a-icon-star a-star-4"]/span[@class="a-icon-alt"]')
#for rate in rating_list:
#	print(rate.text)


def write_to_csv(products_list1,price_list1):
	with open("Amazon_ProductSearch.csv","w") as csvfile:
		fieldnames=['products_list','price_list','rating_list']
		writer = csv.writer(csvfile)
		writer.writerow(fieldnames)

		search_list = [products_list1, price_list1]
		export_data = zip_longest(*search_list, fillvalue = '')
		print(export_data)
		writer.writerows(export_data)


#driver.find_element(By.XPATH,'//span[@id="pagnNextString"]').click

search_prodcut()
write_to_csv(products_list,price_list)
#time.sleep(10)
#driver.find_element_by_link_text("Next Page").click
#driver.find_element(By.XPATH,'//span[@id="pagnNextString"]').click

#elem.click()
#time.sleep(10)
#search_prodcut()
#write_to_csv(products_list,price_list)
