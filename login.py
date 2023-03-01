from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin
class Login(CMSLogin):
    weblink = "https://blc-apps.stage.tllms.com/login?redirectTo=/login"
    btn_login = '//*[@id="app"]/div[1]/div/div/form/div/div/div/div/button'
