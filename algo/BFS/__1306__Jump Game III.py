class Solution:
    
    
    # 2022/02/16
    # BFS [O(n): 64%]
    def canReach(self, arr: List[int], start: int) -> bool:        
        visited = set()
        deq = collections.deque([start])
        while deq:
            idx = deq.popleft()
            if idx in visited:
                continue
            visited.add(idx)
            if arr[idx] == 0:
                return True
            if 0 <= idx + arr[idx] < len(arr):
                deq.append(idx + arr[idx])
            if 0 <= idx - arr[idx] < len(arr):
                deq.append(idx - arr[idx])
        return False