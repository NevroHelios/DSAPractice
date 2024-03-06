#gfg
#Your task is to complete this function

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here
        while node:
            if node.data == x:
                return 1
            
            elif x > node.data:
                node = node.right
            elif x < node.data:
                node = node.left
        return 0