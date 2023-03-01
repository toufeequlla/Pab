from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin

class BLC_Slides_Creation(CMSLogin):
    weblink = "https://blc-cms.stage.tllms.com/"
    btn_blc_slide = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[5]/div[1]'
    btn_new ='//*[@id="root"]/div/div[2]/div/div[1]/div[1]/div/button'
    txt_enter_slide_name = '/html/body/div[3]/div[3]/div[2]/input'
    btn_select_grade ='/html/body/div[3]/div[3]/div[2]/div/div[1]/div/div/div'
    dd_select_grade ='//*[@id="menu-"]/div[3]/ul/li[contains(text(),"[text]")]'
    btn_select_subject = '//html/body/div[3]/div[3]/div[2]/div/div[2]/div'
    dd_select_subject = '//*[@id="menu-"]/div[3]/ul/li[contains(text(),"[text]")]'
    btn_save = '//html/body/div[3]/div[3]/div[3]/div[1]'
    txt_video_id ='//html/body/div[4]/div[3]/div[3]/div[2]/input'
    btn_import = '//*[@id="root"]/div/div[1]/div/div[3]/div[2]/div'
    btn_add = '//html/body/div[4]/div[3]/div[3]/div[2]/button'
    btn_save_import_video = '//html/body/div[4]/div[3]/div[3]/div[4]/button[1]'
    btn_save_to_save_slide = '//*[@id="root"]/div/div[1]/div/div[3]/div[1]/div'
    btn_back = '//img[@alt="Back Icon"]'
    ele_table_column = '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/table/tbody/tr/td/div[text()="[text]"]'
    val_table_column = '//*[@id="root"]/div/div[2]/div/div[1]/div[4]/table/tbody/tr/td/div[text()="[text]"]/parent::*/parent::*/td[1]/div'

