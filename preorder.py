#gfg
#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
   
    # code here
    res = []
    if root:
        res.append(root.data)
        res += preorder(root.left)
        res += preorder(root.right)
    return res