from sys import platform as _platform

import requests

from Common.Enums import OS


class Util:
    def OSType(self):
        if _platform == "linux" or _platform == "linux2":
            return OS.Linux
        elif _platform == "darwin":
            return OS.IOS
        elif _platform == "win32" or _platform == "win64":
            return OS.Windows

    def GetOTP(ph_number, otp_type, country):
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3" \
                    "ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.PthTcyRiA3Koon0RfT-JFkm-31RnVCVY0bTglDin-BA"
            headers = {'Authorization': 'Bearer ' + token,
                       'content-type': 'application/json',
                       'X-TNL-APPID': '601',
                       'X-TNL-APPVERSION': '0.1',
                       'X-TNL-DEVICEID': '66214185',
                       'X-TNL-DEVICEOS': 'Android',
                       'X-TNL-TIMESTAMP': '{{$timestamp}}',
                       'X-TNL-SOURCE-VERSION-CODE': '2'}

            url = 'https://api.tllms.com/staging/k3/api/v1/auth/otp/list'
            if 'india' in country.lower():
                try:
                    data = {"phone": '+91-' + ph_number, "type": str(otp_type)}
                    otp_list_resp = requests.get(url, headers=headers, params=data)
                    print("response : " + str(otp_list_resp))
                    assert '200' in str(otp_list_resp)
                except:
                    data = {"phone": '+91-' + ph_number, "type": 'login'}
                    otp_list_resp = requests.get(url, headers=headers, params=data)
                    print("response : " +str(otp_list_resp))
                    assert '200' in str(otp_list_resp)
            print(str(otp_list_resp))
            return str(otp_list_resp.json()['otp'])

