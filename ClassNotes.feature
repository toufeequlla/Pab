Feature: Class Notes

  Scenario Outline: Create BLC slides
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Click on 'Class Notes' button
    And Click on 'Upload' button
    And Enter '<display_name>' as text for 'Display Name'
    And Click on 'Tnl Cohort id' dropdown
    #And Wait
    And Select '<tnl_cohort_id>' in the 'Tnl Cohort Id' list
    And Wait
    And Enter '/Users/sanjeshsalecha/Automation/classnotes.pdf' as text for 'File Upload'
    And Click on 'Submit' button
    Then Validate 'table column' having '<display_name>' is displayed
    #And Wait

    Examples: TestData
  |   display_name  | tnl_cohort_id  |
  | Auto_Hindi   |  155-tllms08hindimarketing-8th Grade - CBSE Hindi  |

