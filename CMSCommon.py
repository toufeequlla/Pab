import selenium
from behave import *
from Common.Enums import *

class CMSCommon:
    @step('login to CMS Portal')
    def Login(self):
        try:
            if self.driver.isElementDisplayed('//*[@id="root"]/div/div[1]/div[2]/div/div/ul', ElementIDType.XPATH):
                return
        except selenium.common.exceptions.NoSuchElementException:
            self.execute_steps('''When Click on 'Login' button 
                    And Enter 'config:login>email' as text for 'email'
                    And Click on 'Sign in' button
                    And Enter 'config:login>email' as text for 'sign in email'
                    And Click on 'next' button
                    And Wait for 2 seconds
                    And Enter 'config:login>password' as text for 'password'
                    And Click on 'passwordNext' button
                    And Wait
                    And Refresh the page''')

