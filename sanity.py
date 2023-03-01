from behave import *

import Common.Utils
from Common.Enums import ElementIDType
from Common.WebDriver import WebDriver
from WebTestCases import config


class BLC():
    driver = None

    def __init__(self):
        self.driver = WebDriver()
        if self.driver is not None:
            print("Webdriver available")

    @step('Launch "{weblink}" Portal using Chrome')
    def LaunchWebPage1(self, context, weblink):
        print('Launch BLC Portal')
        print(context)
        self.driver.openPage(weblink)

    @step("Launch BLC Portal using Chrome")
    def LaunchWebPage(self):
        print('Launch BLC Portal')
        self.driver.openPage(config.blc_url)

    @step("Enter Phone Number and Password and Login")
    def Login(self):
        phoneNumber = '1021029900'
        password = 'password123'
        self.driver.click("//*[@id=\"root\"]/div/div/a/span[1]", ElementIDType.XPATH)
        self.driver.enterData("enterNumber", phoneNumber, ElementIDType.ID)
        self.driver.takeScreenshot('phoneNumber.png')
        self.driver.click("nextButtonLanding", ElementIDType.ClassName)
        self.driver.enterData("enterPassNumber", password, ElementIDType.ID)
        self.driver.click("nextButtonLanding", ElementIDType.ClassName)
        self.driver.takeScreenshot('password.png')

        try:
            self.driver.getElementByClassName("MuiAvatar-root").is_displayed()
            raise Exception("Login failed")
        except:
            pass

    @step("Dashboard should be displayed")
    def DisplayDashboard(self):
        self.driver.getElementByClassName("MuiAvatar-root").is_displayed()


@step("Enter Phone Number and OTP and Login")
def LoginWithOtp(self):
    phoneNumber = '1021029900'
    password = 'password123'

    self.driver.click("//*[@id=\"root\"]/div/div/a/span[1]", ElementIDType.XPATH)
    self.driver.enterData("enterNumber", phoneNumber, ElementIDType.ID)
    'self.driver.getElementById("enterNumber").send_keys(phoneNumber)'
    self.driver.takeScreenshot('phoneNumber.png')
    self.driver.click("nextButtonLanding", ElementIDType.ClassName)
    self.driver.enterData("enterPassNumber", Common.Utils.Util.GetOTP(phoneNumber, 'login', 'india'),
                          ElementIDType.ID)
    self.driver.click("nextButtonLanding", ElementIDType.ClassName)
    self.driver.takeScreenshot('password.png')

    try:
        self.driver.getElementByClassName("MuiAvatar-root").is_displayed()
        raise Exception("Login failed")
    except:
        pass
