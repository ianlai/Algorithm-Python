class Solution:
    
    # Monotonic stack [O(n): 78%]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while mstack and temperatures[mstack[-1]] < v:
                outIndex = mstack.pop()
                res[outIndex] = i - outIndex
            mstack.append(i)
        return res