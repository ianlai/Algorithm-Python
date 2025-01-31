class Solution:

    # 2021/05/06
    # Store the parents; check the ancestor for each node [O(n2): 5%]
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        print("Code2")
        #parents = collections.defaultdict(int)
        parents = {}
        for i in range(n):
            if leftChild[i] in parents:
                return False
            if leftChild[i] != -1:
                parents[leftChild[i]] = i
            if rightChild[i] in parents:
                return False
            if rightChild[i] != -1:
                parents[rightChild[i]] = i
        
        root = -1 
        for i in range(n):
            cur = i
            visited = set([cur])
            while cur in parents:
                cur = parents[cur]
                if cur in visited:
                    return False
                visited.add(cur)
            if root != -1 and root != cur:
                return False
            root = cur
        return True
        
        
    # Incorrect  
    def validateBinaryTreeNodes1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        print("Code1")
        globalVisited = set()
        for i in range(n):
            curVisited = set()
            deq = collections.deque([i])
            while deq:
                cur = deq.popleft()
                if cur in curVisited:
                    return False
                if cur in globalVisited:
                    break
                curVisited.add(cur)
                globalVisited.add(cur)

                left = leftChild[cur]
                if left != -1:
                    deq.append(left)
                right = rightChild[cur]
                if right != -1:
                    deq.append(right)
        return len(globalVisited) == n