#gfg
#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def summ(node):
            
            lnode = 0
            rnode = 0
            
            if not node or (not node.left and not node.right):
                return 1
                
            if node.left:
                lnode = node.left.data
            if node.right:
                rnode = node.right.data
                
            if (node.data == lnode + rnode) and summ(node.left) and summ(node.right):
                return 1
            else:
                return 0
        
        return summ(root) 