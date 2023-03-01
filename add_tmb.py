from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class Add_TMB(CMSLogin):
    weblink = "https://blc-cms.stage.tllms.com/"
    btn_tmb = '//*[@id=\'root\']/div/div[1]/div[2]/div/div/ul/div[8]/div'
    btn_create_new_tmb = '//*[@id=\'root\']/div/div[2]/div[1]/div/button'
    btn_class_type = '//*[@id=\'root\']/div/div[2]/div[3]/div[1]/div/div/div/div/div'
    dd_class_type = '//*[@id="menu-"]/div[3]/ul/li[text()="Regular"]'
    txt_name = '//*[@id="root"]/div/div[2]/div[3]/div[2]/div/div/input'
    btn_grade = '//*[@id="root"]/div/div[2]/div[3]/div[3]/div/div/div/div'
    dd_grade = '//*[@id="menu-"]/div[3]/ul/li[text()="Standard VII"]'
    txt_slide = '//*[@id="root"]/div/div[2]/div[3]/div[4]/div/div/input'
    btn_save = '//*[@id="root"]/div/div[2]/div[3]/footer/button'
    ele_table_column = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]'
    btn_tmb_id = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]/parent::*/parent::*/td[1]'
    btn_edit = '//*[@id="root"]/div/div[2]/div[3]/div[1]/div[2]/button[2]'
    btn_status = '//*[@id="root"]/div/div[2]/div[3]/div[6]/div/div'
    dd_status = '//*[@id="menu-"]/div[3]/ul/li[2]'
    btn_save_to_publish = '//*[@id="root"]/div/div[2]/div[3]/footer/button'


