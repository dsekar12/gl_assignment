from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions import key_actions
from selenium.webdriver.common.actions import pointer_actions
import time
import wait
import unittest
import datetime
from selenium.common.exceptions import NoSuchElementException
import logging
from behave import *
import configparser

class CompanyTest():
    logging.basicConfig(filename='/usr/src/app/Test_Result/Test_Result.log',
                        format='%(asctime)s %(levelname)-8s %(message)s'
                        , level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    @given('Scenario-2')
    def company_banner(self):
        config = configparser.ConfigParser()
        config.read('/usr/src/app/config.ini')
        #logging.info(config.get('dev_environment','dev_wd_url'))
        baseURL = config.get('dev_environment','dev_wd_url')
        #'https://viewpoint.glasslewis.com/WD/?siteId=DemoClient'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(5)
        driver.get(baseURL)

        time.sleep(10)

#Search for the company in the search company text box
        Search_Company = driver.find_element_by_class_name("k-input")
        if Search_Company is not None:
            Search_Company.click()
            Search_Company.send_keys("Activision")
            time.sleep(5)
            Search_Company.send_keys(Keys.ENTER)

        time.sleep(5)

#Validate the top banner in the “Activision Blizzard Inc” vote card page
        Company_Banner = driver.find_element(By.ID, "detail-issuer-name")
        getcompany = Company_Banner.text
        if Company_Banner is not None:
            logging.info('PASS: Company Banner found and the company name is displayed as '+ getcompany)
            logging.info('PASS: SECOND TEST FOR TOP BANNER VERIFICATION PASSED SUCCESSFULLY AS IT MEETS THE ACCEPTANCE CRITERIA')
        else:
            logging.error('FAIL: Company Banner not found')
            screenshot_time = \
                datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'
                                                                      )
            filename = '/usr/src/app/Test_Result/Country_Filter_Not_Found_' + screenshot_time \
                       + '.png'
            driver.save_screenshot(filename)

        time.sleep(1)

#Close the browser
        driver.close()

#Create instance of class and call the function
topbanner = CompanyTest()
topbanner.company_banner()

