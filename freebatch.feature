Feature: freebatch

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
    Examples: TestData
       | batch_name                                              |end_date| raw_topic               | Centre|room_no|
       | Standard_IX_15_CBSE_Port_Blair_Elegance_2_2022_9_6_5817 | 31    | [384050] - 35745 - power| Elegance| 1   |

