@sanity
Feature: BMS

  Scenario Outline: Open BMS portal

    Given Open "BMS" Portal using Chrome
    When Click on button with xpath '//*[@id="app"]/div[1]/div/div/form/div/div/div/div/button'
    And Enter '<email>' and '<password>' in Google SSO
    And click on 'add slot group' button
    And Click on button with xpath '//*[@class="real-canvas "]/div[13]/div/div/div[1]/div/div[1]/div[2]/div/div'
    And Click on button with xpath '//*[@id="react-select-11-option-1"]'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[7]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="react-select-8-option-10"]'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[8]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[9]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="react-select-10-option-0"]'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[4]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="react-select-5-option-7"]'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[5]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="react-select-6-option-0"]'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[6]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div'
    And Click on button with xpath '//*[@id="react-select-7-option-1"]'
    And Click on Button With xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[1]/div/div/div[1]/div/div/div/label[1]/input'
    And Click on button With xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[14]/div/div/div[1]/div/button'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[3]/div/div/div[1]/div/div/div[1]/table/tbody/tr[3]/td[2]/div/span'
    And Select Slot for 'Sun', '2:15:AM', '11:50:PM'
    And Click on button with xpath '//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[3]/div/div/div[1]/div/div/div[2]/div/div[1]/div/button[3]'
    And Validate 'button' with xpath '//*[@id="app"]/div[1]/div/div/form/div/div/div/div/button' is displayed
    And Wait

    Examples: TestData
      | email                     | password |
      | sanjesh.salecha@byjus.com | R@niwara318 |









