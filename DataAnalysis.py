#import packages
import pandas as pd
import plotly as py
import numpy as np
import matplotlib.pyplot as plt
import datetime
from dateutil import parser

#Read file for the Data Analysis
try:
    df = pd.read_csv('input_data2.csv')
except:
    print "Error"

#Different options to be chosen for Analysis
while True:
    print "1. Age wise distribution "
    print "2. Country wise distribution"
    print "3. State wise distribution"
    print "4. Sales Monthly wise"
    print "5. Gender Ratio analysis"
    print "6. Exit"

    input1 = int(raw_input("Enter the number for its adjacent analysis: "))

    #histogram for age wise distribution
    if input1 == 1:
        age = df['age']
        plt.hist(age)
        plt.xlabel("Age")
        plt.ylabel("No. of persons")
        plt.title("Age wise distribution")
        plt.show()

    #Bar graph for each person's country analysis
    elif input1 == 2:
        country = df['country'].values
        dict = {}
        for i in country:
            count = np.count_nonzero(country == i)
            dict[i] = count
        print dict
        plt.bar(range(len(dict)), dict.values(), align="center")
        plt.xticks(range(len(dict)), list(dict.keys()))
        plt.xlabel("Country")
        plt.ylabel("No. of persons")
        plt.title("Country wise distribution")
        plt.show()

    #Bar graph for each person's state analysis
    elif input1 == 3:
        country = df['state'].values
        dict = {}
        for i in country:
            count = np.count_nonzero(country == i)
            dict[i] = count
        plt.bar(range(len(dict)), dict.values(), align="center")
        plt.xticks(range(len(dict)), list(dict.keys()))
        plt.xlabel("States")
        plt.ylabel("No. of persons")
        plt.title("State wise distribution")
        plt.show()

    #Bar graph for tickets bought per month
    elif input1 == 4:
        date = df['ticket_date'].values
        list1 = []
        for i in date:
            date1 = parser.parse(i)
            date2 = datetime.date.strftime(date1, "%m/%y")
            list1.append(date2)
        dict = {}
        for i in list1:
            count = list1.count(i)
            dict[i] = count
        plt.bar(range(len(dict)), dict.values(), align="center")
        plt.xticks(range(len(dict)), list(dict.keys()))
        plt.xlabel("Month")
        plt.ylabel("No. of persons")
        plt.title("Sales Monthly wise")
        plt.show()

    #Pie Chart for sex ratio
    elif input1 == 5:
        sex = df['sex'].values
        i,j =0,0
        for k in sex:
            if k == 'M':
                i = i + 1
            else:
                j = j + 1
        labels = ['Male','Female']
        layout1 = go.Layout(
            title='Plot Title')
        trace = go.Pie(labels=labels, values = [i,j] )
        py.offline.plot([trace], filename ='basic_pie_chart.html')

    #Breaking the loop
    elif input1 == 6:
        break

    else:
        print "Invalid query"




