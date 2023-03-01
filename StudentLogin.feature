@sanity
Feature: Student Login

#Scenario Outline: Student Join Online Class
#
#  Given Open "link" Portal using Chrome
#    When Click on 'login' button
#    And Enter '<mobileNumber>' as text for 'mobilenumber'
#    And Click on 'next' button
#    And Enter '<password>' as text for 'password'
#    And Click on 'next' button
#    And Wait for 2 seconds
#    And Click on 'homepagelogin' button
#    And Wait for 2 seconds
#    And Click on 'joinclass' button
#    And Wait for 2 seconds
#    And Enter 'Hello Sir' as text for 'inputchat'
#    And Click on 'sendmessage' button
#    And Click on 'reactionoption' button
#    And Wait for 2 seconds
#    And Click on 'likereaction' button
#    And Wait for 2 seconds
#    And Click on 'dotoption' using javascript
#    And Wait for 2 seconds
#    And Click on 'exit' button
#    And Click on 'exitclass' button
#    And Wait for 2 seconds
#    And Click on 'feedback' button
#    And Wait for 2 seconds
#    And Click on 'feedbacktwo' button
#    And Click on 'continue' button
#    And Wait for 2 seconds
#    And Click on 'feedback' button
#    And Click on 'feedbacktwo' button
#    And Click on 'submit' button
#    And Wait for 2 seconds
#
#
#
#  Examples: TestData
#    |mobileNumber                 | password                |
#    |config:login>mobileNumber    | config:login>password   |


#  Scenario Outline: Student Report an issue  Online Class
#
#  Given Open "link" Portal using Chrome
#    When Click on 'login' button
#    And Enter '<mobileNumber>' as text for 'mobilenumber'
#    And Click on 'next' button
#    And Enter '<password>' as text for 'password'
#    And Click on 'next' button
#    And Wait for 2 seconds
#    And Click on 'homepagelogin' button
#    And Wait for 2 seconds
#    And Click on 'joinclass' button
#    And Wait for 2 seconds
#    And Click on 'dotoption' button
#    And Click on 'reportissue' button
#    And Click on 'vedioissue' button
#    And Click on 'report' button
#    And Wait for 2 seconds
#
#
#
#  Examples: TestData
#    |mobileNumber                 | password                |
#    |config:login>mobileNumber    | config:login>password   |




#  Scenario Outline: Student Join Offline Class
#
#  Given Open "link" Portal using Chrome
#    When Click on 'login' button
#    And Enter '<mobileNumber>' as text for 'mobilenumber'
#    And Click on 'next' button
#    And Enter '<password>' as text for 'password'
#    And Click on 'next' button
#    And Wait for 2 seconds
#    And Click on 'homepagelogin' button
#    And Wait for 2 seconds
#    And Click on 'joinclass' button
#    And Wait for 2 seconds
#    And Click on 'dotoption' button
#    And Click on 'exit' button
#    And Click on 'exitclass' button
#    And Click on 'feedback' button
#    And Click on 'feedbacktwo' button
#    And Click on 'continue' button
#    And Wait for 2 seconds
#    And Click on 'feedback' button
#    And Click on 'feedbacktwo' button
#    And Click on 'submit' button
#    And Wait for 2 seconds
#
#
#  Examples: TestData
#    |mobileNumber                 | password                |
#    |config:login>mobileNumber    | config:login>password   |
#

#Scenario Outline: Student Verify Assessment
#
#  Given Open "link" Portal using Chrome
#    When Click on 'login' button
#    And Enter '<mobileNumber>' as text for 'mobilenumber'
#    And Click on 'next' button
#    And Enter '<password>' as text for 'password'
#    And Click on 'next' button
#    And Wait for 2 seconds
#    And Click on 'byjusclass' button
#    And Wait for 2 seconds
#    And Click on 'completedtab' button
#    And Wait for 2 seconds
#    And Click on 'firstresult' button
#    And Wait for 2 seconds
#
#
#  Examples: TestData
#    |mobileNumber                 | password                |
#    |config:login>mobileNumber    | config:login>password   |


#  Scenario Outline: Student Give Assessment
#
#  Given Open "link" Portal using Chrome
#    When Click on 'login' button
#    And Enter '<mobileNumber>' as text for 'mobilenumber'
#    And Click on 'next' button
#    And Enter '<password>' as text for 'password'
#    And Click on 'next' button
#    And Wait for 2 seconds
#    And Click on 'byjusclass' button
#    And Click on 'completedtab' button
#    And Wait for 2 seconds
#    And Click on 'start' button
#    And Click on 'examstart' button
#    And New window opens
#    And Click on 'startassessment' button
#    And Wait for 2 seconds
#    And Click on 'checkbox' button
#    And Click on 'exitassessment' button
#    And Wait for 2 seconds
#    And Switch to alert and click ok
#    And Wait for 2 seconds
#    #Assertions
#1305202813


#  Examples: TestData
#    |mobileNumber                 | password                |
#    |config:login>mobileNumber    | config:login>password   |


  Scenario Outline: Student verify Audio Vedio Settings

  Given Open "link" Portal using Chrome
   When Click on 'login' button
    And Enter '<mobileNumber>' as text for 'mobilenumber'
    And Click on 'next' button
    And Enter '<password>' as text for 'password'
    And Click on 'next' button
    And Wait for 2 seconds
    And Click on 'homepagelogin' button
    And Click on 'checkaudiovideo' button
    And Wait for 2 seconds
    And Count 'greensign' equals '3'
    And Wait for 2 seconds
    #Assertions
#1305202813


  Examples: TestData
    |mobileNumber                 | password                |
    |config:login>mobileNumber    | config:login>password   |


#  Given Launch BLC Portal using Chrome
#    When Enter Phone Number and Password and Login
#    Then Dashboard should be displayed
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And user click on like button
#
#  Scenario: Student Join Offline Class
#
#  Given Launch BLC Portal using Chrome
#    When Enter Phone Number and Password and Login
#    Then Dashboard should be displayed
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And click on like button

    # bootsrap
  # Nodejs
  # Angular
#  Scenario: Student Join Offline Class
#
#  Given Launch BLC Portal using Chrome
#    When Enter Phone Number and Password and Login
#    Then Dashboard should be displayed
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And click on like button
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And user click on like button

#  Scenario: Student Join Offline Class
#
#  Given Launch BLC Portal using Chrome
#    When Enter Phone Number and Password and Login
#    Then Dashboard should be displayed
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And click on like button


#  Scenario: CMS dropdown
#    Given Launch "https://blc-cms.stage.tllms.com/" Portal using Chrome
#    When Click on button with xpath '/html/body/div/div/div/a/span[1]'
#    And Enter email 'sanjesh.salecha@byjus.com' to textbox with id 'email'
#    And Click on button with xpath '//*[@id="signInForm"]/div[4]/button'
#    And Enter email 'sanjesh.salecha@byjus.com' to textbox with id 'identifierId'
#    And Click on button with xpath '//*[@id="identifierNext"]/div/button'
#    And Enter text 'P@ssword1' to textbox with xpath '//*[@id="password"]/div[1]/div/div[1]/input'
#    And Click on button with xpath '//*[@id="passwordNext"]/div/button'
#    And Click on button with xpath '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[6]/div[1]'
#    And Click on button with xpath '//*[@id="root"]/div/div[2]/div/div[1]/div/button'
#    And Click on button with xpath '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/div/div/div/div/div'
#    And Click on button with xpath '//*[@id="menu-"]/div[3]/ul/li[@data-value="Regular"]'
#    And Click on button with xpath '//*[@id="root"]/div/div[2]/div[3]/div/div[4]/div[1]/div/div/div/div/div/div'
#    And Click on button with xpath '//*[@id="menu-"]/div[3]/ul/li[@data-value="Physics"]'
#    And Click on button with xpath '//*[@id="root"]/div/div[2]/div[3]/div/div[8]/div[2]/div/div/div/div/button[2]'
#    #And Click on button with xpath '//*[@id=“mui-3537-popup"]/li/div/div[contains(text(),’ForceandMotionDoubtclarification_StandardVIII_CBSE’]'
#    #And Wait
#    And Get element source by xpath '//*[@class="MuiAutocomplete-listbox"]'
#    And Enter text 'StandardVIII' to textbox with xpath '//*[@placeholder="Enter TMB"]'
#    And Wait
#    And Click on button with xpath '//*[@class="MuiAutocomplete-listbox"]/li/div/div[text()="ForceandMotion_StandardVIII_CBSE"]'
#  #ForceandMotionDoubtclarification_StandardVIII_CBSE’]'
#    And Wait
#    And Get Page Source
#    And User click on join button
#    And User join the class
#    And user chat with tutor
#    And click on like button

    # bootsrap
  # Nodejs
  # Angular
  #featureset(Behave)
  #1020304010
  # report an issue
  #