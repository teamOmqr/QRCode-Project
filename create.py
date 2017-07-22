#import modules
import pandas as pd
import numpy as np
import re # for  email verification
import pyqrcode   # use to create qr code
import png    # to save img as png
import uuid #to genrate the unique id
#both needed to decode the qrcode
import pyqrcode
import csv

import datetime #for date

#to send ticket as mail
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email.Utils import COMMASPACE, formatdate
from email import Encoders

#classes
class data():

    #__init__ method is called by default
    def input_data(self,id):
        self.dict={}   #storing input


        self.dict['name'] =[raw_input("Enter your Name :")]


        # validation for age as int value
        while True:
            try:
                self.dict["age"] = [int(raw_input("Please enter your age: "))]
            except ValueError:
                print("Sorry, Please enter as integer")

                continue
            else:
                # age was successfully parsed!
                # we're ready to exit the loop.
                break

        #email verification
        def email_verfication():
            global addressToVerify
            addressToVerify = raw_input("email:")
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

            if match == None:
                print('invalid email')
                email_verfication()



            else:
                self.dict["email"] = [addressToVerify]
        email_verfication()


        #contact no verification
        def validate_number():
            number = raw_input("enter your contact number:")

            if number.isdigit() and len(number)==10:
                self.dict["number"]=[number]
            else:
                print "please check your contact number (10digits)"
                validate_number()

        validate_number()

        self.dict['sex'] = [raw_input("Enter M/f :").upper()]

        # to get the date and time of ticket issued
        date=datetime.datetime.today()

        self.dict['ticket_date'] = [date]


        # no of ticket
        self.dict['no_of_ticket'] = [raw_input("Enter no of ticket :").upper()]

        # address of the buyer
        self.dict['state'] = [raw_input("Enter your state :").upper()]
        self.dict['country'] = [raw_input("Enter your country :").upper()]

        #generate a unique_id for the entries
        self.dict['unique_id'] = [id]

        obj1.generate(id)

    #genrate the qr code and save it as file (.png)
    def generate(self,id):
        url = pyqrcode.create(id)
        url.png('uca-url.png', scale=8)
        print(url.terminal(quiet_zone=1))
        big_code = pyqrcode.create("123", error='L', version=27, mode='binary')

    def email_t(self):
        filePath = "uca-url.png"  # your file name

        From = 'testpythom@gmail.com'
        To = str(addressToVerify)

        msg = MIMEMultipart()
        msg['From'] = From
        msg['To'] = To
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = 'Ticket for museum'

        msg.attach(MIMEText('Hey this team Om sending you msg'))

        try:
            smtp = smtplib.SMTP('smtp.gmail.com:587')
            smtp.starttls()
            smtp.login('testpythom@gmail.com', 'pythonisamazing')
        except:
            i = 1
        else:
            i = 0

        if i == 0:
            ctype, encoding = mimetypes.guess_type(filePath)
            if ctype is None or encoding is not None:
                # No guess could be made, or the file is encoded (compressed), so
                # use a generic bag-of-bits type.
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            if maintype == 'text':
                fp = open(filePath)
                # Note: we should handle calculating the charset
                part = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(filePath, 'rb')
                part = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'audio':
                fp = open(filePath, 'rb')
                part = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(filePath, 'rb')
                part = MIMEBase(maintype, subtype)
                part.set_payload(fp.read())
                fp.close()
                # Encode the payload using Base64
                Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % filePath)
            msg.attach(part)
            try:
                smtp.sendmail(From, To, msg.as_string())
            except:
                print "Mail not sent"
            else:
                print "Mail sent"
                # ticket generation message
                print("Your ticket has been sent to you via email/n Thanks TEAM OM ")
            smtp.close()
        else:
            print "Connection failed"



#creating object
id = str(uuid.uuid4())
obj1=data()
obj1.input_data(id)
obj1.email_t()

#create dataframe and csv
df=pd.DataFrame(obj1.dict)

#to check header and append data
try:
    with open('input_data.csv', 'rb') as csvfile:
        pass
    with open("input_data.csv","a") as csv_edit:
        df.to_csv(csv_edit,index=False,header=False)
except:
    with open('input_data.csv','a') as csv_edit:
        df.to_csv(csv_edit,index=False)