Feature: Timetable Filter

  Scenario Outline: task
    Given Open "BMS" Portal using Chrome
    When login to BMS Portal
    And Click on 'nextpage' button
    And mouseHover on 'paid batches app'
    And Wait for 2 seconds
    And Click on 'launch' button for 'Paid Batches-Stage'
    And Wait
    And New window opens
    And Wait
    And Enter '<batch_name>' as text for 'searchbox'
    And Wait for 4 seconds
    And Click on 'search' button
    And Wait for 2 seconds
    And Click on 'actionslot' button
    And Wait for 2 seconds
    And Click on 'enddate' button
    And Wait for 2 seconds
    And Click on 'all dates' button for '<end_date>'
    And Wait for 2 seconds


    And Wait for 2 seconds
    And Click on 'radioclick' button

    And Wait for 2 seconds
    And Click on 'topicdrop' button
    And Enter '<raw_topic>' as text for 'topicdrop'
    And Wait for 2 seconds

    And Click on 'roombutton' button
    And Enter '<room_no>' as text for 'roombutton'
    And Wait for 4 seconds

    #And Click on 'update' button
    And Wait for 2 secondsThen Validate 'successfully updated batch end_date' is displayed
    And Wait for 2 seconds
    Then Validate 'Batch updated successfully' is displayed
    And switch to old window
    And Wait for 2 seconds
    And Click on 'first page' button
    And Wait for 2 seconds
    And mouseHover on 'timetable app'
    And Click on 'launch' button for 'Timetable-Stage'
    And Wait for 3 seconds


    And Next window opens
    And Enter '<Centre>' as text for 'tt centre dropdown'
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
    Then Validate 'October month' is displayed
    And Click on 'text' button for 'Next'
    Then Validate 'November month' is displayed
    And Click on 'text' button for 'Next'
    Then Validate 'December month' is displayed
    And Wait for 2 seconds
    Then Validate 'tt end sessions' list with count '01'
    And Wait for 2 seconds
    And switch to old window




    Examples: TestData
      | batch_name                                              |end_date| raw_topic               | Centre|room_no|
      | Standard_IX_15_CBSE_Port_Blair_Elegance_2_2022_9_6_5817 | 31    | [384050] - 35745 - power| Elegance| 1   |


