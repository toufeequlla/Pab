Feature: Tutor App

  Scenario Outline: Add tutor from tooljet
    Given Open "BMS" Portal using Chrome
    When login to BMS Portal
    And Wait for 2 seconds
    And mouseHover on 'paid batches app'
    And Click on 'tutorportallaunch' button
    And Wait
    And New window opens
    And Wait for 3 seconds
    And Click on 'addtutor' button
    And Wait for 3 seconds
    And Click on 'tutorcentredrpdown' button
    And Wait for 2 seconds
    And Click on 'tutorcentrename' button
    And Wait for 2 seconds
    And Enter '<Tutor_Code>' as text for 'tutorcode'
    And Wait for 2 seconds
    And Click on 'subject drpdown' button
    And Wait for 2 seconds
    And Click on button with xpath '//div[text()="<Subject>"]'
    And Wait for 2 seconds
    And Enter '<Tutor>' as text for 'tutorname'
    And Wait for 5 seconds
    And Select '<Tutor>' in the 'tutorname' list
    And Wait for 5 seconds
    And Click on 'tutoradd' button
    And Wait for 2 seconds
    And Validate 'Successfully added tutor to centre' with xpath '//div[contains(text(),'Successfully added tutor to centre')]' is displayed
    And Refresh the page

    Examples: TestData
      | Tutor_Code | Subject | Tutor                     |
      | Auto5      | BIOLOGY | pujala.haribabu@byjus.com |

  Scenario Outline: Remove tutor Batches from tooljet
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Click on 'tutorportallaunch' button
#    And Wait
#    And New window opens
    And Wait
    And Click on 'remove tutor' button
    And Wait for 3 seconds
    And Click on 'remove tutor centre drpdown' button
    And Wait for 2 seconds
    And Click on 'tutorcentrename' button
    And Wait for 2 seconds
    And Click on 'remove tutor subject drpdown' button
    And Wait for 2 seconds
    And Click on button with xpath '//div[text()="<Subject>"]'
    And Wait for 2 seconds
    And Enter '<Tutor>' as text for 'removetutorname'
    And Wait for 3 seconds
    And Select '<Tutor>' in the 'tutorname' list
    And Wait for 3 seconds
    And Click on 'done' button
    And Wait for 2 seconds
    And Click on 'remove' button
    And Wait for 2 seconds
    And Validate 'Successfully removed tutor' with xpath '//div[contains(text(),'Successfully removed tutor')]' is displayed
    And Wait
    And Refresh the page

    Examples: TestData
      | Subject | Tutor                     |
      | BIOLOGY | pujala.haribabu@byjus.com |

  Scenario Outline: Replace tutor Batches from tooljet
#    Given Open "BMS" Portal using Chrome
#    When login to BMS Portal
#    And mouseHover on 'paid batches app'
#    And Click on 'tutorportallaunch' button
#    And Wait
#    And New window opens
    And Wait
    And Click on 'replace tutor' button
    And Wait for 3 seconds
    And Click on 'replace tutor centre drpdown' button
    And Wait for 2 seconds
    And Click on 'tutorcentrename' button
    And Wait for 2 seconds
    And Enter '<Original_Tutor>' as text for 'originaltutorname'
    And Wait for 3 seconds
    And Select '<Original_Tutor>' in the 'tutorname' list
    And Wait for 3 seconds
    And Enter '<Replacement_Tutor>' as text for 'replacementtutorname'
    And Wait for 3 seconds
    And Select '<Replacement_Tutor>' in the 'tutorname' list
    And Click on 'replace' button
    And Wait for 3 seconds
    And Validate 'Tutor replaced' with xpath '//div[contains(text(),'Tutor replaced')]' is displayed
    And Wait
    And Refresh the page

    Examples: TestData
      | Original_Tutor            | Replacement_Tutor         |
      | jyotiprava.giri@byjus.com | pujala.haribabu@byjus.com |
#      | pujala.haribabu@byjus.com | jyotiprava.giri@byjus.com |


