from WebTestCases.BLC.PageFactory.CMSLogin import CMSLogin


class Gif(CMSLogin):
    weblink = 'https://blc-cms.stage.tllms.com/'
    btn_gif = '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[9]/div[1]'
    btn_upload_gif = '//*[@id="root"]/div/div[2]/div[1]/button/div/div'
    txt_name = '//*[@id="root"]/div/div[2]/div[3]/div[1]/div/div/input'
    btn_upload = '//*[@id="root"]/div/div[2]/div[3]/footer/button'
    txt_upload_gif = '//*[@id="gifContainer"]'
    ele_table_column = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]/parent::*/parent::*/td/div/div/a'
    btn_gif_id = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]/parent::*/parent::*/td/div/div/a'
    # btn_tmb_id = '//*[@id="root"]/div/div[2]/div[2]/table/tbody/tr/td/div[text()="[text]"]/parent::*/parent::*/td[1]'
    btn_edit = '//*[@id="root"]/div/div[2]/div[3]/div[1]/div[2]/button/div'
    btn_status = '//*[@id="root"]/div/div[2]/div[3]/div[2]/div/div/div/div/div'
    dd_status = '//*[@id="menu-"]/div[3]/ul/li[2]'
    btn_save_to_publish = '//*[@id="root"]/div/div[2]/div[3]/footer/button'




