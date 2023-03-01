Feature: Slot group
  Scenario Outline: update the end date
    Given Open "BMS" Portal using Chrome
    When login to BMS Portal
    And Wait for 5 seconds
    And mouseHover on 'timetable app' and click on launch button
    And Click on 'launch' button for 'Timetable-Stage'
    And Wait for 5 seconds
    And New window opens
    And Wait for 5 seconds
    And Enter '<Centre>' as text for 'tt centre drpdown'
    And Wait for 2 seconds
    And Select '<Centre>' in the 'tt centre name' list
    And Wait for 3 seconds
    And Enter '<batch_name>' as text for 'tt batch drpdown'
    And Wait for 2 seconds
    And Select '<batch_name>' in the 'tt batch name' list
    And Wait for 2 seconds
    And Click on 'text' button for 'Apply'
    And Wait for 2 seconds
    And Click on 'text' button for 'Month'
    And Wait for 2 seconds
    And Click on 'text' button for 'Next'
    And Click on 'text' button for 'Next'
    Then Validate 'December month' is displayed
    And Wait for 2 seconds
#    Then Validate 'tt end sessions' list with count '00'
    And switch to old window
    And mouseHover on 'paid batches app' and click on launch button
    And Wait for 2 seconds
    And Click on 'launch' button for 'Paid Batches-Stage'
    And Wait for 2 seconds
    And open new tab or switch to tab
    And Wait for 4 seconds
    And Enter '<batch_name>' as text for 'searchbox'
    And Wait for 4 seconds
    And Click on 'search' button
    And Wait for 5 seconds
#    And Click on 'pencil' button
#    And Wait for 5 seconds
#    And Click on 'enddate' button
#    And Wait for 2 seconds
#    And Click on 'all dates' button for '<end_date>'
#    And Wait for 4 seconds
#    And Click on 'subject sequence radio' button
#    And Click on 'modal update' button
#    And Wait for 1 seconds
#    Then Validate 'Batch updated successfully' is displayed
#    And open new tab or switch to tab
#    And Wait for 5 seconds
#    And Open "BMS" Portal using Chrome
#    And Wait for 5 seconds
#    And mouseHover on 'timetable app' and click on launch button
#    And Wait for 5 seconds
#    And Click on 'launch' button for 'Timetable-Stage'
#    And Wait for 5 seconds
    And New window opens
    And Wait for 5 seconds
#    And Enter '<Centre>' as text for 'tt centre drpdown'
#    And Wait for 2 seconds
#    And Select '<Centre>' in the 'tt centre name' list
#    And Wait for 3 seconds
#    And Enter '<batch_name>' as text for 'tt batch drpdown'
#    And Wait for 2 seconds
#    And Select '<batch_name>' in the 'tt batch name' list
#    And Wait for 2 seconds
    And Click on 'text' button for 'Apply'
    And Wait for 2 seconds
#    And Click on 'text' button for 'Month'
#    And Wait for 2 seconds
#    Then Validate 'October month' is displayed
#    And Click on 'text' button for 'Next'
#    Then Validate 'November month' is displayed
#    And Click on 'text' button for 'Next'
    Then Validate 'December month' is displayed
    And Wait for 2 seconds
    Then Validate 'tt end sessions' list with count '01'
    And Wait for 2 seconds
#    And switch to old window
    Examples: TestData
      | batch_name                                                      | end_date | Centre       |
      | Standard_VIII_14_CBSE_Bhubaneswar_Saheed_nagar_4_2022_11_9_bd33 | 10       | Saheed nagar |
