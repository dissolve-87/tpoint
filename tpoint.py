import sys

from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import os 

class Tpoint:
    def __init__(self):

        DRIVER_LOC = f'{os.getcwd()}/asseset/geckodriver'
        s=Service(DRIVER_LOC)
        self.driver = webdriver.Firefox(service=s)

    def PageMaker(self):
        self.driver.get("https://www.tutorialspoint.com/python")
        header = self.driver.find_element(By.ID,"header")
        self.driver.execute_script("""document.getElementById("header").remove()""", header)
        right_ads = self.driver.find_element(By.ID,"google-right-ads")
        self.driver.execute_script("""document.getElementById("google-right-ads").remove()""", right_ads)

        privacy_banner = self.driver.find_element(By.ID,"privacy-banner")
        self.driver.execute_script("""document.getElementById("privacy-banner").remove()""", privacy_banner)

        ebooks_grid = self.driver.find_element(By.ID,"ebooks_grid")
        self.driver.execute_script("""document.getElementById("ebooks_grid").remove()""", ebooks_grid)

        bottom_navigation = self.driver.find_element(By.ID,"bottom_navigation")
        self.driver.execute_script("""document.getElementById("bottom_navigation").remove()""", bottom_navigation)

        google_bottom_ads = self.driver.find_element(By.ID,"google-bottom-ads")
        self.driver.execute_script("""document.getElementById("google-bottom-ads").remove()""", google_bottom_ads)

        try:
            google_top_ads = self.driver.find_element(By.ID,"google-top-ads")
            self.driver.execute_script("""document.getElementById("google-top-ads").remove()""", google_top_ads)
        except Exception: pass

        footer = self.driver.find_element(By.ID,"footer")
        self.driver.execute_script("""document.getElementById("footer").remove()""", footer)

        left = self.driver.find_element(By.CLASS_NAME,"mui-col-md-3")
        self.driver.execute_script("""document.getElementsByClassName("mui-col-md-3")[0].remove()""", left)

            
        fullWidth = self.driver.find_element(By.CLASS_NAME,"mui-col-md-6")
        self.driver.execute_script("""document.getElementsByClassName("mui-col-md-6")[0].setAttribute("class","mui-col-md-12")""", fullWidth)



        try:
            tut_menu = self.driver.find_element(By.CLASS_NAME,"tutorial-menu")
            self.driver.execute_script("""document.getElementsByClassName("tutorial-menu")[0].remove()""", tut_menu)
        except Exception: pass

        try:
            pageBtn = self.driver.find_element(By.CLASS_NAME,"mui-container-fluid")
            self.driver.execute_script("""document.getElementsByClassName("mui-container-fluid")[1].remove()""", pageBtn)
        except Exception: pass


tp = Tpoint()
tp.PageMaker()

'''
mui-col-md-6 tutorial-content
            12
document.getElementsByClassName("mui-col-md-6")[0].setAttribute("class","mui-col-md-12")


document.getElementsByClassName("tutorial-content")[0]

ebooks_grid
alLinks = self.driver.find_elements_by_xpath("//a[@href]")

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