class Solution:
    
    '''
    解答的作法，速度最快。這題就是做BFS，但考點關鍵在於怎麼找到相連的字。
    一個目標字要找到相連的其他字所需時間：
    (1) 從wordList內掃描: O(WL) 
    (2) 對目標字的每一個字元做26字母變換: O(26L)
    (3) 把目標字轉成代表字，再把每個代表字存的array取出: O(LL) //但需要preprocessing把每個字存入相對應代表字array
    '''
    # BFS + list alphabet combination [O(WLL + WLL): 73% / O(WLL): 58%]
    def ladderLength(self, beginWord, endWord, wordList):
        print("Code7 (fastest)")
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        # Since all words are of same length.
        L = len(beginWord)
        
        # {"h*t": ["hot", "hat", "hit"]}
        # Form map -> TC: O(WLL)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) #TC: O(L)

        # BFS -> TC: O(WLL)
        queue = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
    
    
    # 2022/05/08
    # BFS + list alphabet combination [O(W*L*26): 15% / O(W): 58%]
    # 用visited判斷是否走過，距離則直接放在node放入deq
    def ladderLength6(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("Code6 (ok)")
        def findNextWords(word, wordSet):
            nextWords = []
            for i in range(len(word)):
                for j in range(26):
                    ch = chr(ord('a') + j)
                    cur = word[:i] + ch + word[i+1:]
                    if cur in wordSet:
                        nextWords.append(cur)
            return nextWords
            
        wordSet = set(wordList)
        visited = set(beginWord)
        deq = collections.deque([(beginWord, 1)])
        while deq:
            cur, level = deq.popleft()
            for nxt in findNextWords(cur, wordSet):
                if nxt in visited:
                    continue
                visited.add(nxt)
                if nxt == endWord:
                    return level + 1
                deq.append((nxt, level + 1))
        return 0
    
    # 2022/05/08
    # BFS + list alphabet combination [O(W*L*26): 15% / O(W): 58%]
    # 用distance map來做到存visited和level的效果
    def ladderLength5(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("Code5")
        def findNextWords(word, wordSet):
            nextWords = []
            for i in range(len(word)):
                for j in range(26):
                    ch = chr(ord('a') + j)
                    cur = word[:i] + ch + word[i+1:]
                    if cur in wordSet:
                        nextWords.append(cur)
            return nextWords
            
        wordSet = set(wordList)
        distance = {beginWord: 1}
        deq = collections.deque([beginWord])
        while deq:
            cur = deq.popleft()
            for nxt in findNextWords(cur, wordSet):
                if nxt in distance:
                    continue
                distance[nxt] = distance[cur] + 1
                if nxt == endWord:
                    return distance[nxt]
                deq.append(nxt)
        return 0
                
        
    # 2021/10/19 
    # BFS + Search whole wordList [O(W*L*26): 41%]
    def ladderLength4(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        print("Code4: BFS + list possible neighbor words")
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