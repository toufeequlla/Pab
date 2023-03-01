from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class Raw_Topic(CMSLogin):
    weblink = "https://blc-cms.stage.tllms.com/"
    btn_raw_topic = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[6]/div[1]'
    btn_create_new_topic = '//*[@id="root"]/div/div[2]/div/div[1]/div/button'
    btn_class_type = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div'
    dd_class_type = '//*[@id="menu-"]/div[3]/ul/li[@data-value="Regular"]'
    txt_topic_name = '//input[@placeholder="Enter topic name"]'
    txt_topic_display_name = '//input[@placeholder="Enter topic display name"]'
    btn_subject = '//*[@id="root"]/div/div[2]/div[3]/div/div[4]/div[1]/div/div/div/div/div/div'
    dd_subject = '//*[@id="menu-"]/div[3]/ul/li[@data-value="[text]"]'
    btn_grade = '//*[@id=\'root\']/div/div[2]/div[3]/div/div[5]/div/div/div/div/div/div/div'
    dd_grade = '//*[@id="menu-"]/div[3]/ul/li[contains(text(),"[text]")]'
    btn_tmb = '//*[@id="root"]/div/div[2]/div[3]/div/div[8]/div[2]/div/div/div/div/button[2]'
    txt_tmb = '//*[@placeholder="Enter TMB"]'
    dd_tmb = '//*[@class="MuiAutocomplete-listbox"]/li/div/div[text()="[text]"]'
    btn_save = '//*[@id="root"]/div/div[2]/div[3]/div/div[9]/button'
    ele_table_column = '//*[@id="root"]/div/div[2]/div/div[2]/table/tbody/tr/td/div[text()="[text]"]'




