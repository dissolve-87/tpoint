import sys

from bs4 import BeautifulSoup as bs

from selenium import webdriver
import os 


DRIVER_LOC = f'{os.getcwd()}/asseset/geckodriver'
driver = webdriver.Firefox(executable_path=DRIVER_LOC)
driver.get("https://www.tutorialspoint.com/python/")
alLinks = driver.find_elements_by_xpath("//a[@href]")

VALID_LINKS = []



for tmp in alLinks:
    if ".com/python/" in str(tmp.get_attribute("href")) :
        #VALID_LINKS.append(str(tmp.get_attribute("href"))
        #print(str(tmp.get_attribute("href")))
        VALID_LINKS.append(str(tmp.get_attribute("href")))

result = []
[result.append(x) for x in VALID_LINKS if x not in result] 

for tm in result:
    print(tm)
        