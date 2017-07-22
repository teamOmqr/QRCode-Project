#import modules
from qrtools import QR
import pandas as pd
import datetime
from dateutil import parser
import sys

#Read QR function
def read_qr():
    myCode = QR()
    myCode.decode_webcam()
    global search_element
    search_element = myCode.data
    global df
    try:
        df = pd.read_csv('input_data.csv')
    except:
        print('There was an error opening the file!')
        sys.exit()
    global selected_row
    selected_row = df.loc[df['unique_id'] == search_element]
    global adf
    adf = df.drop(df[df.unique_id == search_element].index)

#Calling read_qr function
read_qr()

# While loop for checking the validity of QR
while True:
    if not selected_row.empty:
        date = df['ticket_date'][df['unique_id'] == search_element]
        datevar1 = df['ticket_date'][df['unique_id'] == search_element].index.values[0]
        datevar2 = date[datevar1]
        # 48 hours has been taken as the validity of ticket
        if parser.parse(str(datevar2)) + datetime.timedelta(hours=48) > datetime.datetime.today():
            print "Successful"
            break
        else:
            print "QR Expired"
            read_qr()
    else:
        print "Invalid QR or try again"
        read_qr()

#No. of persons to be allowed by a QR
persons = df['name'][df['unique_id'] == search_element]
print ('No. of persons', persons)

#To append input_data2.csv
try:
    with open('input_data2.csv', 'rb') as csvfile:
        pass
    with open("input_data2.csv","a") as csv_edit:
        selected_row.to_csv(csv_edit,index=False,header=False)
except:
    with open('input_data2.csv','a') as csv_edit:
        selected_row.to_csv(csv_edit,index=False)

#Remove the entry from input_data.csv
with open("input_data.csv","w") as csv_edit:
    adf.to_csv(csv_edit,index=False)