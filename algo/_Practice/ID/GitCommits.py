'''
Git Commits (Ancestor)
每個節點有parents，是有向圖的題目，且沒有環，所以是DAG。
''' 

import collections
class Node:
    def __init__(self, id):
        self.id = id 
        self.parents = set()
    def __str__(self):
        return str(self.id)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n1.parents.update([n2, n3])  #base1
n3.parents.add(n7) 
n4.parents.update([n5, n8])  #base2
n5.parents.add(n6) 
n6.parents.add(n7) 
n6.parents.add(n8) 
n8.parents.add(n7) 

def findAncestors(node):
    q = collections.deque([node])
    visited = set()
    #visited.add(node) #not including the root

    while q: 
        cur = q.popleft()
        for par in cur.parents:
            if par in visited:
                continue
            visited.add(par)
            q.append(par)
    return list(visited) 


'''
雙向BFS (說是雙向應該說是雙源，兩邊都朝目標前進，而不是互相靠近)
這是優化過的版本 

基礎版本應該是先對A做一次BFS，找到所有Parents之後，
才用B也做BFS，每次檢查visited_A，找到就跳出。
但基礎版本一定必需要把A的Ancestors都找過一次。

優化版本則是A, B同步往上走。但為了不要錯過，A必須檢查B，而且B也要檢查A，才不會發生錯過的情形。

假設A有X個祖先，B有Y個祖先（X+Y >= N 因為有重複）。
基礎版本T.C. = O(X + LCA層)
雙向版本T.C. = O(LCA層)
'''
def findLCA(A, B):
    q1 = collections.deque([A])
    q2 = collections.deque([B])
    v1 = set()
    v2 = set()
    
    while q1 and q2:
        cur1 = q1.popleft()
        cur2 = q2.popleft()
        for par1 in cur1.parents:
            if par1 in v1:
                continue
            if par1 in v2: #found
                return par1
            v1.add(par1)
            q1.append(par1)
        
        for par2 in cur2.parents:
            if par2 in v2:
                continue
            if par2 in v1: #found
                return par2
            v2.add(par2)
            q2.append(par2)
    return None



for ancestor in findAncestors(n1):
    print("n1's ancestors:", ancestor)

for ancestor in findAncestors(n4):
    print("n4's ancestors:", ancestor)

print(findLCA(n1, n4))  #7
print(findLCA(n6, n4))  #8