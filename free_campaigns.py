from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class Free_Campaigns(CMSLogin):
    weblink = 'https://blc-cms.stage.tllms.com/'
    btn_free_campaigns = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[10]'
    btn_add_new = '//*[@id="root"]/div/div[2]/div[3]/div[2]/button/div/div'
    txt_campaign_name = '//*[@id="root"]/div/div[2]/div[3]/div[2]/div/div/div/input'
    txt_start_date = '//*[@id="date-picker-inline"]'
    txt_end_date = '/html/body/div[1]/div/div[2]/div[3]/div[4]/div/div/div/div/input'
    btn_course_list = '//*[@id="mui-component-select-course"]'
    dd_course_list = '//*[@id="menu-course"]/div[3]/ul/li[@data-value="[text]"]/div[1]/span/span[1]/input'
    btn_list = '//*[@id="root"]/div/div[2]/div[3]/div[5]/label'
    #btn_submit = '//*[@id="root"]/div/div[2]/div[3]/div[6]/button[1]'
    btn_submit ='js:document.querySelector("button[label=\'Submit\']").click()'
    ele_table_column = '//*[@id="root"]/div/div[2]/div[4]/div/div[2]/div[text()="[text]"]'

#'//*[@id="root"]/div/div[2]/div[3]/div[5]/label' \
#'//*[@id="root"]/div/div[2]/div[3]/div[6]/button[1]'