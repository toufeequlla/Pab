
from Common.SeleniumDriverSetup import SeleniumSetup
from Common.WebDriver import WebDriver

browser = None
webDriverObject = WebDriver()

def before_all(context):
    context.driver = webDriverObject

