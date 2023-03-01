from abc import ABC, abstractmethod

class Driver(ABC):
    ''''@abstractmethod
    def __init__(self, appType , browser):
        pass'''

    @abstractmethod
    def openPage(self, url, wait_time):
        pass

    @abstractmethod
    def getElementById(self, id, wait_time):
        pass

    @abstractmethod
    def getElementByCss(self, css, wait_time=5):
        pass

    @abstractmethod
    def getElementByName(self, name, wait_time = 5):
        pass

    @abstractmethod
    def getElementByXPath(self, xpath, wait_time = 5):
        pass

    @abstractmethod
    def getElementsByXPath(self, xpath, wait_time = 5):
        pass

    @abstractmethod
    def getElementByLinkText(self, linktext, wait_time = 5):
        pass

    @abstractmethod
    def getElementByTagName(self, tagname, wait_time = 5):
        pass

    @abstractmethod
    def getElementByClassName(self, classname, wait_time=5):
        pass

    @abstractmethod
    def getElementByPartialLinkText(self, partiallinktext, wait_time = 5):
        pass

    @abstractmethod
    def click(self, element, idType):
        pass

    @abstractmethod
    def switchToNewWindow(self):
        pass

    @abstractmethod
    def switchToOldWindow(self):
        pass

    @abstractmethod
    def mouseHover(self, element, idType):
        pass

    @abstractmethod
    def isElementDisplayed(self, element, idType, timeout):
        pass

    @abstractmethod
    def acceptAlert(self):
        pass

    @abstractmethod
    def switchToAlert(self):
        pass

    @abstractmethod
    def exicute_script(self, element,idType):
        pass

    @abstractmethod
    def executeJS(self, js):
        pass

    @abstractmethod
    def getText(self,element):
        pass

    @abstractmethod
    def takeScreenshot(self, fileName):
        pass

    @abstractmethod
    def refresh(self):
        pass