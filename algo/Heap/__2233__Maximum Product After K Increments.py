MODULE = 10 ** 9 + 7
class Solution:
    
    # Heap, target is to equlize the num as close as possible [O(klogn): 10%]
    def maximumProduct(self, nums: List[int], k: int) -> int:
        print("Code2")
        
        heapq.heapify(nums)
        for _ in range(k):
            pop = heapq.heappop(nums)
            heapq.heappush(nums, pop+1)
        res = 1
        for num in nums:
            res = res * num % MODULE
        return res
    
    # ==============================================
    
    # Memoization [TLE]
    def maximumProduct1(self, nums: List[int], k: int) -> int:
        print("Code1")
        self.maxVal = 0 
        #@lru_cache
        def dfs(counter, K):
            #print("K:", K, counter)
            if K == 0:
                cur = 1
                #print("K:", K)
                for k, v in enumerate(counter):
                    if v == 0:
                        continue
                    cur = (k * v * cur) % MODULE
                    #print("k,v", k, v)
                    
                self.maxVal = max(cur, self.maxVal) 
                print(counter, cur, self.maxVal)
                return 
                
            #for k, v in list(counter.items()):
            for k, v in enumerate(counter):
                if v == 0:
                    continue
                
                counter[k+1] += 1
                counter[k] -=1
                # if counter[k] == 0:
                #     del counter[k]
                dfs(counter, K-1)
                counter[k+1] -= 1
                # if counter[k+1] == 0:
                #     del counter[k+1]
                counter[k] +=1
        
        #counter = collections.Counter(nums)
        counter = [0] * (max(nums) + k + 10)
        #print(counter)
        for i, v in enumerate(nums):
            counter[v] += 1
            
        dfs(counter, k)
        return self.maxVal