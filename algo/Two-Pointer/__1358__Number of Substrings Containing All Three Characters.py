class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        countMap = collections.defaultdict(int)
        res = 0
        left = 0
        for right in range(len(s)):
            countMap[s[right]] += 1
            while countMap["a"] > 0 and countMap["b"] > 0 and countMap["c"] > 0:
                countMap[s[left]] -= 1
                left += 1
                res += len(s) - right 
        return res


# JAVA
# 
# class Solution {
#     public int numberOfSubstrings(String s) {
#         int[] counter = new int[]{0, 0, 0};
#         int res = 0;
#         int idx = 0;
#         for(int i = 0; i < s.length(); i++){
#             counter[Character.getNumericValue(s.charAt(i)) - Character.getNumericValue('a')] += 1; 
#             while(counter[0] > 0 && counter[1] > 0 && counter[2] > 0){
#                 counter[Character.getNumericValue(s.charAt(idx)) - Character.getNumericValue('a')] -= 1; 
#                 idx += 1;
#                 res += s.length() - i; 
#             }
#         }
#         return res; 
#     }
# }