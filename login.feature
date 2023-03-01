@sanity
Feature: Login

#Scenario: Open BLC Portal and Login
 # Given  Open "https://blc-cms.stage.tllms.com/login" Portal using Chrome
  #  When Click on button with xpath '/html/body/div/div/div/a/span[1]'
   # And Enter Mobile Number '1021029900' to textbox with id 'enterNumber'
    #And Take Screenshot as 'Logphone.png'
   # And Click on button with class name 'nextButtonLanding'
   # And Enter password 'password123' to textbox with id 'enterPassNumber'
   # And Take Screenshot as 'password.png'
   # And Click on button with class name 'nextButtonLanding'
   # Then Verify that element with class name 'MuiAvatar-root' is displayed
   # And Take Screenshot as 'Dashboard.png'

  Scenario: BMS Login
    Given Open "https://blc-apps.stage.tllms.com/login?redirectTo=/login" Portal using Chrome
    When login to BMS Portal
    And Wait
    And Move mouse over 'Batches-Stage' with xpath '//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div'
  #'//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div'
    And Click on button with xpath '//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/div/span/button'
  #'//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[4]/div/div/div/span/button'
    And Wait
    And New window opens
    And Wait
    And Click on button with xpath '//*[@id="real-canvas"]/div[4]/div/div/div[1]/div/button'
    And Click on button with xpath '//*[@class="real-canvas "]/div[13]/div/div/div[1]/div/div[1]/div[2]/div/div'
    And Wait
    #And Click on button with xpath '//*[@id="real-canvas"]/div[14]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'


    #And Click on button with xpath '//*[@id="real-canvas"]/div[14]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[text()="Standard_I_Demo_Bengaluru_ALL_2_III"]'
    And wait
  #//*[@id="app"]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div



  #'//*[@id="mui-16441"]'






