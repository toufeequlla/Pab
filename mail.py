import mimetypes
import os
import smtplib, ssl
from datetime import date
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


class Mail:
    @staticmethod
    def send(content=None, screenshotpath=None):

        with open(content) as fp:
            mailcontent = fp.read()

        subject = "BLC - Automation Test Report for " + str(date.today())
        email_from = 'sanjesh.salecha@byjus.com'
        password = 'warckbzgcgwsxamd'
        email_to = 'sanjesh.salecha@byjus.com'  # ,'vidyashree.n@byjus.com', 'ganesh.shastri@byjus.com'
        # email_to = {','.join(email_to)}

        email_message = EmailMessage()
        email_message['From'] = email_from
        email_message['To'] = email_to
        email_message['Subject'] = subject
        email_message.set_content("Please view the email in html aware email client...!!!")
        #email_message.attach(MIMEText(mailcontent, "html", "utf-8"))
        email_message.add_alternative(mailcontent, subtype="html")

        for file in os.listdir(screenshotpath):
            if file.endswith(".png"):
                path = os.path.join(screenshotpath, file)
                if not os.path.isfile(path):
                    continue
                ctype, encoding = mimetypes.guess_type(path)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                with open(path, 'rb') as fp:
                    email_message.get_payload()[0].add_related(fp.read(), 'image', 'png', cid=file.split('.')[0])
                    #email_message.add_attachment(fp.read(),maintype=maintype,subtype=subtype,filename="cid:"+file.split('.')[0])
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(email_from, password)
                server.send_message(email_message)
                server.quit()
        except Exception as e:
            print("Sendmail error : " + str(e))

