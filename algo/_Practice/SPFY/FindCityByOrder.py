'''
Find all cities which can satify the order (3 type of peppers)

City    |    J   |   H   |   M   |
======================================
Tokyo   |    5       3       2 
Taipei  |    9       1       8
Seattle |    3       5       7   
Seoul   |    0       2       9 
London  |    4       4       4

Input:
1. {"J":3, "H":4, "M": 2}  //["Seattle", "London"]
2. {"M": 8}                //["Taipei", "Seoul"]
'''

def initData():
    cities = [
        {
            "Name": "Tokyo",
            "Peppers": [5, 3, 2]   #J, H, M
        },
        {
            "Name": "Taipei",
            "Peppers": [9, 1, 8]   #J, H, M
        },
        {
            "Name": "Seattle",
            "Peppers": [3, 5, 7]   #J, H, M
        },
        {
            "Name": "Seoul",
            "Peppers": [0, 2, 9]   #J, H, M
        },
        {
            "Name": "London",
            "Peppers": [4, 4, 4]   #J, H, M
        }
    ]
    return cities


def findCitiesByOrder(cities, order):
    res = []
    for city in cities:
        if "J" in order and city["Peppers"][0] < order["J"]:
            continue
        if "H" in order and city["Peppers"][1] < order["H"]:
            continue
        if "M" in order and city["Peppers"][2] < order["M"]:
            continue
        res.append(city["Name"])
    return res

cities = initData()

order1 = {"J": 3, "H": 4, "M": 2}
order2 = {"M": 8}

foundCities1 = findCitiesByOrder(cities, order1)
foundCities2 = findCitiesByOrder(cities, order2)

print(foundCities1)
print(foundCities2)

'''
Improvement1: Use Pepper dictionary instead of list
Improvement2: Use for loop to iterate the peppers in findCitiesByOrder function 
'''