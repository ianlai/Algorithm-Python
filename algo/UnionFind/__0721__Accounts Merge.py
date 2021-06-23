class Solution:                            
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
        #print(emailList)
        #print(emailToIdx)

        
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
        
        
                            
                            
                        