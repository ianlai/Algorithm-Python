class Solution:
    
    # 2021/10/19 
    # BFS + Search whole wordList [O(W*L*26): 41%]
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("BFS + list possible neighbor words")
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
        distance = {beginWord: 1}
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
        return 0
    
    # =====================================

    # 2021/10/19 
    # BFS + Search whole wordList [TLE, 34 / 49 test cases passed]
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("BFS + search whole wordList")
        
        def isNeighbor(word1, word2):
            if len(word1) != len(word2):
                return False
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                if diff >= 2:
                    return False
            return True if diff == 1 else False
            
        def findNextWords(cur):
            res = []
            for word in wordList:
                if isNeighbor(cur, word):
                    res.append(word)
            return res
            
        deq = collections.deque([beginWord])
        distance = {beginWord: 1}
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
        return 0
        
    # =====================================

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("Using distance dict")
        if not beginWord or not endWord or not wordList:
            return 0
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        deq = collections.deque([beginWord])
        visited = set([beginWord]) #Add beginWord at start
        wordSet = set(wordList)    #TLE if using wordList
        distance = {beginWord: 1}
        
        while deq:
            cur = deq.popleft()
            #print(cur)
            if endWord == cur:
                return distance[cur]
            for nextWord in self.getNextWords(cur, wordSet):
                if nextWord in visited:
                    continue
                #print(">", nextWord)
                deq.append(nextWord)
                visited.add(nextWord)
                distance[nextWord] = distance[cur] + 1
            #print("---")
        return 0
    
    def getNextWords(self, word, wordSet):  
        nextWords = []
        for i in range(len(word)):
            for alphabet in self.alphabets:
                newWord = word[:i] + alphabet + word[i+1:]
                if newWord in wordSet:
                    nextWords.append(newWord)
        return nextWords
    
    # =====================================
    
    # BFS, using layer [34%]
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("Using layer variable")
        if not beginWord or not endWord or not wordList:
            return 0
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        
        deq = collections.deque([beginWord])
        visited = set([])
        wordSet = set(wordList) #TLE if using wordList
        layer = 0
        while deq:
            layer += 1
            for _ in range(len(deq)):
                cur = deq.popleft()
                #print(cur)
                if cur == endWord:
                    return layer
                for nextWord in self.getNextWords1(cur, wordSet):
                    if nextWord in visited:
                        continue
                    deq.append(nextWord)
                    visited.add(nextWord)
            #print("---")
        return 0
    
    def getNextWords1(self, word, wordSet):  
        nextWords = []
        for i in range(len(word)):
            for alphabet in self.alphabets:
                newWord = word[:i] + alphabet + word[i+1:]
                if newWord in wordSet:
                    nextWords.append(newWord)
        return nextWords