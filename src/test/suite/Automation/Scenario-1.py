#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import datetime
from selenium.common.exceptions import NoSuchElementException
import logging
from behave import *
import configparser


class LoginTests(unittest.TestCase):
    logging.basicConfig(filename='/usr/src/app/Test_Result/Test_Result.log',
                        format='%(asctime)s %(levelname)-8s %(message)s'
                        , level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    @given('user is on the landing page of WD site')
    def webpage_display(self):
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
        driver.implicitly_wait(10)
        driver.implicitly_wait(3)
        driver.get(baseURL)
        try:
            CountryFilter = driver.find_element(By.XPATH,
                                                "//*[@id='filterid-CountryFilter']//h2[.='Country']"
                                                )
            # if CountryFilter is not None:
            logging.info('PASS: Country Filter Found in Web Disclosure site')
        except NoSuchElementException:
            logging.error('FAIL: Country Filter Not Found in Web Disclosure site'
                         )
            screenshot_time = \
                datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'
                                                                     )
            filename = '/usr/src/app/Test_Result/Country_Filter_Not_Found_' + screenshot_time \
                       + '.png'
            driver.save_screenshot(filename)
            raise


        try:
            Select_Belgium = driver.find_element(By.XPATH,
                                             "//*[@id='Belgium-cb-label-CountryFilter']")
            logging.info('PASS: Belgium Selected in Country Filter')
        except NoSuchElementException:
            logging.error('FAIL: Belgium Not Found in Country Filter'
                         )
            screenshot_time = \
                datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'
                                                                     )
            filename = 'Belgium_Country_Filter_Not_Found_In' + screenshot_time \
                       + '.png'
            driver.save_screenshot(filename)
            raise

        Select_Belgium.click()
        Select_Update = driver.find_element(By.ID, 'btn-update')
        if Select_Update is not None:
            Select_Update.click()
            time.sleep(10)
            logging.info('PASS: Update Button Found and Selected in Country Filter')
        else:
            logging.error('FAIL: Update Button Not Found Country Filter')
            screenshot_time = \
                datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'
                                                                     )
            filename = 'Update_Country_Button_Not_Found_In' + screenshot_time \
                       + '.png'
            driver.save_screenshot(filename)
        All_Rows = driver.find_elements_by_xpath('//table/tbody/tr')
        count_all_rows = str(len(All_Rows))
        # len method is used to get the size of that list
        logging.info('Number of rows detected in the grid is:' + count_all_rows)

        Is_All_Rows_Belgium = \
            driver.find_elements_by_xpath("//td[contains(text(),'Belgium')]"
                                          )
        count_Belgium = str(len(Is_All_Rows_Belgium))
        logging.info('Number of rows detected in the grid for Belgium:' + count_Belgium)


        if count_all_rows == count_Belgium:
            logging.info('PASS: Grid contains all the meetings for Belgium only')
        else:
            logging.info('FAIL: Grid not updated correctly for Belgium, meetings for countries other than Belgium are listed')
            screenshot_time = \
                datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'
                                                                     )
            filename = '/usr/src/app/Test_Result/Grid_Country_Filter_Count_Not_Matching' + screenshot_time \
                       + '.png'
            driver.save_screenshot(filename)
        # Close the browser
        driver.close()

start = LoginTests()
start.webpage_display()

