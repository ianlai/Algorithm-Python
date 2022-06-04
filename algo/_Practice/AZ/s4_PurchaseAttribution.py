=begin 

Let’s write a purchase attribution algorithm. You’ll be given a file of ad impressions and a separate file of purchase events. 
The goal is to figure out how many total impressions each ad served, and how many purchases can be attributed to each ad. 
If multiple ad impressions could be attributed to the same purchase, then the most recent ad impression should be picked 
(unless it takes place after the purchase event). Assume that the files are sorted in ascending order on the timestamp field.

Ad traffic log (impressions):

ads= 
// <ad_timestamp>   <ad-id>    <customer-id>    <product-id>
// 00:00:01        123456           345831     		 BRTX762
// 00:00:21        223999           345831     		 A000GHX657
//...

Purchase log:

purchaseLog = 
// <purchase_timestamp>     <customer-id>       <product-id>
// 00:00:06        345831             BRTX762
// 00:00:27        574328             A000GHX657
//...

Desired Output:

// <ad-id>        <total-impressions>     <total-purchases>
// 123456         1                       1
// 223999         1                       0
//...
=end

trafficLog = []


def generateAdMap(ads):
    adMap = collections.defaultdict(list)  # (customerId, productId) -> [adTime, adId, adImpression]
    for adTime, adId, customerId, productId in ads:
        adMap[(customerId, productId)][2] += 1   #total impression 
        
        if (customerId, productId) in adMap:
            continue
        adMap[(customerId, productId)][0] = adTime
        adMap[(customerId, productId)][1] = adId
    return adMap

def generateOutput(adMap, purchaseLog):
    output = []
    adToCounts = collections.defaultdict(list)  # adId -> (total impression, total purchase)
    for purchaseTime, customerId, productId in purchaseLog:
        if (customerId, productId) in adMap:
            adId = adToCounts[adId][1] 
            adToCounts[adId] = adMap[(customerId, productId)][2] # total impression 
            
            if purchaseTime > adMap[0]: 
                adId = adMap[(customerId, productId)][1]
                adToCounts[adId][1] += 1  #total purchase incremented by 1 
            
    for adId, impression, purchase in adToCounts.items():
        output.append(adId, impression, purchase)
    return output 
    
    

