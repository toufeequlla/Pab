from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin
from behave import *

class BMS_Batch:
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
    btn_launch='//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div/div[4]/div/div/div/span/button'
    btn_searchdropdown='//*[@id="real-canvas"]/div[40]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    btn_iddropdown="//div[2]/div/div/div[1][contains(text(),'Batch ID')]"
    btn_email="//div[contains(@data-email,'btc_automation@byjus.com')]"

    btn_search="//button[text()='Search']"
    batchname="//textarea[contains(text(),'Standard_VIII_155_CBSE_Mumbai_Kalyan_mumbai_2_2022')]"
    btn_centrename='//*[text()="Kalyan_mumbai"]'
    btn_coursealiasdropdown='//*[@id="real-canvas"]/div[14]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    btn_coursealiasname='//*[@id="react-select-3-option-1"][text()="Standard_VIII_CBSE_ALL_ALL_2_III"]'
    btn_rowsdropdown='//*[@id="real-canvas"]/div[23]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]'
    btn_100rows='//*[@id="react-select-4-option-2"][text()="100"]'
    btn_batchstatusdropdown='//*[@id="real-canvas"]/div[36]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    btn_active='//*[@id="react-select-5-option-0"][text()="ACTIVE"]'
    btn_inactive='//*[@id="react-select-5-option-1"][text()="INACTIVE"]'

    txt_centrename = "//div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_centrename = "//div[2]/div/div/div[1][contains(text(),'[text]')]"
    txt_destination_centrename = "//div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_destination_centrename = "//div[2]/div/div/div[contains(text(),'[text]')]"

    btn_plus = '//*[@id="real-canvas"]/div[1]/div/div/div[1]/div/div/div/table/tbody/tr[2]/td[15]/div/button[1]'
    btn_destplus = '//*[@id="real-canvas"]/div[1]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[15]/div/button[1]'
    btn_students = "//button[contains(text(),'Students')]"
    btn_checkbox = "//input[@title='Toggle Row Selected']"
    btn_transfer= "//button[contains(text(),'Transfer')]"
    btn_batch_id= "//td/div/span[contains(text(),'10365')]"
    btn_confirm= "//button[contains(text(),'Confirm')]"
    btn_back= "//button[contains(text(),'ᐸ')]"
    btn_link= "//a[contains(text(),'[text]')]"
    ele_link= "//a[contains(text(),'[text]')]"
    ele_selected_batch_details= "//textarea[contains(text(),'10365')]"
    ele_student_details_in_cms= "//div[contains(text(),'1434035278')]"
    ele_student_details_in_bms= "//div/span[contains(text(),'1434035278')]"

    ele_paid_batches_app ="//div[contains(text(),'Paid Batches-Stage')]"
    btn_add_slot_group = "//button[contains(text(),'Add slot group')]"
    btn_add_course_alias = "//button[contains(text(),'Add course alias')]"
    btn_update_centre = "//button[contains(text(),'Update Centre')]"
    btn_update = "//div[7]/div/div/div[1]/div/div/button[contains(text(),'Update')]"

    txt_cohort = "//div[3]/div/div/div[2]/div/div[11]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_cohort = "//div[2]/div/div/div[1][contains(text(),'[text]')]"

    btn_city_dropdown = '//*[@id="canvas-ebd12096-afc8-4cad-b3d1-33b3562a404a"]/div[16]/div/div/div[1]/div/div/div[2]/div/div/div'
    btn_centre_dropdown = '//*[@id="canvas-ebd12096-afc8-4cad-b3d1-33b3562a404a"]/div[17]/div/div/div[1]/div/div/div[2]/div/div/div'
    btn_duration = '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[10]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    txt_city= "//div[3]/div/div/div[2]/div/div[16]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/input"
    dd_city= "//ul/li/label/div/span[contains(text(),'[text]')]"

    txt_centre= "//div[3]/div/div/div[2]/div/div[17]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/input"
    txt_update_centre= "//div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_centre= "//ul/li[1]/label/div/span[contains(text(),'[text]')]"

    txt_duration= "//div[3]/div/div/div[2]/div/div[10]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    # dd_duration = "//div[3]/div/div/div[contains(text(),'[text]')]"
    dd_duration = '/html/body/div[2]/div/div/div[text()="[text]"]'
    btn_duration_option = "//div[3]/div/div/div[contains(text(),'4 Weeks')]"

    txt_phase = "//div/div[3]/div/div/div[2]/div/div[13]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_phase = '/html/body/div[2]/div/div/div[text()="[text]"]'

    # txt_phase= "//div/div[3]/div/div/div[2]/div/div[13]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    # dd_phase = "//div[3]/div/div/div[1][contains(text(),'[text]')]"

    btn_add= "//div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/button[contains(text(),'Add')]"
    ele_course_alias_created= "//div[contains(text(),'Course alias created')]"

    txt_abh_name= '//*[@id="canvas-c5571683-c586-42f9-95a4-d6ad0d219756"]/div[5]/div/div/div[1]/div/div/input'
    txt_abh_email= '//*[@id="canvas-c5571683-c586-42f9-95a4-d6ad0d219756"]/div[6]/div/div/div[1]/div/div/input'
    ele_centre_details_updated_successfully= "//div[contains(text(),'Centre details updated successfully')]"


    btn_add_city= "//button[contains(text(),'Add City')]"
    btn_submit= "//button[contains(text(),'Submit')]"
    txt_state = "//div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_state = "//div[2]/div/div/div[contains(text(),'[text]')]"
    txt_city_name = '//*[@id="canvas-0f50b23f-2afe-4ae4-a96b-3ec357b71d51"]/div[4]/div/div/div[1]/div/div/input'
    txt_city_code = '//*[@id="canvas-0f50b23f-2afe-4ae4-a96b-3ec357b71d51"]/div[6]/div/div/div[1]/div/div/input'
    ele_successfully_added_city = "//div[contains(text(),'Successfully added City')]"

    btn_delete_batches= "//button[contains(text(),'Delete Batches')]"
    btn_retrieve_batches= "//button[contains(text(),'Retrieve Batches')]"
    btn_delete="//div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/button[contains(text(),'Delete')]"
    ele_batch_status_updated_to_inactive = "//span[contains(text(),'Batch status updated to INACTIVE')]"
    ele_batch_status_updated_to_active = "//span[contains(text(),'Batch status updated to ACTIVE')]"
    btn_done = "//button[contains(text(),'Done')]"
    btn_retrieve = "//div[3]/div/div/div[1]/div/div/button[contains(text(),'Retrieve')]"






