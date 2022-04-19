'''
======================================
[Problem-1] Subdomain visit count

We are given a list cpdomains of count-paired domains. 
We would like a list of count-paired domains, (in the same format as the input, and in any order), 
that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
'''






'''
======================================
[Problem-2] Longest Common Continuous Subarray

Input: 
[
  ["3234.html", "xys.html", "7hsaa.html"], // user1
  ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]
Output:  輸出兩個人最長連續相同的訪問紀錄
["xys.html", "7hsaa.html"]

'''








'''
======================================
[Problem-3] Ads Conversion Rate

The people who buy ads on our network don't have enough data about how ads are working for their business. 
They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page
after clicking one of their ads:

 # Each user completed 1 purchase.
 completed_purchase_user_ids = [
   "3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a
user clicked on one of our ads:
 ad_clicks = [
  #"IP_Address,Time,Ad_Text",
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
       
The client also sent over the IP addresses of all their users.

注意不是所有的IP都在此mapping內
       
all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]
       
Write a function to parse this data, determine how many times each ad was clicked,
then return the ad text, that ad's number of clicks, and how many of those ad clicks
were from users who made a purchase.

 Expected output:
 Bought Clicked Ad Text
 1 of 2  2017 Pet Mittens
 0 of 1  The Best Hollywood Coats
 3 of 3  Buy wool coats for your pets
'''

completed_purchase_user_ids = [
   "3123122444","234111110", "8321125440", "99911063"]

# multiple-to-multiple 
ad_clicks = [
  #"IP_Address,Time,Ad_Text",
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

# 1-to-1 
all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]

import collections
def calculateConversionRate():
    
    convertedIds = set(completed_purchase_user_ids)

    #有些IP沒有mapping，所以給他一個預設ID=0 (必須確保 completed_purchase_user_ids裡面沒有0)
    ipToId = collections.defaultdict(int)  
    for record in all_user_ips:
        id, ip = record.split(',')
        ipToId[ip] = id

    adToIdCount = collections.defaultdict(lambda : collections.defaultdict(int))
    for record in ad_clicks:
        ip, _, ad = record.split(',')
        adToIdCount[ad][ipToId[ip]] += 1
    
    res = []
    for ad, idCount in adToIdCount.items():
        countTotal = 0
        countConverted = 0
        for id, count in idCount.items():
            countTotal += count
            if id in convertedIds:
                countConverted += count
        res.append([countConverted, countTotal, ad])
    return res

res = calculateConversionRate()

for row in res:
    print(row)