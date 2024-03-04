#User function Template for python3


'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    # code here
    res = []
    if root:
        res += postOrder(root.left)
        res += postOrder(root.right)
        res.append(root.data)
    return res    

