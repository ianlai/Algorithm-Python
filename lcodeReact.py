#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
import browsercookie
import json
import ssl
import pprint
#import json2html
from json2html import *

PPRINT = pprint.PrettyPrinter(indent=4)

DIFFICULTY_TYPES = ['Easy']
RESET = False

COOKIE_PATH = '/Users/01204086/Library/Application Support/Google/Chrome/Profile 1/Cookies'
WEBSITE_URL = 'https://leetcode.com'
URL_PROBLEM = 'https://leetcode.com/problems/'
API_URL = 'https://leetcode.com/api/problems/all/'
LCODE_JSON_PATH = 'show-lcode-app/src/lcode-react.json'

from lcodeFile import fetchFileDate
idToDate = fetchFileDate()


def getCookie(website_url, cookie_path):
    myNeedDomainDict = {}
    targetDomain = website_url.split('/')[-1]
    for _ in browsercookie.chrome([cookie_path]):
        if targetDomain in _.domain:
            myNeedDomainDict[_.name] = _.value
    return myNeedDomainDict

def getQuizCount():
    with requests.Session() as s:
        s.cookies.update(requests.utils.cookiejar_from_dict(getCookie(WEBSITE_URL, COOKIE_PATH)))
        r = s.get(API_URL)
        my_result = json.loads(r.text)
    my_statistic_data = {key: my_result[key] for key in ['ac_easy', 'ac_medium', 'ac_hard', 'num_solved']}

    return my_statistic_data

def showQuizListFromLeetcode():
    with requests.Session() as s:
        s.cookies.update(requests.utils.cookiejar_from_dict(getCookie(WEBSITE_URL, COOKIE_PATH)))
        r = s.get(API_URL)
        #print("### header:", "\n", r.headers)
        my_result = json.loads(r.text)
    #print('User Name:' , my_result['user_name'])
    my_statistic_data = {key: my_result[key] for key in ['ac_easy', 'ac_medium', 'ac_hard', 'num_solved']}

    count_easy   = 0
    count_medium = 0
    count_hard   = 0
    q = []
    qMap = {}
    qArr = []
    for i in range(len(my_result['stat_status_pairs'])):
        q.append(my_result['stat_status_pairs'][i])
        if q[i]['difficulty']['level'] == 1:
            count_easy += 1
        if q[i]['difficulty']['level'] == 2:
            count_medium += 1
        if q[i]['difficulty']['level'] == 3:
            count_hard += 1
    q = sorted(q, key=lambda e: e['stat']['frontend_question_id'])

    print()
    print("=====================================")
    print("============= Leetcode ==============")
    print("=====================================")
    

    data = []
    existedData = {}
    if RESET:
        print("RESET mode (wipe-out)")
    else:
        print("APPEND mode")

    if not RESET:
        with open(LCODE_JSON_PATH, "r") as fr:
            data = fr.read().splitlines(True)
            # data = data[1:len(data)-1]
        dataArr = json.loads("".join(data))
        for data in dataArr:
            existedData[data["Number"]] = {
                        "Number": data["Number"], 
                        "Level" : data["Level"], 
                        "Title" : data["Title"],
                        "Url" : data["Url"], 
                        "Tags" : data["Tags"], 
                        "Memo" : data["Memo"],
                        "Date" : idToDate[data["Number"]]
                    }
    for e in q:
        if e['status'] == "ac":
            qNumber = str(e['stat']['frontend_question_id']).zfill(4)
            qTitle = e['stat']['question__title']
            qSlug = e['stat']['question__title_slug']
            qLevel = e['difficulty']['level']

            #print(qNumber, qTitle, qLevel)
            qUrl = URL_PROBLEM + qSlug
            qLink = "<a href=\"" + qUrl + "\">" + qTitle + "</a>"
            qMap[qNumber] = [qTitle, qUrl, qLevel]
            
            appendData = None
            if not RESET:  #Append
                if qNumber in existedData: #skip
                    appendData = existedData[qNumber]
                else:
                    appendData = {
                            "Number": qNumber, 
                            "Level" : qLevel, 
                            "Title" : qTitle, 
                            "Url" : qUrl, 
                            "Tags" : [],
                            "Memo" : ""
                        }
            else:          #
                appendData = {
                            "Number": qNumber, 
                            "Level" : qLevel, 
                            "Title" : qTitle, 
                            "Url" : qUrl, 
                            "Tags" : [],
                            "Memo" : ""
                        }
            qArr.append(appendData)
            # print(appendData)

    #Write file 
    with open(LCODE_JSON_PATH, "w") as f:
        f.write("[" + "\n")
        for idx, object in enumerate(qArr):
            # Use json to write
            json.dump(object, f, separators=(', ', ': '), indent = 4, ensure_ascii=False)
            
            if idx != len(qArr) - 1:
                f.write(",\n")
            else:
                f.write("\n")

    #qJson = json.dumps(qMap)
    #f.write(qJson)
        f.write("]")
        f.close()



def stringFormatter(s, num):
    s = str(s)
    return f'{s:>{num}}'

# run as a script (not module)
if __name__ == '__main__':
    showQuizListFromLeetcode()
