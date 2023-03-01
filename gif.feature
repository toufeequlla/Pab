Feature: Gif

  Scenario Outline: Adding gif file
    Given Open "https://blc-cms.stage.tllms.com/" Portal using Chrome
    When login to CMS Portal
    And wait for 5 seconds
    And Click on 'gif' button
    And Click on 'Upload Gif' button
    And Enter '<name>' as text for 'Name'
    And Enter 'config:data>gifpath' as text for 'Upload GIF'
    #And Enter text 'Gif_Automation4' to textbox with xpath '//*[@id="root"]/div/div[2]/div[3]/div[1]/div/div/input'
    #And Enter text 'C://Users//Amol Deshmukh//Downloads//GIF//gif5.gif' to textbox with id 'gifContainer'
    And Click on 'Upload' button
    Then Validate 'table column' having '<name>' is displayed
    And Wait
    And Click on 'Gif ID' button for '<name>'
    And Click on 'Edit' button
    And click on 'Status' dropdown
    And Select 'Published' in the 'Status' list
    And click on 'Save to publish' button
    And Wait for 5 seconds


    Examples: TestData
  |   name  |
  | Auto_Gif<dynamic>  |
