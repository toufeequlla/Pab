Feature: Free Campaigns

  Scenario Outline: Adding Free campaigns
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Click on 'Free Campaigns' button
    And Click on 'Add New' button
    And Enter '<name>' as text for 'Campaign Name'
    And Enter '<start_date>' as text for 'Start Date'
    And Enter '<end_date>' as text for 'End Date'
    And Click on 'Course List' button
    And select '<course_name>' in the 'Course List' list
    And Wait for 2 seconds
    #And Click on 'List' button
    And click on 'Submit' button
    And wait
    And Validate the 'table column' having the '<name>' is displayed




     Examples: TestData
  |   name     | start_date | end_date   | course_name |
  | Auto_Camp_<dynamic>  | 01/09/2022 | 30/09/2022 | free batch  |
