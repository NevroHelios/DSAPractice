#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        def h(root):
            # return max(h(root.left), h(root.right)) + 1  # one line implementation    
            if not root:
                return 0
            else:
                lh = h(root.left)
                rh = h(root.right)
                return max(lh, rh) + 1
        return h(root)