import os
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import logging
from selenium.webdriver.chrome.options import Options


class SeleniumSetup:
    def __init__(self):
        self.driver = None

    def selenium_driver(self):

        # creating chrome instance
        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument("--disable-infobars")
        opt.add_argument('--start-maximized')
        opt.add_argument("no-sandbox")
        opt.add_argument("detach=true")
        opt.add_argument("user-data-dir="+os.path.expanduser("~/Library")+"/Application Support/Google/Chrome/Default")
        opt.add_argument('--incognito')
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })
        return webdriver.Chrome("/opt/homebrew/bin/chromedriver", options=opt)

        #return RemoteWebDriver(service.getUrl(), newChromeOptions());



