Feature: Raw Topic

  Scenario Outline: Create raw topic
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Click on 'Raw topic' button
    And Click on 'Create New Topic' button
    And Click on 'Class Type' button
    And Select 'Regular' in the 'Class Type' list
    And Enter '<topic_name>' as text for 'Topic Name'
    And Enter '<topic_display_name>' as text for 'Topic Display Name'
    And Click on 'Subject' dropdown
    And Select '<subject>' in the 'Subject' list
    And Click on 'Grade' dropdown
    And Wait for 3 seconds
    And Select '<grade>' in the 'Grade' list
    And Click on 'TMB' button
     #And Click on button with xpath '//*[@id="mui-3537-popup"]/li/div/div[contains(text(),'ForceandMotionDoubtclarification_StandardVIII_CBSE']'
    And Enter '<tmb_name>' as text for 'TMB'
    And Select '<tmb_name>' in the 'TMB' list
    #ForceandMotionDoubtclarification_StandardVIII_CBSE']'
    And Click on 'Save' button
    And Wait for 5 seconds
    Then Validate 'table column' having '<topic_name>' is displayed
    And Wait


    Examples: TestData
  |   topic_name  | topic_display_name  | subject | grade | tmb_name |
  | booster:<dynamic>       |  Chapter2             | Science | Standard VII | AutoTMB27 |

