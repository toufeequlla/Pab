from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class Class_Notes(CMSLogin):
    weblink = "https://blc-cms.stage.tllms.com/"
    btn_class_notes = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[2]/div[1]'
    btn_upload = '//*[@id="root"]/div/div[2]/div[1]/div[2]/button'
    txt_display_name = '//*[@id="name"]'
    btn_tnl_cohort_id = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/div'
    dd_tnl_cohort_id = '//*[@id="menu-"]/div[3]/ul/li[10]'
    #text()="[text]"]'
    txt_file_upload =  '//*[@id="pdfContainer"]'
    btn_submit = '/html/body/div[3]/div[3]/div/div[2]/div[4]/button[2]/span[1]'
    ele_table_column = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]'
