Feature: BMS Batch

#  Scenario Outline: Search Batch using Batch name and Batch ID search box from tooljet
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Wait for 2 seconds
#    And Click on 'launch' button
#    And Wait
#    And New window opens
#    And Wait
#    And Enter '<batch_name>' as text for 'searchbox'
#    And Wait for 4 seconds
#    And Click on 'search' button
#    And Wait for 5 seconds
#    Then Validate 'Table body' with xpath '//textarea[contains(text(),'Standard_VIII_155_CBSE_Mumbai_Kalyan_mumbai_2_2022')]' is displayed
#    And Wait
#    And Refresh the page
#    And Wait for 5 seconds
#    And Click on 'searchdropdown' button
#    And Wait for 5 seconds
#    And Click on 'id name dropdown' button
#    And Click on 'iddropdown' button
#     And Enter '<batch_id>' as text for 'searchbox'
#    And Wait for 4 seconds
#    And Click on 'search' button
#    And Wait for 5 seconds
#    Then Validate 'Table body' with xpath '//span[contains(text(),7615)]' is displayed
#    Examples: TestData
#      | batch_name                                                   |batch_id |
#      | Standard_VIII_155_CBSE_Mumbai_Kalyan_mumbai_2_2022_6_27_d0c4 |7615     |

#  Scenario: Search Batch using Center from tooljet
##    Given Open "BMS" Portal using Chrome
##    When login to BMS Portal
##    And mouseHover on 'paid batches app'
##    And Click on 'launch' button
##    And Wait
##    And New window opens
#    And Wait for 5 seconds
#    And Click on 'centredropdown' button
#    And Wait
#    And Click on 'centrename' button
#    And Wait for 5 seconds
#    Then Validate 'Table body' with xpath '//textarea[normalize-space()='Kalyan_mumbai']' is displayed
#    And Wait for 6 seconds
#    And Refresh the page
#
#  Scenario: Search Batch using Course Alias from tooljet
###    Given Open "BMS" Portal using Chrome
###    When login to BMS Portal
###    And mouseHover on 'paid batches app'
###    And Click on 'launch' button
###    And Wait
###    And New window opens
#    And Wait
#    And Click on 'coursealiasdropdown' button
#    And Wait for 5 seconds
#    And Click on 'coursealiasname' button
#    And Wait for 5 seconds
#    Then Validate 'Table body' with xpath '//textarea[normalize-space()='Standard_VIII_CBSE_ALL_ALL_2_III']' is displayed
#    And Wait for 6 seconds
#    And Refresh the page
#
#  Scenario: Filter the number of rows from tooljet
###    Given Open "BMS" Portal using Chrome
###    When login to BMS Portal
###    And mouseHover on 'paid batches app'
###    And Click on 'launch' button
###    And Wait
###    And New window opens
#    And Wait for 5 seconds
#    And Click on 'rowsdropdown' button
#    And Wait
#    And Click on '100rows' button
#    And Wait for 5 seconds
#    Then Validate 'Table body' with xpath '//tbody/tr[100]' is displayed
#    And Wait for 5 seconds
#    And Refresh the page
#
#  Scenario: Filter the ACTIVE/INACTIVE batches  from tooljet
###    Given Open "BMS" Portal using Chrome
###    When login to BMS Portal
###    And mouseHover on 'paid batches app'
###    And Click on 'launch' button
###    And Wait
###    And New window opens
#    And Wait
#    And Click on 'batchstatusdropdown' button
#    And Click on 'active' button
#    And Wait for 6 seconds
#    Then Validate 'Table body' with xpath '//td[contains(.,'ACTIVE')]' is displayed
#    And Click on 'batchstatusdropdown' button
#    And Click on 'inactive' button
#    And Wait for 4 seconds
#    Then Validate 'Table body' with xpath '//td[contains(.,'INACTIVE')]' is displayed
#    And Wait
#    And Refresh the page

  Scenario Outline: Add Course Alias
    Given Open "BMS" Portal using Chrome
   When login to BMS Portal
   And mouseHover on 'paid batches app'
    And Click on 'launch' button
   And Wait
    And New window opens
    And Wait for 5 seconds
    And click on 'add course alias' button
    And Wait for 5 seconds
    And Enter '<Cohort>' as text for 'cohort'
#    And Wait for 3 seconds
    And Select '<Cohort>' in the 'cohort' list
#    And Wait for 3 seconds
    And Click on 'city dropdown' button
    And Enter '<City>' as text for 'city'
    And Wait for 3 seconds
    And Select '<City>' in the 'city' list
    And Wait for 3 seconds
    And Click on 'city dropdown' button
    And Wait for 3 seconds
    And Click on 'centre dropdown' button
    And Wait for 3 seconds
    And Enter '<Centre>' as text for 'centre'
    And Wait for 2 seconds
    And Select '<Centre>' in the 'centre' list
    And Wait for 3 seconds
    And Click on 'centre dropdown' button
    And Wait for 3 seconds
#    And Click on 'duration' button
#    And Wait for 3 seconds
#    And Click on 'duration option' button
    And Enter '<Duration>' as text for 'duration'
    And Wait for 3 seconds
    And Select '<Duration>' in the 'duration' list
    And Wait for 2 seconds
    And Enter '<Phase>' as text for 'phase'
    And Wait for 5 seconds
    And Select '<Phase>' in the 'phase' list
    And Wait for 3 seconds
    And Click on 'add' button
    And Wait for 3 seconds
    Then Validate 'course alias created' is displayed
    And Wait for 6 seconds
    And Refresh the page

    Examples: TestData
      | Cohort               | City        | Centre       | Duration | Phase |
      |  | Bhubaneswar | Saheed nagar | 10 Weeks | IV    |

  Scenario Outline: Update Center
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Click on 'launch' button
#    And Wait
#    And New window opens
    And Wait for 5 seconds
    And click on 'update centre' button
    And Enter '<Centre>' as text for 'update centre'
    And Wait for 2 seconds
    And Select '<Centre>' in the 'destination centrename' list
    And Wait for 3 seconds
    And Enter '<ABH Name>' as text for 'abh name'
    And Wait for 3 seconds
    And Enter '<ABH Email>' as text for 'abh email'
    And Wait for 3 seconds
    And click on 'update' button
    And Wait for 2 seconds
    Then Validate 'centre details updated successfully' is displayed
    And Refresh the page

    Examples: TestData
      | Centre       | ABH Name        | ABH Email                 |
      | Saheed nagar | Jyotiprava Giri | jyotiprava.giri@byjus.com |

  Scenario Outline: Add City
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Click on 'launch' button
#    And Wait
#    And New window opens
    And Wait for 5 seconds
    And click on 'add city' button
    And Enter '<State>' as text for 'state'
    And Wait for 2 seconds
    And Select '<State>' in the 'state' list
    And Wait for 3 seconds
    And Enter '<City Name>' as text for 'city name'
    And Wait for 3 seconds
    And Enter '<City Code>' as text for 'city code'
    And Wait for 3 seconds
    And click on 'submit' button
    And Wait for 2 seconds
    Then Validate 'successfully added city' is displayed
    And Refresh the page

    Examples: TestData
      | State  | City Name | City Code |
      | Odisha | cuttack   | abcd    |

  Scenario Outline: Delete and Retrieve batches from tooljet
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Wait for 2 seconds
#    And Click on 'launch' button
#    And Wait
#    And New window opens
    And Wait
    And Click on 'searchdropdown' button
    And Wait for 2 seconds
    And Click on 'iddropdown' button
    And Enter '<batch_id>' as text for 'searchbox'
    And Wait for 4 seconds
    And Click on 'search' button
    And Wait for 5 seconds
    Then Validate 'Table body' with xpath '//span[contains(text(),10311)]' is displayed
    Then Validate 'Table body' with xpath '//td[contains(.,'ACTIVE')]' is displayed
    And Click on 'checkbox' button
    And Wait for 2 seconds
    And Click on 'delete batches' button
    And Wait for 2 seconds
    And Click on 'delete' button
    And Wait for 2 seconds
    Then Validate 'batch status updated to inactive' is displayed
    And Wait for 2 seconds
    And Click on 'done' button
    And Wait for 2 seconds
    And Refresh the page
    And Wait for 2 seconds
    And Click on 'batchstatusdropdown' button
    And Wait for 2 seconds
    And Click on 'inactive' button
    And Wait for 5 seconds
    Then Validate 'Table body' with xpath '//td[contains(.,'INACTIVE')]' is displayed
    And Wait for 2 seconds
    And Click on 'searchdropdown' button
     And Wait for 2 seconds
    And Click on 'iddropdown' button
    And Enter '<batch_id>' as text for 'searchbox'
    And Wait for 4 seconds
    And Click on 'search' button
    And Wait for 5 seconds
    Then Validate 'Table body' with xpath '//span[contains(text(),10311)]' is displayed
    Then Validate 'Table body' with xpath '//td[contains(.,'INACTIVE')]' is displayed
    And Click on 'checkbox' button
    And Wait for 5 seconds
    And Click on 'retrieve batches' button
    Then Validate 'Table body' with xpath ' //div[1]/div/div/div/div[contains(text(),'Are you sure you want to retrieve these batches ?')]' is displayed
    And Click on 'retrieve' button
    Then Validate 'batch status updated to active' is displayed
    And Click on 'done' button
    And Refresh the page
    And Click on 'searchdropdown' button
     And Wait for 2 seconds
    And Click on 'iddropdown' button
    And Wait for 5 seconds
    And Enter '<batch_id>' as text for 'searchbox'
    And Wait for 4 seconds
    And Click on 'search' button
    And Wait for 5 seconds
    Then Validate 'Table body' with xpath '//span[contains(text(),10311)]' is displayed
    Then Validate 'Table body' with xpath '//td[contains(.,'ACTIVE')]' is displayed

    Examples: TestData
      | batch_id |
      | 10311    |

  Scenario Outline: Batch transfer of a student
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And Move mouse over 'Paid Batches-Stage' with xpath '//div[contains(text(),'Paid Batches-Stage')]'
#    And Click on 'launch' button
#    And Wait
#    And New window opens
#    And Wait for 5 seconds
    And Enter '<centre>' as text for 'centrename'
    And Wait for 2 seconds
    And Select '<centre>' in the 'centrename' list
    And Wait for 3 seconds
    And Click on 'plus' button
    And Wait for 3 seconds
    And Click on 'students' button
    And Wait for 3 seconds
    And Click on 'checkbox' button
    And Wait for 3 seconds
    And Click on 'transfer' button
    And Wait for 3 seconds
    And Enter '<centre>' as text for 'destination centrename'
    And Wait for 3 seconds
    And Select '<centre>' in the 'destination centrename' list
    And Wait for 2 seconds
    And Click on 'batch id' button
    And Validate 'selected batch details' is displayed
    Then Click on 'confirm' button
    And Wait for 2 seconds
    Then Click on 'confirm' button
    And Wait for 30 seconds
    And Enter '<centre>' as text for 'centrename'
    And Wait for 2 seconds
    And Select '<centre>' in the 'centrename' list
    And Wait for 3 seconds
    And Click on 'destplus' button
    And Wait for 3 seconds
    And Click on 'students' button
    And Wait for 3 seconds
    Then Validate 'student details in bms' is displayed
    And Wait for 5 seconds
    And Click on 'back' button
    And Wait for 5 seconds
    Then open new tab for CMS
    When login to CMS Portal
    Then New window opens
    And Enter '<centre>' as text for 'centrename'
    And Wait for 2 seconds
    And Select '<centre>' in the 'centrename' list
    And Wait for 3 seconds
    And Click on 'plus' button
    And Wait for 3 seconds
    And click on 'link' button for '<course_id>'
    And Wait for 3 seconds
    And click on 'link' button for '<dest_batch_name>'
    And Wait for 3 seconds
    Then Validate 'student details in cms' is displayed
    And Wait for 3 seconds
    Then open new tab for TLLMS
    And Wait for 5 seconds
    Then validate 'link' of '<dest_batch_name>' is displayed
    And Wait for 6 seconds

    Examples: TestData
      | centre         | source_batch_id | dest_batch_id | course_id | dest_batch_name                                                |
      | BTC AUTOMATION | 10365           | 10279         | 3477      | Standard_IX_15_CBSE_Port_Blair_BTC_AUTOMATION_52_2022_9_1_9a62 |
