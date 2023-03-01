import unittest
from appium import webdriver

from AppTestCases import config


class AppiumDriverSetup():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.4',
        'deviceName': 'Android Emulator',
        'app': config.appName
    }

    @classmethod
    def setUp(self):
        # set up appium
        'desired_caps = {}'
        'desired_caps["app"] = config.appName'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=self.desired_caps)
        return self.driver

    @classmethod
    def tearDown(self):
        self.driver.quit()
