class Solution:
    
    # BFS with whole path; removing redanduncy on the fly [41%]
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        print("BFF with whole path")
        
        wordSet = set(wordList)
        nodeMap = collections.defaultdict(list)
        
        #Find possible next words and do memoization
        def findNextWords(cur):
            if cur in nodeMap:
                return nodeMap[cur]
            nextWords = []
            for i in range(len(cur)):
                for nc in "abcdefghijklmnopqrstuvwxyz":
                    word = cur[:i] + nc + cur[i+1:]
                    if word in wordSet:
                           nextWords.append(word)
            nodeMap[cur] = nextWords
            return nextWords
        
        #BFS to find the min distance
        def findMinDistance():
            distance = {beginWord: [1, [tuple([beginWord])]]}
            deq = collections.deque([beginWord])
            res = []
            minDistance = inf
            while deq:
                cur = deq.popleft()
                curDistance, curPaths = distance[cur][0], distance[cur][1]
                nextWords = findNextWords(cur)
                
                for nextWord in nextWords:
                    nextDistance = curDistance + 1
        
                    # Add into deq when (1) new word or (2) new distance is not larger then recorded distance
                    if nextWord in distance and nextDistance > distance[nextWord][0]:
                        continue
                    deq.append(nextWord)
                    
                    # Remove duplicates on the fly
                    nextPaths = set()
                    
                    # Compose new paths based on the curren paths (might be multiple)
                    if nextWord in distance: 
                        nextPaths = distance[nextWord][1]
                    for idx, curPath in enumerate(curPaths):
                        nextPaths.add(curPath + tuple([nextWord]))
                        
                    distance[nextWord] = [nextDistance, nextPaths] 
                    
            if endWord in distance:
                #res = list(set([tuple(path) for path in distance[endWord][1]]))
                res = list(distance[endWord][1])
            return res
        
        res = findMinDistance()
        return res
        
    # =============================================================
    # BFS + DFS [TLE]
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        print("BFS + DFS")
        
        wordSet = set(wordList)
        nodeMap = collections.defaultdict(list)
        
        #Find possible next words and do memoization
        def findNextWords(cur):
            if cur in nodeMap:
                return nodeMap[cur]
            nextWords = []
            for i in range(len(cur)):
                for nc in "abcdefghijklmnopqrstuvwxyz":
                    word = cur[:i] + nc + cur[i+1:]
                    if word in wordSet:
                           nextWords.append(word)
            nodeMap[cur] = nextWords
            return nextWords
        
        #BFS to find the min distance
        def findMinDistance():
            distance = {beginWord: 1}
            deq = collections.deque([beginWord])
            while deq:
                cur = deq.popleft()
                nextWords = findNextWords(cur)
                for nextWord in nextWords:
                    if nextWord in distance:
                        continue
                    deq.append(nextWord)
                    distance[nextWord] = distance[cur] + 1 
                    if nextWord == endWord:
                        return distance[nextWord]
            return None
        
        #Helper function for DFS
        def dfs(cur, res, visited, maxLayer, layer):
            if layer >= maxLayer:
                if cur[-1] == endWord:
                    res.append(cur)
                return

            nextWords = findNextWords(cur[-1])
            for nextWord in nextWords:
                if nextWord in visited:
                    continue
                visited.add(nextWord)
                dfs(cur + [nextWord], res, visited, maxLayer, layer + 1)
                visited.remove(nextWord)
            
        #DFS to find the paths
        def findPathsWithMinDistance(minD):
            visited = set()
            res = []
            dfs([beginWord], res, visited, minD, 1)
            return res
        
        res = []
        minDistance = findMinDistance()
        if minDistance == None:
            return []
        else:
            res = findPathsWithMinDistance(minDistance)
            return res
        
    # =============================================================
    # Only BFS -> Can only find one path 
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        print("BFS + can only find one path")
        def findNextWords(cur):
            res = []
            for i in range(len(cur)):
                for nc in "abcdefghijklmnopqrstuvwxyz":
                    word = cur[:i] + nc + cur[i+1:]
                    if word in wordSet:
                           res.append(word)
            return res
        
        wordSet = set(wordList)
        deq = collections.deque([beginWord])
        distance = collections.defaultdict(list)
        distance[beginWord] = [1, [beginWord]]
        res = []
        
        while deq:
            cur = deq.popleft()
            nextWords = findNextWords(cur)
            print(distance)
            for nextWord in nextWords:
                if nextWord in distance:
                    continue
                print(">>>", nextWord)
                deq.append(nextWord)
                distance[nextWord].append(distance[cur][0] + 1)
                distance[nextWord].append(distance[cur][1] + [nextWord])
                if nextWord == endWord:
                    res.append(distance[nextWord][1])
        return res