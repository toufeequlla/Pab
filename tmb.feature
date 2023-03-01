Feature: Add TMB

  Scenario Outline: Adding tmb
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And Click on 'Tmb' button
    And Click on 'Create new tmb' button
    And Click on 'Class Type' button
    And Select 'Regular' in the 'Class Type' list
    And Enter '<tmb_name>' as text for 'Name'
    And Click on 'Grade' button
    And Wait for 2 seconds
    And Select '<grade>' in the 'Grade' list
    And Enter '<slide_id>' as text for 'Slide'
    And Click on 'Save' button
    And Wait for 5 seconds
    Then Validate 'table column' having '<tmb_name>' is displayed
    And Click on 'TMB ID' button for '<tmb_name>'
    And Click on 'Edit' button
    And click on 'Status' dropdown
    And Select 'Published' in the 'Status' list
    And click on 'Save to publish' button
    And Wait for 5 seconds
#    And Wait

    Examples: TestData
  |   tmb_name  | grade       |  slide_id |
  |AutoTMB<dynamic>  | Standard VII|    config:data>slide_id   |
  # |AutoTMB41  | Standard VII|    1340  |
