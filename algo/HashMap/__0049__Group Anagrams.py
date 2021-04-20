class Solution:
    
    # Use sorted string as the map key
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
            