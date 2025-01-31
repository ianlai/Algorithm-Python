'''
Keyword targeting is one type of campaign strategy that advertisers use to spend their budget. It involves the advertiser to specify 
keywords that will result in their ad being shown to the end user.  Advertisers will pick keywords that pertain to their product in 
hopes of matching what users are searching for and result in higher chance user will click the ad.  You will write code that will 
simulate an ad server that contains advertisers keywords and how it responds to incoming search queries.  Initial requirements are 
for the ad server to return the advertiser that has the best matching keywords compared with each search query.  "Best matching" 
advertiser for a search query is defined as the advertiser that has matching keyword in the lowest position in his list of keywords.

For example, assuming we have these 2 advertisers keywords:

Advertiser X: shoes, sneakers, slippers  
Advertiser Y: sneakers, sandals, socks

Advertiser X would be best match for query "shoes" (position 1) and "slippers" (position 3) since these queries don't exist for Advertiser Y.

Advertiser Y would be best match for query "sneakers" (position 1) since it is position 2 for that keyword in Advertiser X.

The inputs to your program is a list of advertisers keywords where position in the list identifies the advertiser:


input1
    [
      ["shoes","sneakers","slippers"],  # 0
      ["sneakers","sandals","socks"],   # 1
      ["shirts","pants","ties"],        # 2
      ["ties","socks","hats"]           # 3
    ]

and list of search queries:
input2
    ["shoes","slippers","sneakers","socks","pants","hats"]

The outputs (can be to console) would first be this list of advertiser identifiers representing the best matching advertiser 
for each input search query:

output1:
    0,0,1,3,2,3

then followed by this report which is a list of counts per advertiser, ordered by original list order of the advertiser:

output2: 
    ad0: 2   
    ad1: 1  
    ad2: 1  
    ad3: 2  

Write a program that will take these 2 inputs and return above outputs given the above known information. Structure your code so 
that it can easily adapt to changing future requirements of:

a) how "best matching" is determined  
b) how the report can be modified or additional reports can be added



Requirements have changed so that for each keyword, the advertiser is allowed to bid a price.  The "best match" now means the
advertiser with the highest bid price for that keyword.

The change to advertiser input is:

    [
      [["shoes","1.25"],["sneakers","1.50"],["slippers","1.50"]],
      [["sneakers","1.00"],["sandals","1.00"],["socks","1.00"]],
      [["shirts","1.00"],["pants","1.00"],["ties","1.00"]],
      [["ties","0.75"],["socks","0.75",["hats","0.75"]]
    ]

where each keyword now has a corresponding bid price.  Using the same input search queries, the new output for list of best matching
advertiser identifiers would be:

    0,0,0,1,2,3
    
================================    
input1
    [
      ["shoes","sneakers","slippers"],  # ad0
      ["sneakers","sandals","socks"],   # 1
      ["shirts","pants","ties"],        # 2
      ["ties","socks","hats"]           # 3
    ]

and list of search queries:
input2
    ["shoes","slippers","sneakers","socks","pants","hats"]

'''
class Advertiser:
    def __init__(self, keywordArray = ["shoes","sneakers","slippers"], mode):
        self.name = name
        self.keywordsToIdx = {}
        
        for idx, val in enumerate(keywordArray):
            keywordsToIdx[val] = idx #idx
            keywordsToIdx[val] = idx #price
            
    def addKeyword(key):
    
    
class KeywordTarget:
    def __init__(self, advertiserArray, queries):
        self.advertiserArray = advertiserArray
        self.queries = queries
    
    def generateOutput(self):
        ads = self.advertiserArray[keywordsToIdx]
        for q in queries:
            minVal = inf 
            for ad, val in ads.items():
                if q not in ad:
                    continue
                minVal = min(minVal, val)
                
        

