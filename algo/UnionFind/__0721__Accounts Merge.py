class Solution:                      
    
    # Union-Find [O(nlogn): 20%]
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        print("2021/07/06")
        if not accounts:
            return []
        
        idxToEmail = []
        emailToIdx = collections.defaultdict(int)
        emailToName = collections.defaultdict(str)
        
        # Step1: Parse 
        idx = 0
        for data in accounts:
            name, emails = data[0], data[1:]
            for email in emails:
                if email in emailToIdx:
                    continue
                idxToEmail.append(email)
                emailToIdx[email] = idx
                idx += 1
                emailToName[email] = name
                
        #print(idxToEmail)
        #print(emailToIdx)
        #print(emailToName)
        
        # Step2: Union (with idx)
        parent = [-1] * len(idxToEmail)
        for data in accounts:
            name, emails = data[0], data[1:]
            for email in emails[1:]:
                self.union(parent, emailToIdx[emails[0]], emailToIdx[email])
    
        # Step3: Create nameToEmails 
        idxToEmails = collections.defaultdict(list)
        for i in range(len(parent)):
            head = self.find(parent, i)
            email = idxToEmail[i] #not head
            idxToEmails[head].append(email)
        #print(idxToEmails)
        
        # Step4: Create results 
        results = []
        for idx, emails in idxToEmails.items():
            result = [emailToName[idxToEmail[idx]]]
            result.extend(sorted(emails))
            results.append(result)
        return results
    
    def find(self, parent, e):
        if parent[e] == -1:
            return e
        else:
            return self.find(parent, parent[e]) 
            
    def union(self, parent, e1, e2):
        if e1 == e2:
            return 
        head1 = self.find(parent, e1)
        head2 = self.find(parent, e2)
        if head1 != head2:
            parent[head2] = head1
                    
    # ==========================================              
                    
    # Union-Find [O(nlogn): 18%]
    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []
        
        emailList = []
        emailToIdx = collections.defaultdict(int)
        emailToName = collections.defaultdict(str)
        
        #parse 
        idx = 0
        for data in accounts:
            name = data[0]
            emails = data[1:]
            for email in emails:
                if email in emailToIdx:
                    continue
                emailList.append(email)
                emailToIdx[email] = idx
                emailToName[email] = name
                idx += 1
        print(emailList)
        print(emailToIdx)

        
        #union
        parent = [-1] * len(emailList)
        for data in accounts:
            name = data[0]
            emails = data[1:]
            for email in emails[1:]:
                self.union(parent, emailToIdx[emails[0]], emailToIdx[email])
        #print(parent)
    
        # Form nameToEmails 
        nameToEmails = collections.defaultdict(list)
        for i in range(len(parent)):
            if parent[i] == -1:
                head = i
                email = emailList[i]
                name = emailToName[email]
                nameToEmails[i].append(email)
            else:
                #head = parent[i]
                head = self.find(parent, i)
                email = emailList[i] #not head
                name = emailToName[email]
                nameToEmails[head].append(email)
        #print(nameToEmails)
        
        results = []
        for idx, emails in nameToEmails.items():
            results.append([])
            results[-1].append(emailToName[emailList[idx]])
            results[-1].extend(sorted(emails))
        #print(results)
        return results
    
    
    def find(self, parent, e):
        if parent[e] == -1:
            return e
        else:
            return self.find(parent, parent[e]) #<--
            
    def union(self, parent, e1, e2):
        if e1 == e2:
            return 
        head1 = self.find(parent, e1)
        head2 = self.find(parent, e2)
        if head1 != head2:
            parent[head2] = head1
        
        
                            
                            
                        