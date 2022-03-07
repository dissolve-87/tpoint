import sys

from bs4 import BeautifulSoup as bs

from selenium import webdriver
import os 


DRIVER_LOC = f'{os.getcwd()}/asseset/geckodriver'
driver = webdriver.Firefox(executable_path=DRIVER_LOC)
driver.get("https://www.tutorialspoint.com/python/")
header = driver.find_element_by_id("header")
driver.execute_script("""document.getElementById("header").remove()""", header)
right_ads = driver.find_element_by_id("google-right-ads")
driver.execute_script("""document.getElementById("google-right-ads").remove()""", right_ads)

privacy_banner = driver.find_element_by_id("privacy-banner")
driver.execute_script("""document.getElementById("privacy-banner").remove()""", privacy_banner)

ebooks_grid = driver.find_element_by_id("ebooks_grid")
driver.execute_script("""document.getElementById("ebooks_grid").remove()""", ebooks_grid)

bottom_navigation = driver.find_element_by_id("bottom_navigation")
driver.execute_script("""document.getElementById("bottom_navigation").remove()""", bottom_navigation)

google_bottom_ads = driver.find_element_by_id("google-bottom-ads")
driver.execute_script("""document.getElementById("google-bottom-ads").remove()""", google_bottom_ads)

footer = driver.find_element_by_id("footer")
driver.execute_script("""document.getElementById("footer").remove()""", footer)

left = driver.find_element_by_class_name("mui-col-md-3")
driver.execute_script("""document.getElementsByClassName("mui-col-md-3")[0].remove()""", left)


tut_menu = driver.find_element_by_class_name("tutorial-menu")
driver.execute_script("""document.getElementsByClassName("tutorial-menu")[0].remove()""", tut_menu)

fullWidth = driver.find_element_by_class_name("mui-col-md-6")
driver.execute_script("""document.getElementsByClassName("mui-col-md-6")[0].setAttribute("class","mui-col-md-12")""", fullWidth)
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