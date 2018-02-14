from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

class AppleMainPage():
    def appleMainPageButtonInteractions(self):

        #################
        #   Locators    #
        #################
        _baseURL = "https://www.apple.com"
        _main_sub_pages_on_main_page = "//li[starts-with(@class,'homepage-section-item')]"

        chromeDriverLocation = "/Users/sergiiskarshevskyi/Documents/workspace_Python/SeleniumProject/lib/chromedriver"
        os.environ["webreiver.chrome.driver"] = chromeDriverLocation
        driver = webdriver.Chrome(chromeDriverLocation)
        driver.get(_baseURL)

        elements_list_on_main_page = driver.find_elements(By.XPATH, _main_sub_pages_on_main_page)
        length_of_elements_on_main_page = len(elements_list_on_main_page)

        for element in range(length_of_elements_on_main_page):
            elements_list_on_main_page[element].click()
            time.sleep(1)
            driver.back()
            elements_list_on_main_page = driver.find_elements(By.XPATH, _main_sub_pages_on_main_page)



chr_t = AppleMainPage()
chr_t.appleMainPageButtonInteractions()
