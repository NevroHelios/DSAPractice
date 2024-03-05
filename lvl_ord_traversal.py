# Node Class:
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to build a sample binary tree
def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res  

        # lis = []
        # if not root:
        #     return []
        # def bfs(root, l):
        #     if len(lis) == l:
        #         lis.append([])
        #     lis[l].append(root.data)
        #     if root.left:
        #         bfs(root.left, l + 1)
        #     if root.right:
        #         bfs(root.right, l + 1)
        # bfs(root, 0)
        # return [i for j in lis for i in j]
    

# Example case
tree_root = build_tree()
solution = Solution()
level_order_traversal = solution.levelOrder(tree_root)
print(level_order_traversal)