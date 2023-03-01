import time

import selenium

from Common.Enums import ElementIDType
from behave import step


class BMS:
    @step("Select Slot for '{day}', '{startTime}', '{endTime}'")
    def selectSlotInGrid(self, day, startTime, endTime):

        while True:
            rows = self.driver.getElementsByXPath('//*[@id="canvas-fa41d068-121b-49fe-b78f-aded0669082e"]/div[3]/div/div/div[1]/div/div/div[2]/table/tbody/tr')
            i = 0
            for row in rows:
                try:
                    slot_from_row = self.driver.getElementByXPath("//*[@id=\"canvas-fa41d068-121b-49fe-b78f-aded0669082e\"]/div[3]/div/div/div[1]/div/div/div[2]/table/tbody/tr[" + str(i+1) + "]").text
                    slot = slot_from_row.split("\n")
                    if day == slot[0] and startTime == slot[1] and endTime == slot[2]:
                        self.driver.click("//*[@id=\"canvas-fa41d068-121b-49fe-b78f-aded0669082e\"]/div[3]/div/div/div[1]/div/div/div[2]/table/tbody/tr[" + str(i + 1) + "]/td[1]/div/div/input", ElementIDType.XPATH)
                        print("slot selected")
                        return
                    i = i + 1
                except:
                    print("error")

            pagecount = self.driver.getElementByXPath("//*[@id=\"canvas-fa41d068-121b-49fe-b78f-aded0669082e\"]/div[3]/div/div/div[1]/div/div/div[3]/div/div[1]/div[@class='pagination']/small/strong").text.split("of")

            totalpage = pagecount[1]
            currentpage = pagecount[0]
            if(totalpage == currentpage):
                print("last page reached")
                return
            self.driver.click("//*[@id=\"canvas-fa41d068-121b-49fe-b78f-aded0669082e\"]/div[3]/div/div/div[1]/div/div/div[3]/div/div[1]/div/button[3]", ElementIDType.XPATH)



    @step('login to BMS Portal')
    def Login(self):
        self.execute_steps('''When Click on 'Login' button 
        And Enter 'config:login>email' as text for 'email'
        And Click on 'next' button
        And Wait for 2 seconds
        And Enter 'config:login>password' as text for 'password'
        And Click on 'passwordNext' button
        And Wait''')

    #@when('Select end date from calender')
    #def step_Slotclan(self):
        #raise NotImplementedError('STEP: When Select end date from calender')

        #for edt in btn_edd :
           #print(1);
            #if edt == '25':


        #break


