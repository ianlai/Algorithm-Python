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

COOKIE_PATH = '/Users/01204086/Library/Application Support/Google/Chrome/Profile 1/Cookies'
WEBSITE_URL = 'https://leetcode.com'
URL_PROBLEM = 'https://leetcode.com/problems/'
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
    qMap = {}
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
            qNumber = str(e['stat']['frontend_question_id']).zfill(4)
            qTitle = e['stat']['question__title']
            qSlug = e['stat']['question__title_slug']
            qLevel = e['difficulty']['level']
            print(qNumber, qTitle, qLevel)
            qMap[qNumber] = [qTitle, URL_PROBLEM + qSlug, qLevel]
    
    score = 5 * my_result['ac_hard'] + 3 * my_result['ac_medium'] + 1 * my_result['ac_easy']
    print("=====================================")
    print('Solved / Total (Easy)  :' , stringFormatter(my_result['ac_easy']   , 4), '/', stringFormatter(count_easy, 4))
    print('Solved / Total (Medium):' , stringFormatter(my_result['ac_medium'] , 4), '/', stringFormatter(count_medium, 4))
    print('Solved / Total (Hard)  :' , stringFormatter(my_result['ac_hard']   , 4), '/', stringFormatter(count_hard,4))
    print('Solved / Total (All)   :' , stringFormatter(my_result['num_solved'], 4), '/', stringFormatter(my_result['num_total'],4))
    print('Total Score            :' , stringFormatter(score, 4))
    print("=====================================")
    print()

    qJson = json.dumps(qMap)
    f = open("lcode.json", "w")
    f.write(qJson)
    f.close()

    f = open("lcode.html", "w")
    f.write("""<!doctype html>
        <html>
        <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
        </head><body>
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        """)
    f.write(json2html.convert(json=qJson, table_attributes="class=\"table table-bordered table-hover\""))
    f.write('</body></html>')
    f.close()

def stringFormatter(s, num):
    s = str(s)
    return f'{s:>{num}}'

# run as a script (not module)
if __name__ == '__main__':
    showQuizListFromLeetcode()  
