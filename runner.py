import os
os.system("python3 -m behave \"WebTestCases/BLC/features/StudentLoginStudentLogin.feature\"")
os.system("python3 -m behave \"WebTestCases/BLC/features/sanity.feature\"")
from ExternalSystems.TestCaseMgmtSys import testrail

testrail.create_feature_file(244, 0, run_ID, case_val)