import time
from datetime import date, datetime

import selenium
from behave import *

from Common.Enums import ElementIDType
from Common.FileOps import Json
from Common.PageElement import PageElement as PE



class tutorPortal:

    @staticmethod
    def suffixNumber(n):
         return str(n)+("th" if 4 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))

    @staticmethod
    def getDateAndDay():
        currentDate = date.today()
        dateWithSuffix = str(tutorPortal.suffixNumber(int(currentDate.strftime(("%d")))))
        return dateWithSuffix +" "+ currentDate.strftime("%B") + ", " + currentDate.strftime("%A")

@step('login to tutor Portal')
def Login(self):
        try:
            if self.driver.isElementDisplayed('//a[text()=\'Schedule Page\']', ElementIDType.XPATH):
                return
        except selenium.common.exceptions.NoSuchElementException:
            self.execute_steps('''When Click on 'Login' button 
                    And Enter 'config:login>email' as text for 'email'
                    And Click on 'Sign in' button
                    And Enter 'config:login>email' as text for 'google email'
                    And Click on 'next' button
                    And Wait for 2 seconds
                    And Enter 'config:login>password' as text for 'google password'
                    And Click on 'next' button
                    And Wait''')


@step('Check mic before run')
def micoff(self):
    try:
        if self.driver.isElementDisplayed("//div[@title ='Enable all students’ microphone (students need to unmute themselves)']",ElementIDType.XPATH) :
         self.driver.click("//div[@title ='Enable all students’ microphone (students need to unmute themselves)']/img[contains(@src,'/static/media/mic')]",ElementIDType.XPATH)
    except selenium.common.exceptions.NoSuchElementException:
     return

@step('Check cam before run')
def micoff(self):
    try:
        if self.driver.isElementDisplayed("//div[@title ='Turn on all students’ camera']",ElementIDType.XPATH) :
         self.driver.click("//div[@title ='Turn on all students’ camera']/img[contains(@src,'/static/media/cam')]",ElementIDType.XPATH)
    except selenium.common.exceptions.NoSuchElementException:
     return

@step("Enter email '{username}' and password '{password}' in student portal with '{userid}'")
def tutorPortalLogin(self, username, password, userid):
    className = self.feature.name.replace(" ", "_")
    if username.startswith("config:"):
        username = Json.get(self.config.userdata, username.split(":")[1])
    if password.startswith("config:"):
        password = Json.get(self.config.userdata, password.split(":")[1])
    self.driver.click('//span[contains(text(),\'LOGIN\')]', ElementIDType.XPATH)
    self.driver.enterData("//input[@id='enterNumber']", username, ElementIDType.XPATH)
    self.driver.click("//div[contains(text(),'NEXT')]", ElementIDType.XPATH)
    multipleAccountXpath = (PE.get(str("ele_" + "multiAccount"), className))
    isDisplayed = self.driver.elementAvailable(multipleAccountXpath)
    if isDisplayed:
        userid = Json.get(self.config.userdata, userid.split(":")[1])
        self.driver.click("//input[@value='" + userid + "']/following-sibling::span", ElementIDType.XPATH)
        self.driver.click("//div[contains(text(),'NEXT')]", ElementIDType.XPATH)
    self.driver.enterData("//input[@type='password']", password, ElementIDType.XPATH)
    self.driver.click("//div[contains(text(),'NEXT')]", ElementIDType.XPATH)
    time.sleep(5)


@step("open new tab with '{studentUrl}'")
def openNewTabforstudenyPortal(self, studentUrl):
    if studentUrl.startswith("config:"):
        studentUrl = Json.get(self.config.userdata, studentUrl.split(":")[1])
        self.driver.openNewTab(studentUrl)


@step("Validate '{element}' that is current day is displayed")
def validateDateAndDayOnTutorPortal(self, element):
    className = self.feature.name.replace(" ", "_")
    print("Class : " + className + " / textbox : ele" + element)
    text = tutorPortal.getDateAndDay()
    isDisplayed = self.driver.isElementDisplayed(
        PE.get("ele_" + element.replace(" ", "_").lower(), className).lower().replace("[text]", text),
        ElementIDType.XPATH)
    if isDisplayed:
        print(element + " is Displayed")
