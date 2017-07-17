#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  INTERSYS.py
#
#  Copyright 2017 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.


import datetime, time, unittest,HtmlTestRunner,xmlrunner
from selenium import webdriver
from colorama import init,Fore, Back, Style
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException



class  Intersys(unittest.TestCase):
    init(autoreset=True)
    print(Back.GREEN + Fore.WHITE + "\n<================================ COMPANY =================================>")
    print(Fore.GREEN + "-------------------------------------------------------------------------------")
    print(Fore.MAGENTA + """                        TEST CASE #1
                """)
    def setUp(self):

        #Go to https://www.intersysconsulting.com/   
        print ("TEST IN PROGRESS")
        self.driver = webdriver.Chrome("C:\Python27\dr_src\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.intersysconsulting.com")
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True


##### CONECTA AL WEB SERVER DE SELENIUM PARA TRABAJO REMOTO #####

        # self.driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:4444/wd/hub',
        #    desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver.get("http://192.168.1.254")
        # self.driver.implicitly_wait(30)

    def test_1_Magnifying_glass(self):
                 #Hit on the magnifying glass
                 driver = self.driver
                 try:
                     self.search_field = self.driver.find_element_by_xpath('//*[@id="searchToggle"]/i').click()
                     time.sleep(3)
                 except NoSuchElementException:
                     self.assertTrue(self.search_field, "Fail.... ")
                     st = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H;%M")
                     file_name = "TC1_test_Magnifying_glass" + st + ".png"
                     driver.save_screenshot(file_name)
                     raise
                 finally:
                     print("Fail")

    def test_2_Subscription_Services(self):
                 #Capture “Subscription Services” on search box and hit enter
                 driver = self.driver
                 try:
                     self.search_field = self.driver.find_element_by_xpath('//*[@id="searchToggle"]/i').click()
                     time.sleep(3)
                     self.driver.find_element_by_xpath('//*[@id="searchBar"]/form/div/input').send_keys("Subscription Services")
                     time.sleep(3)
                     self.search_field = self.driver.find_element_by_xpath('//*[@id="searchBar"]/form/button').click()
                     time.sleep(3)
                 except NoSuchElementException:
                     self.assertTrue(self.search_field, "Fail.... ")
                     st = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H;%M")
                     file_name = "TC1_Subscription_Services" + st + ".png"
                     driver.save_screenshot(file_name)
                     raise
                 finally:
                     print("Fail")

    def test_3_Assert_equals(self):
                 #Assert the content for element with id ‘menu-footer-menu’ equals the string ‘Company’
                 driver = self.driver
                 try:
                     self.search_field = self.driver.find_element_by_xpath('//*[@id="searchToggle"]/i').click()
                     time.sleep(3)
                     self.driver.find_element_by_xpath('//*[@id="searchBar"]/form/div/input').send_keys("Subscription Services")
                     time.sleep(3)
                     self.search_field = self.driver.find_element_by_xpath('//*[@id="searchBar"]/form/button').click()
                     time.sleep(3)
                     company = "https://www.intersysconsulting.com/company/"
                     self.compan = self.driver.find_element_by_id('menu-footer-menu')
                     time.sleep(3)
                 except NoSuchElementException:
                     self.assertTrue(self.search_field, "Fail.... ")
                     self.assertequal(self.company, compan, "Error not equal............ ")
                     st = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H;%M")
                     file_name = "TC1_Assert_equals" + st + ".png"
                     driver.save_screenshot(file_name)
                     raise
                 finally:
                     print("Fail")  

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    print(Fore.YELLOW +"\t\t ==== Test in progress ====\n")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='intersys_tc1'),failfast=False, buffer=False, catchbreak=False,verbosity=2)
    testRunner=xmlrunner.XMLTestRunner(output='tc-reports')

