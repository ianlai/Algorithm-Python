class Solution:

    # Remove hasOdd variable
    def longestPalindrome(self, s: str) -> int:
        print("2")
        charCount = collections.defaultdict(int)
        for c in s:
            charCount[c] += 1
        
        longest = 0
        for count in charCount.values():
            if count % 2 == 1:  #odd
                longest += count - 1
            else:
                longest += count
        return longest if len(s) == longest else longest + 1

    # Use hasOdd variable
    def longestPalindrome1(self, s: str) -> int:
        print("1")
        charCount = collections.defaultdict(int)
        for c in s:
            charCount[c] += 1
        
        hasOdd = False
        longest = 0
        for char, count in charCount.items():
            if count % 2 == 1:  #odd
                hasOdd = True
                longest += count - 1
            else:
                longest += count
        return longest + 1 if hasOdd else longest
