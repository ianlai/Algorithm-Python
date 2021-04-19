#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
import browsercookie
import json
import ssl
import pprint
PPRINT = pprint.PrettyPrinter(indent=4)

DIFFICULTY_TYPES = ['Easy']

COOKIE_PATH = '/Users/01204086/Library/Application Support/Google/Chrome/Profile 1/Cookies'
WEBSITE_URL = 'https://leetcode.com'
API_URL = 'https://leetcode.com/api/problems/all/'

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

    for e in q:
        if e['status'] == "ac":
            print("", str(e['stat']['frontend_question_id']).zfill(4), e['stat']['question__title'])
    
    score = 5 * my_result['ac_hard'] + 3 * my_result['ac_medium'] + 1 * my_result['ac_easy']
    print("=====================================")
    print('Solved / Total (Easy)  :' , stringFormatter(my_result['ac_easy']   , 4), '/', stringFormatter(count_easy, 4))
    print('Solved / Total (Medium):' , stringFormatter(my_result['ac_medium'] , 4), '/', stringFormatter(count_medium, 4))
    print('Solved / Total (Hard)  :' , stringFormatter(my_result['ac_hard']   , 4), '/', stringFormatter(count_hard,4))
    print('Solved / Total (All)   :' , stringFormatter(my_result['num_solved'], 4), '/', stringFormatter(my_result['num_total'],4))
    print('Total Score            :' , stringFormatter(score, 4))
    print("=====================================")
    print()

def stringFormatter(s, num):
    s = str(s)
    return f'{s:>{num}}'

# run as a script (not module)
if __name__ == '__main__':
    showQuizListFromLeetcode()  
