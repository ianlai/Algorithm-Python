#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import drange, SUNDAY

from algolist import getPracticeNumber
from algolist import showQuizListFromDir
from reviewlist import getReviewNumber
from lcode import getQuizCount
from lcode import showQuizListFromLeetcode

import datetime
import numpy as np

###################### 
### Initialize
######################
FILE_PREFIX     = "statistics"
FILE_PREFIX_SCORE     = "score"
FILE_STATISTICS = FILE_PREFIX + ".log"

FILE_IMAGE201910 = FILE_PREFIX + "_201910" + ".png"
FILE_IMAGE201911 = FILE_PREFIX + "_201911" + ".png"
FILE_IMAGE201912 = FILE_PREFIX + "_201912" + ".png"
FILE_IMAGE202001 = FILE_PREFIX + "_202001" + ".png"
FILE_IMAGE202002 = FILE_PREFIX + "_202002" + ".png"
FILE_IMAGE202003 = FILE_PREFIX + "_202003" + ".png"

FILE_IMAGE_SCORE202004 = FILE_PREFIX_SCORE + "_202004" + ".png"
FILE_IMAGE_SCORE202005 = FILE_PREFIX_SCORE + "_202005" + ".png"
FILE_IMAGE_SCORE202006 = FILE_PREFIX_SCORE + "_202006" + ".png"
FILE_IMAGE_SCORE202007 = FILE_PREFIX_SCORE + "_202007" + ".png"
FILE_IMAGE_SCORE202008 = FILE_PREFIX_SCORE + "_202008" + ".png"

FILE_IMAGE_SCORE202104 = FILE_PREFIX_SCORE + "_202104" + ".png"
FILE_IMAGE_SCORE202105 = FILE_PREFIX_SCORE + "_202105" + ".png"
FILE_IMAGE_SCORE202106 = FILE_PREFIX_SCORE + "_202106" + ".png"
FILE_IMAGE_SCORE202107 = FILE_PREFIX_SCORE + "_202107" + ".png"
FILE_IMAGE_SCORE202108 = FILE_PREFIX_SCORE + "_202108" + ".png"
FILE_IMAGE_SCORE202109 = FILE_PREFIX_SCORE + "_202109" + ".png"
FILE_IMAGE_SCORE202110 = FILE_PREFIX_SCORE + "_202110" + ".png"
FILE_IMAGE_SCORE202111 = FILE_PREFIX_SCORE + "_202111" + ".png"
FILE_IMAGE_SCORE2021_TOTAL = FILE_PREFIX_SCORE + "_2021" + ".png"
FILE_IMAGE_SCORE_TOTAL = FILE_PREFIX_SCORE + "_total" + ".png"



DATE_FORMATTER = "%Y-%m-%d"
dates = []
values = []        #done quiz number (local)
reviewNumber = []  #reviewed quiz number (local)

leetnumber = []  #leetcode quiz number
easyNumber = []
mediumNumber =[]
hardNumber = []
leetscore = []  #leetcode score 

latest_date = ""

###################### 
### Write to file  
######################
def write(line):
    f = open(FILE_STATISTICS, "a+")
    f.write(line)
    f.close()

def writePrepare(today_date, today_value, today_lcode, score, today_review):
    line = [] 
    line.append(sf(str(today_date)))
    line.append(sf(str(today_value)))
    line.append(sf(str(today_lcode['num_solved'])))
    line.append(sf(' | '))
    line.append(sf(str(today_lcode['ac_easy']),5))
    line.append(sf(str(today_lcode['ac_medium']),5))
    line.append(sf(str(today_lcode['ac_hard']),4))
    line.append(sf(' | '))
    line.append(sf(str(score)))
    line.append(sf(' | '))
    line.append(sf(str(today_review),4))
    line.append('\n')
    linePrint = ''.join(line)
    return linePrint

###################### 
### Draw the graph   
######################
def draw(dates, values):

    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(14, 10))

    dates = dates[-len(leetscore):]
    values = values[-len(leetscore):]
    annotate_y_offset = 5
    
    # vertical dividers (week, day)
    xfmt = mdates.DateFormatter("%m/%d")

    ### Set grid
    axs[0].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[0].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[0].grid(which='major', color='#bbbbbb', axis ='y')
    axs[1].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[1].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[1].grid(which='major', color='#bbbbbb', axis ='y')

    ### Draw number figure 
    y_stack = np.row_stack([easyNumber, mediumNumber, hardNumber])
    axs[0].stackplot(dates, y_stack, colors=['#5cb85c', '#f0ad4e', '#d9534f'])                 #e,m,h number
    #axs[0].plot_date(dates, values,'-', marker='o')
    axs[0].plot_date(dates, leetnumber,'-', marker='', linewidth = 5, color='black')           #leet number
    #axs[0].plot_date(dates[-len(reviewNumber):], reviewNumber,'-', marker='o', color='#555555')  #review number

    ### Draw score figure 
    axs[1].set_ylim(0,900) #score of quiz
    axs[1].plot_date(dates, leetscore,'-', marker='.', markersize=10, color='#cc3300')


    # Year: Total 
    axs[1].set(xlabel="Date", ylabel="Score",
    title="Score of Quiz (2021.04 - 2022.02)")
    axs[0].set_title("Number of Quiz", fontweight = 'bold')
    axs[1].set_title("Score of Quiz", fontweight = 'bold')
    axs[0].set_xlim(datetime.datetime(2021,4,1), datetime.datetime(2022,2,28)) 

    xloc1 = mdates.MonthLocator()
    xloc2 = mdates.WeekdayLocator(SUNDAY)
    axs[0].xaxis.set_major_formatter(xfmt)
    axs[0].xaxis.set_major_locator(xloc1) #major: month
    #axs[0].xaxis.set_minor_formatter(xfmt)
    axs[0].xaxis.set_minor_locator(xloc2) #minor: week
    plt.gcf().autofmt_xdate()
    plt.savefig(FILE_IMAGE_SCORE_TOTAL)


    # Month: 2021.04 ~ 
    axs[0].clear()
    axs[0].stackplot(dates, y_stack, colors=['#5cb85c', '#f0ad4e', '#d9534f'])                 #e,m,h number
    axs[0].plot_date(dates, leetnumber,'-', linewidth = 1, marker='o', color='black')   
    axs[0].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[0].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[0].grid(which='major', color='#bbbbbb', axis ='y')


    xloc1 = mdates.WeekdayLocator(SUNDAY)
    xloc2 = mdates.DayLocator()
    axs[0].xaxis.set_major_formatter(xfmt)
    axs[0].xaxis.set_major_locator(xloc1) #major: week
    axs[0].xaxis.set_minor_formatter(xfmt)
    axs[0].xaxis.set_minor_locator(xloc2) #minor: day

    plt.gcf().autofmt_xdate(which='both')

    # leetcode number
    # for i,j in zip(dates, leetnumber):
    #     axs[0].annotate(str(j), xy=(i, j + annotate_y_offset - 5))
    for i in range(len(leetnumber)):
        axs[0].annotate(leetnumber[i]  , xy=(dates[i], leetnumber[i] + annotate_y_offset ), fontweight = 'bold')
        axs[0].annotate(hardNumber[i]  , xy=(dates[i], leetnumber[i] - annotate_y_offset ), fontsize = 9, color='#b00e2c')
        axs[0].annotate(mediumNumber[i], xy=(dates[i], easyNumber[i] + mediumNumber[i] - annotate_y_offset - 7), fontsize = 9 , color='#c9891a')
        axs[0].annotate(easyNumber[i]  , xy=(dates[i], easyNumber[i] - annotate_y_offset) ,fontsize = 9, color='#3e7d23')

    # review number (gray line)
    # for i in range(len(reviewNumber)):
    #     axs[0].annotate(reviewNumber[i],
    #     xy=(dates[-len(reviewNumber):][i], reviewNumber[i] + annotate_y_offset - 5),
    #     fontweight = 'bold', color='#555555')
    
    # leetcode score
    for i,j in zip(dates, leetscore):
        axs[1].annotate(str(j), xy=(i, j - annotate_y_offset * 1.5))

    lastDateMap = {
        1: 31, 
        2: 28, 
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31, 
        11: 30, 
        12: 31, 
    }

    #2021
    # for month in range(4, 13, 1):
    #     monthStr = str(month).zfill(2)
    #     dateStr = "2021." + monthStr 
    #     numberTitle = "Number of Quiz (" + dateStr + ")"
    #     scoreTitle = "Score of Quiz (" + dateStr + ")"
    #     axs[1].set(xlabel="Date", ylabel="Score")
    #     axs[0].set_title(numberTitle, fontweight = 'bold')
    #     axs[1].set_title(scoreTitle, fontweight = 'bold')
    #     axs[0].set_xlim(datetime.datetime(2021, month, 1), datetime.datetime(2021, month, lastDateMap[month])) 
    #     fileName = "score_2021" + monthStr + ".png"
    #     plt.savefig(fileName)

    #2022
    for month in range(1, 3, 1):
        monthStr = str(month).zfill(2)
        dateStr = "2022." + monthStr 
        numberTitle = "Number of Quiz (" + dateStr + ")"
        scoreTitle = "Score of Quiz (" + dateStr + ")"
        axs[1].set(xlabel="Date", ylabel="Score")
        axs[0].set_title(numberTitle, fontweight = 'bold')
        axs[1].set_title(scoreTitle, fontweight = 'bold')
        axs[0].set_xlim(datetime.datetime(2022, month, 1), datetime.datetime(2022, month, lastDateMap[month])) 
        fileName = "score_2022" + monthStr + ".png"
        plt.savefig(fileName)

    # plt.show()

###################### 
### Read from file  
######################
def read():
    f = open(FILE_STATISTICS, "r")
    line = f.readline()
    while line != '':  # The EOF char is an empty string
        split_line = line.split()
        if len(split_line) > 3 :  # Format-2 (add leetcode numbers)
            date_str = split_line[0] 
            file_count = split_line[1] 
            l_count_total = split_line[2] 
            l_count_easy = split_line[4] 
            l_count_medium = split_line[5] 
            l_count_hard = split_line[6] 
            l_score = split_line[8] 
            dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
            values.append(int(file_count))
            leetscore.append(int(l_score))
            leetnumber.append(int(l_count_total))
            easyNumber.append(int(l_count_easy))
            mediumNumber.append(int(l_count_medium))
            hardNumber.append(int(l_count_hard))

        elif len(split_line) == 2:
            date_str, val_str = split_line[0], split_line[1] 
            dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
            values.append(int(val_str))
        else:
            break

        if len(split_line) == 11:  # Format-3 (add review numbers)
                l_count_review = split_line[10]
                reviewNumber.append(int(l_count_review))

        line = f.readline()
    f.close()

def sf(s, num=6):
    s = str(s)
    return f'{s:>{num}}'

###################### 
### Print info 
######################

showQuizListFromDir()       #from local repo
showQuizListFromLeetcode()  #from leetcode

###################### 
### Read today info 
######################
print(">> Read from files:", FILE_STATISTICS)
read()
latest_date = dates[-1].strftime(DATE_FORMATTER)
today_date = datetime.date.today()

# New data
if str(today_date) != str(latest_date): 
    print(">> Status : NEW! (latest = ", latest_date, ", today = " ,today_date, ")") 
    
    #Get data 
    today_lcode = getQuizCount()      # Get leetcode data
    today_value = getPracticeNumber() # Get local data
    today_review = getReviewNumber()  # Get local review number
    
    #Update data in memory
    dates.append(today_date)
    values.append(today_value)
    leetnumber.append(today_lcode['num_solved'])
    easyNumber.append(today_lcode['ac_easy'])
    mediumNumber.append(today_lcode['ac_medium'])
    hardNumber.append(today_lcode['ac_hard'])
    reviewNumber.append(today_review)
    score = 1 * today_lcode['ac_easy'] \
        + 3 * today_lcode['ac_medium'] \
        + 5 * today_lcode['ac_hard']
    leetscore.append(score)

    #Update data in file
    writeLine = writePrepare(today_date, today_value, today_lcode, score, today_review)
    write(writeLine)
else:
    print(">> Status: Existed date.")

#print(">> Save the image:", FILE_IMAGE_SCORE202104)

#Debug
# print("dates       :", len(dates))
# print("values      :", len(values))
# print("leetnumber  :", len(leetnumber))
# print("easyNumber  :", len(easyNumber))
# print("mediumNumber:", len(mediumNumber))
# print("hardNumber  :", len(hardNumber))
# print("leetscore   :", len(leetscore))
# print("reviewNumber:", len(reviewNumber))

draw(dates, values)