@sanity
Feature: sanity1

Scenario: Student Join Online Class

  Given Launch BLC Portal using Chrome
    When Enter Phone Number and Password and Login
    Then Dashboard should be displayed
    And User click on join button
    And User join the class
    And user chat with tutor
    And user click on like button

  Scenario: Student Join Offline Class

  Given Launch BLC Portal using Chrome
    When Enter Phone Number and Password and Login
    Then Dashboard should be displayed
    And User click on join button
    And User join the class
    And user chat with tutor
    And click on like button

    # bootsrap
  # Nodejs
  # Angular