class Solution:
    
    # 2022/05/31 
    # Customized comparator (including digit and letter) 
    # [O(N + NlogN*L): 86% / O(NL): 75%]
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        print("Code2")
        
        def comparator(l1, l2):
            l1 = l1.split()
            l2 = l2.split()
            if l1[1].isdigit() and l2[1].isdigit():
                return 0
            elif l1[1].isdigit() or l2[1].isdigit():
                return 1 if l1[1].isdigit() else -1  #數字要在後面，所以如果l1是數字，代表順序是錯的，要換，所以是1 
            else:
                p = 1
                # Compare1 - arr[1:]
                while p != len(l1) and p != len(l2):
                    if l1[p] < l2[p]:
                        return -1
                    elif l1[p] > l2[p]:
                        return 1
                    p += 1

                # Compare2 - len
                if len(l1) < len(l2):
                    return -1
                elif len(l1) > len(l2):
                    return 1

                # Compare3 - arr[0] (identifier)
                if l1[0] < l2[0]:
                    return -1
                elif l1[0] > l2[0]:
                    return 1
            
        logs.sort(key = cmp_to_key(comparator))
        return logs
        
    # 2022/05/31 
    # Customized comparator (letter only) [O(N + NlogN*L): 46% / O(NL): 36%]
    def reorderLogFiles1(self, logs: List[str]) -> List[str]:
        print("Code1")
        def comparatorLetterLog(l1, l2):
            l1 = l1[0] #extract the log arr (l1[1] is the index)
            l2 = l2[0] #extract the log arr (l1[1] is the index)
            #l1 = l1.split()
            #l2 = l2.split()

            p = 1
            # Compare1 - arr[1:]
            while p != len(l1) and p != len(l2):
                if l1[p] < l2[p]:
                    return -1
                elif l1[p] > l2[p]:
                    return 1
                p += 1
                
            # Compare2 - len
            if len(l1) < len(l2):
                return -1
            elif len(l1) > len(l2):
                return 1
            
            # Compare3 - arr[0] (identifier)
            if l1[0] < l2[0]:
                return -1
            elif l1[0] > l2[0]:
                return 1
            
            return 0
        
        letterLog, digitLog = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digitLog.append(log)
            else:
                letterLog.append(log)
        
        letterLogArr = []  #log, idx
        for idx, log in enumerate(letterLog):
            logArr = log.split()
            letterLogArr.append([logArr, idx])
        
        letterLogArr.sort(key = cmp_to_key(comparatorLetterLog))
        #letterLog.sort(key = cmp_to_key(comparatorLetterLog))  #We can sort letterLog direct but need to split everytime 
        
        res = [None] * len(logs)
        
        # Need to compose the letterLog back into the res first part
        for i in range(len(letterLogArr)):
            idx = letterLogArr[i][1]
            res[i] = letterLog[idx]
            
        # Just need to insert th letterLog one by one if we sort letterLog directly 
        # for i in range(len(letterLog)):
        #     res[i] = letterLog[i]
        
        for i in range(len(digitLog)):
            res[i + len(letterLogArr)] = digitLog[i]
        
        return res 