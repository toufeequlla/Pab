from behave import*

class Tutor_App:
    weblink = "https://blc-apps.stage.tllms.com/applications/tutor-stage"
    btn_login = "//form[@action='.']//div//div//div//div//button"
    btn_sign_in = '//*[@id="signInForm"]/div[4]/button'
    txt_email = '//*[@id="identifierId"]'
    btn_next = '//*[@id="identifierNext"]/div/button'
    txt_password = '//*[@id="password"]/div[1]/div/div[1]/input'
    btn_passwordnext = '//*[@id="passwordNext"]/div/button'

    btn_tutorportallaunch = '//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/div[4]/div/div/div/span/button'
    btn_addtutor = "//button[contains(text(),'Add tutor')]"
    btn_tutorcentredrpdown = '//*[@id="canvas-6a061174-2d42-49e2-8853-176b4821a6cb"]/div[12]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    btn_tutorcentrename = "//div[contains(text(),'Kalyan_mumbai')]"
    btn_tutoradd = '//*[@id="canvas-6a061174-2d42-49e2-8853-176b4821a6cb"]/div[4]/div/div/div[1]/div/div[contains(.,"Add")]'
    btn_tutorname = "//div[contains(text(),'[text]')]"
    txt_tutorcode = "//input[contains(@class,'form-control is-invalid validation-without-icon')]"
    dd_tutorname = "/html/body/div[2]/div/div/div[contains(text(),'[text]')]"
    btn_subject_drpdown = '//*[@id="canvas-6a061174-2d42-49e2-8853-176b4821a6cb"]/div[11]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    dd_subject = '//div[text()="<Subject>"]'

    txt_tutorname = '//div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[10]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input'
    txt_removetutorname = '//div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[8]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input'
    btn_remove_tutor = "//button[contains(text(),'Remove Tutor')]"
    btn_remove_tutor_centre_drpdown = '//*[@id="canvas-63eb353c-5ef2-4ed5-9fb4-976610752bd8"]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    btn_remove_tutor_centre_name = "//div[contains(text(),'Kalyan_mumbai')]"
    btn_remove_tutor_subject_drpdown = '//*[@id="canvas-63eb353c-5ef2-4ed5-9fb4-976610752bd8"]/div[6]/div/div/div[1]/div/div[1]/div[2]'
    btn_done = "//button[contains(text(),'Done')]"
    btn_remove = "//button[normalize-space()='Remove']"

    btn_replace_tutor = "//button[contains(text(),'Replace Tutor')]"
    btn_replace_tutor_centre_drpdown = '//*[@id="canvas-065ee768-76e8-4377-ba25-0eb8b7f77246"]/div[8]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    txt_centrename = "//div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[8]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input"
    dd_centrename = "//div[contains(text(),'[text]')]"
    # dd_centre_name = "/html/body/div[2]/div/div/div[contains(text(),'[text]')]"

    txt_originaltutorname = '//div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[6]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input'
    txt_replacementtutorname = '//div[1]/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[7]/div/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/input'
    btn_replace = "//div[11]/div/div/div[1]/div/div/button[contains(text(),'Replace')]"
