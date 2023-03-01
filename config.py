from Common.Enums import Browser
import  os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

blc_url = 'https://learn.blc.integration.tllms.com/login'
browser = Browser.Chrome
logOutputDir = "/Users/mohamedtoufeequlla/Desktop/AutoT/"
screenshotpath = "/Users/mohamedtoufeequlla/Desktop/AutoT/"
courseData = PATH('../WebTestCases/BLC/Res/courseData.json')

env="stage"