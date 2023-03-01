Feature: Videos file

  Scenario: Uploading Videos
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Click on 'Videos' button with xpath '//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[7]/div[1]'
    And Click on button with xpath '//*[@id="root"]/div/div[2]/div[1]/div/button'
    And Wait