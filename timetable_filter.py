from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin
from behave import *

class Timetable_Filter:
    weblink = "https://blc-apps.stage.tllms.com"

    btn_cmslogin = "//span[contains(text(),'LOGIN')]"
    btn_login = "//form[@action='.']//div//div//div//div//button"
    btn_sign_in = '//*[@id="signInForm"]/div[4]/button'
    txt_email = '//*[@id="identifierId"]'
    txt_cmsemail = '//*[@id="email"]'
    btn_next = '//*[@id="identifierNext"]/div/button'
    txt_password = '//*[@id="password"]/div[1]/div/div[1]/input'
    txt_cmspassword = '//*[@id="password"]'
    btn_passwordnext = '//*[@id="passwordNext"]/div/button'
    txt_searchbox = "//input[contains(@placeholder,'Search Batch')]"
    btn_launch='//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div/span/button'
    btn_searchdropdown='//*[@id="real-canvas"]/div[40]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'

    btn_email="//div[contains(@data-email,'btc_automation@byjus.com')]"
    btn_nextpage = '//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[3]/div/ul/li[4]/a'
    ele_paid_batches_app = "//div[contains(text(),'Paid Batches-Stage')]"
    btn_search = "//button[text()='Search']"
    batchname="//textarea[contains(text(),'Standard_VIII_155_CBSE_Mumbai_Kalyan_mumbai_2_2022')]"

    btn_rowsdropdown='//*[@id="real-canvas"]/div[23]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]'
    btn_100rows='//*[@id="react-select-4-option-2"][text()="100"]'
    btn_batchstatusdropdown='//*[@id="real-canvas"]/div[36]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'

    btn_actionslot = '//*[@id="real-canvas"]/div[1]/div/div/div[1]/div/div/div/table/tbody/tr/td[15]/div/button[2]'

    btn_enddate = '//div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/div/input'
    btn_all_dates = "//div[@class='react-datepicker__month']/div/div[contains(text(),'[text]')]"
    btn_edclan ='//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[text()=30]'
    btn_update ='//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[5]/div/div/div[1]/div/div/button'
    btn_effectivedate= '//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[18]/div/div/div[1]/div/div/div[1]/div/input'
    btn_eftdatesel= '//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[18]/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[6]'
    btn_radioclick= "//input[@type='radio']"
    btn_topicdrop= '//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[19]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    dd_topicvalue="//html/body/div[2]/div/div/div[contains(text(),'[text]')]"
    txt_topicdrop='//div[3]/div/div/div[2]/div/div[19]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input'
    ele_successfully_updated_batch_start_date = '//div[contains(text(),"slot updated successfully at UXOS for transferBatch batch 11137")]'
    ele_timetable_app = "//div[contains(text(),'Timetable-Stage')]"
    btn_first_page = '/html/body/div/div[1]/div/div/div/div/div[2]/div/div[3]/div/ul/li[3]/a'

    btn_launch = "//div[contains(text(),'[text]')]/parent::div/parent::div/div[3]/div/div/div/span/button[contains(text(),'Launch')]"

    ele_timetable_app = "//div[contains(text(),'Timetable-Stage')]"






    btn_modal_update = "//div[@class='modal-content modal-component']//button[contains(text(),'Update')]"

    btn_pencil = '//*[@id="real-canvas"]/div[1]/div/div/div[1]/div/div/div/table/tbody/tr/td[15]/div/button[2]'

    btn_startdate = "//div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/input"
    ele_startdate = "//div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div/input"
    txt_enddate = "//div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/div/input"
    btn_enddate = "//div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/div/input"

    btn_all_dates = "//div[@class='react-datepicker__month']/div/div[contains(text(),'[text]')]"
    btn_subject_sequence_radio = "//input[@type='radio']"
    ele_successfully_updated_batch_start_date = '//div[contains(text(),"slot updated successfully at UXOS for transferBatch batch 11061")]'

    # txt_tt_centre_drpdown = "//div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    txt_tt_centre_dropdown = "/html/body/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_tt_centre_name = "//html/body/div[2]/div/div/div[contains(text(),'[text]')]"
    txt_tt_batch_drpdown = "//div[1]/div/div/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_tt_batch_name = "//html/body/div[2]/div/div/div[contains(text(),'[text]')]"

    ele_october_month = "//span[contains(text(),'October 2022')]"
    ele_november_month = "//span[contains(text(),'November 2022')]"
    ele_december_month = "//span[contains(text(),'December 2022')]"

    ele_tt_start_sessions = "//a[contains(text(),'18')]/parent::div/parent::div/parent::div/div[2]/div[2]/div/div[contains(text(),'Mat...')]"
    ele_tt_end_sessions = "//a[contains(text(),'09')]/parent::div/parent::div/parent::div/div[2]/div[2]/div/div[contains(text(),'Mat...')]"

    ele_batch_updated_successfuly = "//div[contains(text(),'Batch updated successfully')]"

    btn_text = "//button[contains(text(),'[text]')]"

    btn_roombutton='//*[@id="canvas-a55309ae-d3c0-4304-888a-52c9f58fd88d"]/div[12]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]'












