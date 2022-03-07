import sys

from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import os 


DRIVER_LOC = f'{os.getcwd()}/asseset/geckodriver'
s=Service(DRIVER_LOC)

driver = webdriver.Firefox(service=s)
driver.get("https://www.tutorialspoint.com/python")
header = driver.find_element(By.ID,"header")
driver.execute_script("""document.getElementById("header").remove()""", header)
right_ads = driver.find_element(By.ID,"google-right-ads")
driver.execute_script("""document.getElementById("google-right-ads").remove()""", right_ads)

privacy_banner = driver.find_element(By.ID,"privacy-banner")
driver.execute_script("""document.getElementById("privacy-banner").remove()""", privacy_banner)

ebooks_grid = driver.find_element(By.ID,"ebooks_grid")
driver.execute_script("""document.getElementById("ebooks_grid").remove()""", ebooks_grid)

bottom_navigation = driver.find_element(By.ID,"bottom_navigation")
driver.execute_script("""document.getElementById("bottom_navigation").remove()""", bottom_navigation)

google_bottom_ads = driver.find_element(By.ID,"google-bottom-ads")
driver.execute_script("""document.getElementById("google-bottom-ads").remove()""", google_bottom_ads)

try:
    google_top_ads = driver.find_element(By.ID,"google-top-ads")
    driver.execute_script("""document.getElementById("google-top-ads").remove()""", google_top_ads)
except Exception: pass

footer = driver.find_element(By.ID,"footer")
driver.execute_script("""document.getElementById("footer").remove()""", footer)

left = driver.find_element(By.CLASS_NAME,"mui-col-md-3")
driver.execute_script("""document.getElementsByClassName("mui-col-md-3")[0].remove()""", left)

    
fullWidth = driver.find_element(By.CLASS_NAME,"mui-col-md-6")
driver.execute_script("""document.getElementsByClassName("mui-col-md-6")[0].setAttribute("class","mui-col-md-12")""", fullWidth)



try:
    tut_menu = driver.find_element(By.CLASS_NAME,"tutorial-menu")
    driver.execute_script("""document.getElementsByClassName("tutorial-menu")[0].remove()""", tut_menu)
except Exception: pass

try:
    pageBtn = driver.find_element(By.CLASS_NAME,"mui-container-fluid")
    driver.execute_script("""document.getElementsByClassName("mui-container-fluid")[1].remove()""", pageBtn)
except Exception: pass


'''
mui-col-md-6 tutorial-content
            12
document.getElementsByClassName("mui-col-md-6")[0].setAttribute("class","mui-col-md-12")


document.getElementsByClassName("tutorial-content")[0]

ebooks_grid
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

'''