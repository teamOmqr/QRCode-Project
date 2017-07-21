# Crack The Door-Project
Crack the Door is the application module which is used to improve the entrance ticketing system and make it easy for people to pass the gates with comfort. In addition to ticketing system, this application provides the graphical analysis which includes several comparison graphs which helps in collecting and scrutinizing every data allowing managers to target the large audience by improving the strategies categorially.

## Getting Started
- Crack-the-door is an QR Code ticketing system designed for Windows, Linux, or OSX. It's written in Python with no third party modules needed. The tool is designed to eases up the comfort level of the visitors with the help of generation of QR code in spite of the hard paper ticket, which helps the visitors to get scan the QR code whenever needed which saves much more time and trouble. The mechanism is simple, issue QR Codes, track them in a database, and be able to look them up in a simplfied fashion. The way it works is by sending the ticket in a form of a QR Code with a randomizesd hash value to an internal database as well as e-mail will be generated and sent to the visitors.
- Once scanned in, the device will open a URL of the QR Code server. The server handles the request and identifies if the person has a ticket, has already checked in, or is not found. If found and has not checked in, the user is checked in and the user can successfully enter the Museum.
- In addition to this prototype module, our team has made a mechanism by which entrance gates will be automated, visitors only have to make sure that their QR codes get scanned and it helps to reduce the man power at the entrance. This mechanism works in such a way that whenever the QR code will get scanned, the entrance gate will open and infrared sensors at the entrance will scan and allow the number of visitors mentioned at the time of booking for a particular ticket.
- Data analysis tool will provide graphical analysis using several comparisons graph for more future improvement like collecting and scrutinizing every data for better business investments. 

## Prerequisites
> **Requirements for running the code:**
- Operating System ( Windows/Linux)
- Python 2.7 ( https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi )
- Microsoft Excel ( To view the Database manually )
- IDE ( ECLIPSE/PYCHARM recommended ) -( https://www.jetbrains.com/pycharm/ )/ COMMAND PROMPT 

> **HOW TO RUN CODE:**
- Install the python 2.7 from the above link specified
- Install the IDE or run on command prompt.
- Import the source code to the IDE.
- Now import all the Modules necessary from the list given below .
     - Go to Command Prompt
     - exectute command on console:      
                 PIP install module_name(listed below).
- and then Simply execute the code.

## Modules
- pandas
- numpy
- dateutil
- pyqrcode
- uuid
- re
- png
- csv
- datetime
- plotly
- matplotlib.pyplot
- smtplib
- mimetypes
- email
- qrtools

## No Prompt
**STEP 1:**
- If finding any difficulties above, simply download the crack-the-door .EXE files from this website.

**STEP 2:**
- Run the .exe files for the corresponding operations such as generating QR code, Scanning QR code and Data Analysis Tools.

## Basic structure
src/database/input_data.csv - contains all of the email addresses and qrcode hash codes - contains those that have already registered.

## Built With
- Python
- Excel ( Database Management System can change in future )

## Version
Crack-the-door **Version 1.0 **( Basic module Application )

## Authors- TEAM OM
- Ankit Shukla
- Abhishek Jindal
- Keshav Khetan
- Aekanshu Panchal 

## TO-DO:
- Interface is ugly, first basic module, will make nicer in next release of module.
- While booking we will consider the verified government idea for the purpose for security and authentication.
- More refined analysis of data would be possible for better predictions.
- Automation of the Entrances.




