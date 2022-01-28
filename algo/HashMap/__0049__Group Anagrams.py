class Solution:
    
    # 2022/01/28
    # Use sorted string as the map key [94%]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print("Code2")
        stringMap = collections.defaultdict(list)
        for s in strs:
            stringMap[''.join(sorted(s))].append(s)
        return stringMap.values()

    # ==================================================
    # 2021/04/18
    # Use sorted string as the map key [35%]
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        print("Code1")
        if strs is None or len(strs) == 0:
            return []
        
        ans = []
        keyToList = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in keyToList:
                keyToList[sortedStr].append(s)
            else:
                keyToList[sortedStr] = []
                keyToList[sortedStr].append(s)
        #print(keyToList)
        for key in keyToList:
            ans.append(keyToList[key])

        return ans
                    