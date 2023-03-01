sanity
Feature: Login

Scenario: Open BLC Portal and Login
  Given  Open "https://blc-cms.stage.tllms.com/login" Portal using Chrome
    When Click on button with xpath '/html/body/div/div/div/a/span[1]'
   # And Enter Mobile Number '1021029900' to textbox with id 'enterNumber'
    #And Take Screenshot as 'Logphone.png'
   # And Click on button with class name 'nextButtonLanding'
   # And Enter password 'password123' to textbox with id 'enterPassNumber'
   # And Take Screenshot as 'password.png'