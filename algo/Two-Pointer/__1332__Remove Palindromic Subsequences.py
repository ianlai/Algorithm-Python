class Solution:

    # 2022/06/09
    # Two pointer to check palindrome or not [O(N): 93% / O(1): 10%]
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        isPalindrome = True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                isPalindrome = False
                break
                
        if isPalindrome:
            return 1
        else:
            return 2
            

    # Two pointer [Incorrect]
    def removePalindromeSub1(self, s: str) -> int:
        arr = list(s)
        step = 0
        while any(arr):
            left, right = 0, len(arr) - 1
            print(arr)
            
            while left <= right: 
                while not arr[left]:
                    left += 1
                while not arr[right]:
                    right -= 1
                print(step, left, right)
                if arr[left] == arr[right]:
                    arr[left] = None
                    arr[right] = None
                    left += 1
                    right -= 1
                else:
                    right -= 1
            step += 1
        return step
                
            
            
        