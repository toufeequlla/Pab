# AutoBase
Basic Automation framework for web and app test automation using Python, Selenium, Appium and Behave

#Experimentation Branch:
Please use <i>blc_team</i> branch for your experimentation.

# Setting up git:
Follow below instructions to setup the git ssh key
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

IDE:
Download and Install the pyCharm IDE from https://www.jetbrains.com/pycharm/download/#section=mac

For Git support, please download and install xCode from Apple Store if GIT does not work, then only.

To clone the repo:
git clone git@github.com:byjutech/AutoBase.git

# Modules to be isntalled:
  &nbsp;&nbsp; pip3 install behave <br>
  &nbsp;&nbsp; pip3 install selenium <br>
  &nbsp;&nbsp; pip3 install webdriver_manager
 
 <i>If pip3 is not working, try: <br></i>
 &nbsp;&nbsp; &nbsp;&nbsp; python3 -m pip install behave <br>
 &nbsp;&nbsp; &nbsp;&nbsp; python3 -m pip install selenium <br>
 &nbsp;&nbsp; &nbsp;&nbsp; python3 -m pip install webdriver_manager <br>
 
 # Tutorials:
  &nbsp;&nbsp; &nbsp;&nbsp; Behave : https://behave.readthedocs.io/en/stable/tutorial.html
  <br>&nbsp;&nbsp; &nbsp;&nbsp; Selenium : https://www.selenium.dev/documentation/
  <br>&nbsp;&nbsp; &nbsp;&nbsp; Python : https://docs.python.org/3/tutorial/index.html
  <br>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  https://www.geeksforgeeks.org/python-programming-language/?ref=shm
 
 # Example files <br>
 To automate a test case, write testcase in gherkin as in <i><b>login.feature</b></i> in features directory. <br>
 Makse sure corresponding step definition is there in <i><b>features/steps/commonactions.py or sanity.py file<i><b> file
  
  
  # Command to run the scripts:
   python3 -m behave WebTestCases/BLC/features/<i>login<i>.feature 
  
  Please replace the name of feature file (italicised) with your feature file.
  
