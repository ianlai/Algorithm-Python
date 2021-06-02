"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        deque = collections.deque([root])
        count = 0
        while deque:
            #print([x.val for x in deque])
            for _ in range(len(deque)):
                cur = deque.popleft()
                #print(cur.val, [x.val for x in cur.children])
                deque.extend(cur.children)
                # for node in cur.children:
                #     deque.append(node)
            count += 1
            #print("layer:", count)
        return count


### Golang 
# /**
#  * Definition for a Node.
#  * type Node struct {
#  *     Val int
#  *     Children []*Node
#  * }
#  */

# func maxDepth(root *Node) int {
#     if root == nil{
#         return 0
#     }
#     deq := make([]Node, 0)
#     deq = append(deq, *root)
#     maxHeight := 0
#     for len(deq) != 0 {
#         size := len(deq)
#         //fmt.Println(size)
#         for i := 0; i < size; i++{
#             cur := deq[0]
#             deq = deq[1:]
#             for j := 0; j < len(cur.Children); j++{
#                 deq = append(deq, *cur.Children[j])
#             }
#         } 
#         maxHeight++ 
#     }     
#     return maxHeight
# }