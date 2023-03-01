Feature: BLC Slides Creation

  Scenario Outline: Create BLC slides
    Given Open "CMS" Portal using Chrome
    When login to CMS Portal
    And Click on 'BLC Slide' button
    And Click on 'New' button
    And Wait for 5 seconds
    And Enter '<slide_name>' as text for 'Enter Slide Name'
    And Click on 'Select Grade' button
    And Wait
    #And Select Grade with xpath '//*[@id="menu-"]/div[3]/ul/li[contains(text(),"<grade>")]'
    And Select '<grade>' in the 'Select Grade' list
    And Click on 'Select Subject' button
    And Select '<Subject>' in the 'Select Subject' list
    And Click on 'Save' button
    And Click on 'Import' button
    And Enter '<video_id>' as text for 'video id'
    And Click on 'Add' button
    And Click on 'Save Import Video' button
    #And Click on 'Add New Slide' button with xpath '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div'
    And Click on 'Save to Save Slide' button
    And Wait for 3 seconds
    And Click on 'Back' button
    And Wait for 5 seconds
    Then Validate 'table column' with 'slide id' having '<slide_name>' is displayed

    And Wait for 5 seconds


    #Below table has the test data used by above script
Examples: TestData
  |   slide_name  | grade              |  video_id | Subject |
  |Auto<dynamic>      | Standard VII       |    498    | Science |
  #|Auto Slide 22  | Standard VII|    498    |

