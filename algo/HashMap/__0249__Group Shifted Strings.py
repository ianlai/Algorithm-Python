class Solution:
    
    # Hashmap [O(n): 83%]
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        stringMap = collections.defaultdict(list)
        for s in strings:
            diff = ord(s[0]) - ord('a')
            shifted_s = ""
            for c in s:
                shifted_c = ord(c) - ord('a') - diff
                if shifted_c < 0:
                    shifted_c += 26
                shifted_s += alphabets[shifted_c]
            stringMap[shifted_s].append(s)
        return stringMap.values()