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

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.data)
                inorder(root.right)
        inorder(root)
        return res