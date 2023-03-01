import os
import time

import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Common import Enums
from Common.Driver import Driver
from selenium.webdriver.common.by import By

from Common.Enums import ElementIDType
from Common.SeleniumDriverSetup import SeleniumSetup
from WebTestCases import config
import codecs


class WebDriver(Driver):
    def __init__(self):
        self.element = None
        browser = config.browser
        if browser == Enums.Browser.Chrome:
            self.driver = SeleniumSetup.selenium_driver(self)
            if self.driver is not None:
                print('driver acquired')

    def openPage(self, url, wait_time=15):
        print("Launching : " + url)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(wait_time)

    def getElementById(self, id, wait_time=5):
        self.element = self.driver.find_element_by_id(id)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByCss(self, css, wait_time=5):
        self.element = self.driver.find_element_by_css_selector(css)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByName(self, name, wait_time=5):
        self.element = self.driver.find_element_by_name(name)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByXPath(self, xpath, wait_time=5):
        for x in range(2):
            try:
                self.driver.implicitly_wait(15)
                self.element = self.driver.find_element(By.XPATH, xpath)
                break
            except selenium.common.exceptions.StaleElementReferenceException:
                time.sleep(1)
                print("StaleReferenceException")
            except:
                self.driver.refresh()
                print("some other problem while getting element")
                break

        return self.element

    def getElementsByXPath(self, xpath, wait_time=5):
        for x in range(2):
            try:
                time.sleep(1)
                self.driver.implicitly_wait(15)
                self.element = self.driver.find_elements(By.XPATH, xpath)
                break
            except selenium.common.exceptions.StaleElementReferenceException:
                time.sleep(1)
                print("StaleReferenceException")
            except:
                print("some other problem while getting element")
                break

        return self.element

    def getElementByLinkText(self, linktext, wait_time=5):
        self.element = self.driver.find_element_by_id(linktext)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByTagName(self, tagname, wait_time=5):
        self.element = self.driver.find_element_by_tag_name(tagname)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByClassName(self, classname, wait_time=5):
        self.element = self.driver.find_element(By.CLASS_NAME, classname)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def getElementByPartialLinkText(self, partiallinktext, wait_time=5):
        self.element = self.driver.find_element_by_id(partiallinktext)
        self.driver.implicitly_wait(wait_time)
        return self.element

    def click(self, element, idType):
        self.wait_for_element_to_be_clickable(element, idType)
        if idType == ElementIDType.XPATH:
            self.getElementByXPath(element).click()
        if idType == ElementIDType.ID:
            self.getElementById(element).click()
        if idType == ElementIDType.ClassName:
            self.getElementByClassName(element).click()
        return

    def clickBy(self, by, locator):
        self.driver.find_element(by, locator).click()

    '''
    Desc : Function to enter data
    element: element identifier
    data: text to enter
    idType : type of identifier as described in ElementIDType enum
    '''
    def enterData(self, element, data, idType):
        self.wait_for_element_to_be_clickable(element, idType)
        if idType == ElementIDType.XPATH:
            self.getElementByXPath(element).send_keys(data)
        if idType == ElementIDType.ID:
            self.getElementById(element).send_keys(data)
        if idType == ElementIDType.Name:
            self.getElementByName(element).send_keys(data)
        return

    def takeScreenshot(self, fileName):
        if config.screenshotpath is None or config.screenshotpath is '':
            config.screenshotpath = os.getcwd()
        print(config.screenshotpath + fileName)
        self.driver.save_screenshot(config.screenshotpath + fileName)

    def switchToNewWindow(self):
        handle = self.driver.window_handles[1]
        self.driver.switch_to.window(handle)
        self.driver.implicitly_wait(5)

    def switchToNextWindow(self):
        handle = self.driver.window_handles[2]
        self.driver.switch_to.window(handle)
        self.driver.implicitly_wait(5)

    def switchToOldWindow(self):
        handle = self.driver.window_handles[0]
        self.driver.switch_to.window(handle)
        #self.driver.switch_to.default_content()
        self.driver.implicitly_wait(10)

    def mouseHover(self, element, idType):
        element = self.getElementByXPath(element)
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()

    def getPageSource(self, filePath):
        file = codecs.open(filePath, "w", "utf-8")
        #file = open(filePath, 'w')
        file.write(self.driver.page_source)
        file.close()

    def getElementHtmlSource(self, element, filePath):
        file = open(filePath, 'w')
        element = self.getElementByXPath(element)
        file.write(element.get_attribute('outerHTML'))
        file.close()

    def WaitForElement(self, element, idType, timeout=15):
        try:
            if idType == ElementIDType.XPATH:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
            if idType == ElementIDType.ID:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
            if idType == ElementIDType.Name:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
            if idType == ElementIDType.ClassName:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        except TimeoutException:
            return False

    def isElementDisplayed(self, element, idType, timeout=15):
        try:
            if idType == ElementIDType.XPATH:
                return self.driver.find_element(By.XPATH, element).is_displayed()
            if idType == ElementIDType.ID:
                return self.driver.find_element(By.ID, element).is_displayed()
            if idType == ElementIDType.Name:
                return self.driver.find_element(By.NAME, element).is_displayed()
            if idType == ElementIDType.ClassName:
                return self.driver.find_element(By.CLASS_NAME, element).is_displayed()
        except TimeoutException:
            print(element + " :Not Found ..")
            return False

    def wait_for_locator_webdriver(self, locator_value, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            return False

    def wait_for_element_to_be_clickable(self, element, idType, timeout=15):
        try:
            if idType == ElementIDType.XPATH:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, element)))
            if idType == ElementIDType.ID:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, element)))
            if idType == ElementIDType.Name:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.NAME, element)))
            if idType == ElementIDType.ClassName:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, element)))
        except TimeoutException:
            return False
        except selenium.common.exceptions.StaleElementReferenceException:
            self.driver.refresh()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, element)))


    def switchToAlert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def exicute_script(self, element, idType):
        if idType == ElementIDType.XPATH:
            self.driver.execute_script("arguments[0].click();", self.getElementByXPath(element))

    def executeJS(self, js):
        self.driver.execute_script(js)
        self.driver.implicitly_wait(10)

    def assert_data(self, msg):
        self.driver.assertEqual(msg)

    def getText(self, element):
        return self.driver.find_element_by_xpath(element).text

    def refresh(self):
        self.driver.refresh()

    def acceptAlert(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def ActionControl(self):
        act = ActionChains(self.driver)
        act.send_keys(Keys.ESCAPE).perform()
        act.send_keys(Keys.ENTER)

    def mousetoelementAndSendText(self, element, text):
        element = self.getElementByXPath(element)
        hov = ActionChains(self.driver).move_to_element(element)
        # hov.click().send_keys(text)
        hov.send_keys(text)
        hov.perform()

    def openNewTab(self,url):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)

    def openNewTabforcms(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get("https://blc-cms.stage.tllms.com/")

    def openNewTabfortllms(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get("https://staging.tllms.com/admin/logistics/order_info?premium_account_id=1434035278")

    def assert_page_source(self, msg):
        self.driver.getPageSource().contains(msg)

    def gettitle(self):
        title = self.driver.title
        return title


    def elementAvailable(self,element):
        try:
            self.driver.find_element(By.XPATH, element)
            return True
        except selenium.common.exceptions.StaleElementReferenceException:
            return False
        except :
            return False
