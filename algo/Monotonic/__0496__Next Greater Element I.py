class Solution:
    
    #Monotonic stack [O(M+N): 73%]
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print("Code3: Monotonic stack")
        
        nextGreatMap = {}
        mstack = []
        
        # Step1: 
        # If any new item is greater, then good matching between [-1] to new 
        # pop out [-1] and record in map
        # finally, add the new into the stack (it also needs to find a good matching)
        for n2 in nums2:
            while mstack and mstack[-1] < n2:
                nextGreatMap[mstack[-1]] = n2
                mstack.pop()
            mstack.append(n2)
        
        # Step2: 
        # Pop out all the remaining because those couldn't find good matching 
        for s in mstack:
            nextGreatMap[s] = -1  
        #print(nextGreatMap)
        res = []
        for n1 in nums1:
            res.append(nextGreatMap[n1])
        return res
            
    # =====================================================  
    
    # Brute force with map[O(N + MN): 18%]
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print("Code2")
        res = []
        valToIdx = {}
        for i2, n2 in enumerate(nums2):
            valToIdx[n2] = i2
            
        for n1 in nums1:
            start = False
            inserted = False
            for i2 in range(valToIdx[n1], len(nums2)):
                n2 = nums2[i2] 
                if n1 == n2:
                    start = True
                if start:
                    if n2 > n1:
                        res.append(n2)
                        inserted = True
                        break
            if not inserted:
                res.append(-1)
        return res
    
    # =====================================================
    
    # Brute force [O(MN): 10%]
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print("Code1")
        res = []
        for n1 in nums1:
            start = False
            inserted = False
            for n2 in nums2:
                if n1 == n2:
                    start = True
                if start:
                    if n2 > n1:
                        res.append(n2)
                        inserted = True
                        break
            if not inserted:
                res.append(-1)
        return res