'''
https://leetcode.com/problems/implement-queue-using-stacks/
Implement Queue
- push()
- pop()
- peek() 
- empty()
'''

'''
(1) Use array (stack) - insert adjust 
'''

class MyQueue():
    def __init__(self):
        print("Queue by Stack")
        self.s1 = []
        self.s2 = []
    
    def push(self, v):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(v)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return len(self.s1) == 0 

q = MyQueue()
print( q.empty() ) #True
q.push(1)
q.push(2)
q.push(3)
print( q.pop() )  #1
q.push(4)
print( q.empty() )  #False
print( q.pop() )  #2
print( q.peek() ) #3
print( q.peek() ) #3
print( q.pop() )  #3
q.push(5) 
print( q.pop() )  #4
print( q.empty() )  #False
print( q.pop() )  #5
print( q.empty() )  #True

'''
(2) Use linkedlist 
'''
class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None
class MyQueueLL():
    def __init__(self):
        print("Queue by LL")
        self.dummy = Node()
        self.head = self.dummy
        self.tail = self.dummy

    def push(self, v):
        self.tail.next = Node(v)
        self.tail = self.tail.next

    def pop(self):
        if self.empty():
            return None
        res = self.head.next.val
        self.head = self.head.next
        return res
        
    def peek(self):
        if self.empty():
            return None
        return self.head.next.val

    def empty(self):
        return self.head.next is None

q = MyQueueLL()
print( q.empty() ) #True
q.push(1)
q.push(2)
q.push(3)
print( q.pop() )  #1
q.push(4)
print( q.empty() )  #False
print( q.pop() )  #2
print( q.peek() ) #3
print( q.peek() ) #3
print( q.pop() )  #3
q.push(5) 
print( q.pop() )  #4
print( q.empty() )  #False
print( q.pop() )  #5
print( q.empty() )  #True