@sanity
Feature: BLC Course
Scenario Outline: Upload BLC Course
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Wait for 3 seconds
    And Click on 'BLC Courses' button
    And Wait for 3 seconds
    And Click on 'Upload Courses' button
    And Wait for 3 seconds
    And Enter '<course name>' as text for 'Course Name'
    And Wait for 2 seconds
    And Enter '<cohort id>' as text for 'Enter Cohort'
    And Wait for 2 seconds
    And Select '<cohort id>' in the 'Enter Cohort' list
    And Click on 'Enter Course Sub Tag' dropdown
    And Select '<course sub tag>' in the 'course sub tag' list
    And Enter '<csv file path>' as text for 'Browse'
    And Click on 'Upload' button
    Then Validate 'table column' having '<course name>' is displayed
    And Click on 'BLC Courses' button
    And Validate 'column' having '<course name>' is displayed
    And Wait for 2 seconds


    #Below table has the test data used by above script
    Examples: TestData
    |course name       | cohort id| course sub tag| csv file path|
    |Auto<dynamic>     | 262      | Regular       | /Users/sanjeshsalecha/Automation/rawtopics.csv|



