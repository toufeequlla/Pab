from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class BLC_Course(CMSLogin):
    weblink = "https://blc-cms.stage.tllms.com/"
    btn_blc_courses = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[1]/div[1]'
    btn_upload_courses = '//*[@id=\'root\']/div/div[2]/div[1]/div/button'
    txt_course_name = '//*[@id="root"]/div/div[2]/div[3]/div[2]/div/div/input'
    txt_enter_cohort = '//*[@id="root"]/div/div[2]/div[3]/div[3]/div/div/div/div/input'
    dd_enter_cohort = '/html/body/div[3]/div/ul/li[contains(text(),"[text]")]'
    #btn_enter_cohort = '/html/body/div[3]/div/ul/li[contains(text(),"[text]")]'
    btn_enter_course_sub_tag = '//*[@id="root"]/div/div[2]/div[3]/div[4]/div/div/div/div/div/div'
    dd_course_sub_tag = '//*[@id="menu-"]/div[3]/ul/li[contains(text(),"[text]")]'
    txt_browse = '//*[@id="csvContainer"]'
    btn_upload = '//*[@id="root"]/div/div[2]/div[3]/div[7]/button'
    ele_table_column = '//*[@id="root"]/div/div[2]/div[4]/div[2]/table/tbody/tr/td/div[contains(text(),"[text]")]'
    ele_column = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[contains(text(),"[text]")]'
