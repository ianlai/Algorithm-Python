class Solution:    
    
    # Monotonic Stack [O(n): 19%]
    # One pass -> Normal array
    # Two pass -> Circular array
    # Save the index instead of saving the value 
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        print("Code2")
        stack = []
        res = [-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        #print(res)
        return res
                
    # ==================================================

    #Incorrect
    def nextGreaterElements1(self, nums: List[int]) -> List[int]:
        
        mstack = []
        nextGreater1 = [inf] * len(nums)
        for i, v in enumerate(nums):
            while mstack and mstack[-1][1] < v:
                ni, nv = mstack.pop()
                nextGreater1[ni] = v
            mstack.append((i, v))
        #print(nextGreater)
        
        
        for i in range(len(nums)-1, -1, -1):
            if nextGreater1[i] == inf:
                nextStart = i 
                break
        #nextStart = nextGreater1.index(inf)
        print("NextStart = ", nextStart)
        
        nums2 = nums[nextStart:] + nums[:nextStart]
        mstack = []
        print("1:", nextGreater1)
        print("  ", nums)
        print("  ", nums2)
        nextGreater2 = [inf] * len(nums)
        for i, v in enumerate(nums2):
            #print(i, v)
            while mstack and mstack[-1][1] < v:
                ni, nv = mstack.pop()
                nextGreater2[ni] = v
                # ni -= nextStart 
                # if ni < 0 :
                #     ni += len(nums2)
                # nextGreater[ni] = v
            mstack.append((i, v))
        print("2:", nextGreater2)
        res = nextGreater1[:nextStart] + nextGreater2[:len(nums)-nextStart]
        
        for i, v in enumerate(res):
            if v == inf:
                res[i] = -1
        return res
                    