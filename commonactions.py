import time

import re
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from Common.Enums import *
from Common.PageElement import PageElement as PE
from Common.FileOps import Json
from WebTestCases import config
from TutorPortal import tutorPortal
import json



class CommonActions:
    flow = None

    def __init__(self):
        self.driver = None
        if self.driver is not None:
            print("Webdriver available")

    @step('Open "{weblink}" Portal using Chrome')
    def launchWebPage(self, weblink):
        weblink = PE.get("weblink", self.feature.name.replace(" ", "_"))
        print('Launch Web Portal : ' + weblink)
        self.driver.openPage(weblink)

    @step("Open the '{weblink}' Portal using Chrome")
    def launchWebPage(self, weblink):
        if weblink.startswith("config:"):
            weblink = Json.get(self.config.userdata, weblink.split(":")[1])
        print('Launch Web Portal : ' + weblink)
        self.driver.openPage(weblink)


    @step("Click on GIF with xpath '{xpath}'")
    @step("Click on BLC slides with xpath '{xpath}'")
    @step("Click on Class Notes with xpath '{xpath}'")
    @step("Click on New button with xpath '{xpath}'")
    @step("click on login")
    @step("Click on login button with xpath '{xpath}'")
    @step("Click on button with xpath '{xpath}'")
    @step("Click on Select Grade with xpath '{xpath}'")
    @step("Select Grade with xpath '{xpath}'")
    @step("Select Published with xpath '{xpath}'")
    @step("Select Subject with xpath '{xpath}'")
    @step("Select Class Type with '{xpath}'")
    def clickButtonWithXPath(self, xpath):
        self.driver.click(xpath, ElementIDType.XPATH)

    @step("Click on dropdown '{btnDesc}' with xpath '{xpath}'")
    @step("Select '{btnDesc}' with xpath '{xpath}'")
    @step("click on '{btnDesc}' button with xpath '{xpath}'")
    def clickButtonWithXPath(self, btnDesc, xpath):
        self.driver.click(xpath, ElementIDType.XPATH)

    @step("click on '{btnDesc}' with xpath '{xpath}'")
    def clickButtonWithXPath(self, btnDesc, xpath):
        self.driver.click(xpath, ElementIDType.XPATH)

    @step("click on '{btnDesc}' button for '{text}'")
    @step("Click on '{btnDesc}' dropdown")
    @step("click on '{btnDesc}' button")
    def clickButton(self, btnDesc, text=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / Button : btn_" + btnDesc)
        xpath = PE.get(str("btn_" + btnDesc.replace(" ", "_").lower()), className)
        if text is not None and "<dynamic>" in text:
            text = (self._config.dynamictestdata["'" + text + "'"]).strip("'")
        if xpath.startswith("js:"):
            self.driver.executeJS(xpath.split(":")[1])
        elif text == None:
            self.driver.click(xpath, ElementIDType.XPATH)
        else:
            if text != None:
                if text.startswith("config:"):
                    text = Json.get(self.config.userdata, text.split(":")[1])
                self.driver.click(xpath.replace("[text]", text), ElementIDType.XPATH)

    @step("select '{text}' in the '{list}' list")
    def selectText(self, text, list):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / list : dd_" + list)
        self.driver.click(PE.get(str("dd_" + list.replace(" ", "_").lower()), className).replace('[text]', text),
                          ElementIDType.XPATH)

    @step("Click on button with class name '{className}'")
    def clickButtonWithClassName(self, className):
        self.driver.click(className, ElementIDType.ClassName)

    @step("Enter email '{text}' to textbox with id '{id}'")
    @step("Enter Mobile Number '{text}' to textbox with id '{id}'")
    @step("Enter password '{text}' to textbox with id '{id}'")
    @step("Enter text '{text}' to textbox with id '{id}'")
    def setTextWithId(self, text, id):
        self.driver.enterData(id, text, ElementIDType.ID)

    @step("Enter '{desc}' '{text}' to textbox with xpath '{xpath}'")
    @step("Enter '{desc}' '{text}' with xpath '{xpath}'")
    def setTextWithXPath(self, desc, text, xpath):
        self.driver.enterData(xpath, text, ElementIDType.XPATH)

    @step("Enter '{text}' as text for '{txt_desc}'")
    def setText(self, txt_desc, text):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : txt_" + txt_desc)
        value = None
        print("text to be set : " + text)
        if "<dynamic>" in text:
            text = (self._config.dynamictestdata["'"+text+"'"]).strip("'")
        if text.startswith("config:"):
            print("inside if")
            try:

                if self.config.userdata is not None:
                    print("userdata :   " + str(self.config.userdata))
                    value = Json.get(self.config.userdata, text.split(":")[1])
                    if value is None:
                        value = Json.get(self.config.masterdata, text.split(":")[1])
                elif self.config.masterdata:
                    value = Json.get(self.config.masterdata, text.split(":")[1])
            except Exception as e:
                print("Error while reading config value: " + str(e))
                value = Json.get(self.config.masterdata, text.split(":")[1])
        if value is not None:
            text = value
        self.driver.enterData(PE.get("txt_" + txt_desc.replace(" ", "_").lower(), className), text, ElementIDType.XPATH)

    @step("Enter password '{text}' to textbox with name '{name}'")
    def setTextWithName(self, text, name):
        self.driver.enterData(name, text, ElementIDType.Name)
        time.sleep(5)

    @step("Take screenshot as '{filename}'")
    def takeScreenshot(self, filename):
        self.driver.takeScreenshot(filename)

    @step("Verify that element with class name '{className}' is displayed")
    def displayDashboard(self, className):
        try:
            self.driver.getElementByClassName("MuiAvatar-root").is_displayed()
            raise Exception("Login failed")
        except:
            pass

    @step("Enter '{email}' and '{password}' in Google SSO")
    @step("Enter email '{email}' and password '{password}' in Google SSO")
    def googleSSOLogin(self, email, password):
        time.sleep(10)
        self.driver.switchToNewWindow()
        # self.driver.enterData("identifierId", self.config['login']['username'], ElementIDType.ID)
        if email.startswith("config:"):
            email = Json.get(self.config.masterdata, email.split(":")[1])
        self.driver.enterData("identifierId", email, ElementIDType.ID)
        self.driver.click('//*[@id="identifierNext"]/div/button/span', ElementIDType.XPATH)
        # self.driver.enterData("password", self.config['login']['password'], ElementIDType.Name)
        self.driver.enterData("password", password, ElementIDType.Name)
        self.driver.click('//*[@id="passwordNext"]/div/button', ElementIDType.XPATH)
        time.sleep(5)
        self.driver.switchToOldWindow()

    @step("Wait for {seconds} seconds")
    def wait(self, seconds):
        time.sleep(int(seconds))

    @step("Wait")
    def wait(self):
        time.sleep(10)

    @step("Move mouse over '{element}' with xpath '{xpath}'")
    def moveMouse(self, element, xpath):
        self.driver.mouseHover(xpath, ElementIDType.XPATH)

    @step("Get Page Source")
    def getPageSource(self):
        self.driver.getPageSource(config.logOutputDir + "pageSource.html")

    @step("Get element source by xpath '{xpath}'")
    def getElementHtmlSource(self, xpath):
        self.driver.getElementHtmlSource(xpath, config.logOutputDir + "element.txt")

    @step("New window opens")
    def switchToNewWindow(self):
        self.driver.switchToNewWindow()

    @step("Next window opens")
    def switchToNextWindow(self):
        self.driver.switchToNextWindow()


    @step("Validate '{element}' with xpath '{xpath}' is displayed")
    def isElementDisplayed(self, element, xpath):
        isDisplayed = self.driver.isElementDisplayed(xpath, ElementIDType.XPATH)
        if isDisplayed:
            print(element + " is Displayed")
        else:
            print(element + " is not Displayed")
        assert isDisplayed == True

    @step("Validate '{element}' with Id '{id}' is displayed")
    def isElementDisplayedById(self, element, id):
        assert self.driver.isElementDisplayed(id, ElementIDType.ID) == True

    @step("Validate '{element}' with className '{className}' is displayed")
    def isElementDisplayedByClassName(self, element, className):
        assert self.driver.isElementDisplayed(className, ElementIDType.ClassName) == True

    @step("Switch to alert and click ok")
    def acceptAlert(self):
        self.driver.switchToAlert();

    @step("Click on '{btnDesc}' using javascript")
    def clickjs(self, btnDesc):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / Button : btn_" + btnDesc)
        self.driver.exicute_script(PE.get(str("btn_" + btnDesc.replace(" ", "_").lower()), className),
                                   ElementIDType.XPATH)

    @step("Count '{btnDesc}' equals '{number}'")
    def countAndVerify(self, btnDesc, number):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / Button : btn_" + btnDesc)

    @step("Validate '{element}' is displayed")
    @step("Validate the '{element}' having the '{text}' is displayed")
    @step("Validate '{element}' having '{text}' is displayed")
    @step("Validate '{element}' with '{data}' having '{text}' is displayed")
    @step("Validate '{element}' symbol is displayed")
    @step("Validate '{element}' button is displayed")
    @step("Validate '{element}' text is displayed")
    @step("validate '{element}' of '{text}' is displayed")
    def validateText(self, element, text=None, data=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : lbl_" + element)
        value = None

        if text is not None and '<dynamic>' in text:
            value = Json.get(self.config.dynamictestdata, text)
            if value is None:
                value = Json.get(self.config.dynamictestdata, text.strip('\''))
            if value is None:
                value = Json.get(self.config.dynamictestdata, "\'"+text+"\'")

        if text is not None and text.startswith("config:"):
            value = Json.get(self.config.userdata, text.split(":")[1])

        if value is None:
            value = text
        if value is None:
            elementxpath = PE.get("ele_" + element.replace(" ", "_").lower(), className)
        else:
            elementxpath = PE.get("ele_" + element.replace(" ", "_").lower(), className).replace("[text]", value.strip("\'"))

        isDisplayed = self.driver.isElementDisplayed(elementxpath, ElementIDType.XPATH)
        if isDisplayed and data is not None:
            self.config.userdata = json.dumps(
                    "\"data\":{\"" + data.replace(" ", "_") + "\":\"" + self.driver.getText(
                        PE.get("val_" + element.replace(" ", "_").lower(), className).lower().replace("[text]", value.strip("\'"))) + "\" }")
        elif isDisplayed:
            print(element + " is Displayed")
        else:
            print(element + " is not Displayed")
        assert isDisplayed == True

    @step("Validate the '{element}' having '{text1}' and '{text2}' is displayed")
    def validateElementWithText(self, element, text1=None, text2=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : ele_" + element)
        if text1.startswith("config:"):
            text1 = Json.get(self.config.userdata, text1.split(":")[1])
        if text2.startswith("config:"):
            text2 = Json.get(self.config.userdata, text2.split(":")[1])
        data = PE.get("ele_" + element.replace(" ", "_").lower(), className)
        # data = PE.get("ele_txt", className)
        data = data.replace("[text1]", text1)
        data = data.replace("[text2]", text2)
        isDisplayed = self.driver.isElementDisplayed(data, ElementIDType.XPATH)
        assert isDisplayed == True

    @step("Click on the '{element}' having '{text1}' and '{text2}' is displayed")
    def ClickOnElement(self, element, text1=None, text2=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : ele_" + element)
        if text1.startswith("config:"):
            text1 = Json.get(self.config.userdata, text1.split(":")[1])
        if text2.startswith("config:"):
            text2 = Json.get(self.config.userdata, text2.split(":")[1])
        # data = PE.get("ele_" + element.replace(" ", "_").lower(), className)
        data = PE.get("ele_txt", className)
        data = data.replace("[text1]", text1)
        data = data.replace("[text2]", text2)
        self.driver.click(data, ElementIDType.XPATH)

    @step("click on '{btnDesc}' button and Validate '{element}' is displayed")
    @step("click on '{btnDesc}' button and Validate '{element}' button is displayed")
    def clickButtonAndValidateButtonClicked(self, btnDesc, element, text=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / Button : btn_" + btnDesc)
        if text == None:
            self.driver.click(PE.get(str("btn_" + btnDesc.replace(" ", "_").lower()), className), ElementIDType.XPATH)
            isDisplayed = self.driver.isElementDisplayed(
                PE.get(str("btn_" + element.replace(" ", "_").lower()), className), ElementIDType.XPATH)
        else:
            self.driver.click(
                PE.get(str("btn_" + btnDesc.replace(" ", "_").lower()), className).replace("[text]", text),
                ElementIDType.XPATH)
            isDisplayed = self.driver.isElementDisplayed(
                PE.get(str("btn_" + element.replace(" ", "_").lower()), className).replace("[text]", text),
                ElementIDType.XPATH)
        if isDisplayed:
            print(element + " is Displayed")

    @step("write '{text}' on '{element}'")
    def validateDateAndDayOnTutorPortal(self, element, text=None):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : btn" + element)
        self.driver.click(PE.get(str("btn_" + element.replace(" ", "_")), className), ElementIDType.XPATH)
        time.sleep(10)
        self.driver.mousetoelementAndSendText(PE.get(str("btn_" + element.replace(" ", "_")), className), text)
        time.sleep(10)

    @step("Validate '{element}' functionality")
    def validateDateAndDayOnTutorPortal(self, element):
        className = self.feature.name.replace(" ", "_")
        print("Class : " + className + " / textbox : btn" + element)
        self.driver.click(PE.get(str("btn_" + element.replace(" ", "_")), className), ElementIDType.XPATH)


    @step("open new tab")
    def openNewTabforstudenyPortal(self):
        self.driver.openNewTab()

    @step("open new tab for CMS")
    def openNewTabforcms(self):
        self.driver.openNewTabforcms()

    @step("open new tab for TLLMS")
    def openNewTabfortllms(self):
        self.driver.openNewTabfortllms()

    @step("switch to old window")
    def switchToOldwWindow(self):
        self.driver.switchToOldWindow()

    @step("Refresh the page")
    def refresh(self):
        self.driver.refresh()

    @step("mouseHover on '{element}'")
    @step("mouseHover on '{element}' with '{text}'")
    def mousehover(self,element,text='None'):
        className = self.feature.name.replace(" ", "_")
        if text.startswith("config:"):
            text = Json.get(self.config.userdata, text.split(":")[1])
        data = PE.get("ele_" + element.replace(" ", "_").lower(), className)
        if text != None:
            data = data.replace("[text]", text)
        self.driver.mouseHover(data,ElementIDType.XPATH)

        @step("Validate '{element}' list with count '{text}'")
        def validateDateAndDayOnTutorPortal(self, element, text):
            className = self.feature.name.replace(" ", "_")
            xpath = PE.get("ele_" + element.replace(" ", "_").lower(), className)
            listn = len(self.driver.getElementsByXPath(xpath))
            assert listn == int(text)
            time.sleep(2)