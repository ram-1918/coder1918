"""
Trees
------
1. Build a tree from scratch, learn its behaviour
2. LCA, Depth, Symetric, right-side view, construct tree
3. Recursive and iterative(stack/queue) approach
4. preorder, in-order, postorder - DFS; level order - BFS
5. Leaf node, last level, balanced tree, complete binary tree, full binary tree
"""

class TreeNode:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

class ConstructBST:
    def __init__(self):
        self.max_diameter = 0
    
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        if root.val > value:
            root.left = self.insert(root.left, value)
        elif root.val < value:
            root.right = self.insert(root.right, value)
        return root
    
    def delete(self, root, value):
        if not root:
            return root
        # traverse until current root value becomes equal to delete node value
        if root.val > value:
            root.left = self.delete(root.left, value)
            return root
        elif root.val < value:
            root.right = self.delete(root.right, value)
            return root
        # print(root.val) # At this point, we will have the node that should be deleted
        # 2 cases
        # 1. If one child node is empty
        if not root.left:
            temp = root.right
            del root
            return temp
        elif not root.right:
            temp = root.left
            del root
            return temp
        # 2. If both child nodes exist
        else:
            parent = root
            current = root.right
            while current.left is not None: # traverse to find the leftmost node to the root.right node
                parent = current
                current = current.left

            # Here we separate the current node by assigning parent.left/parent.right as None
            if parent != root:
                parent.left = current.right
            else:
                parent.right = current.right
            
            root.val = current.val # assiging the root value with the current value(leftmost value)
            del current # delete leftmost value
            return root # return updated root
    
    # height at root node = h; 
    # height = # of edges present in the longest path connecting that node to a leaf node
    def getHeight(self, root): 
        
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1
    
    # At root node, depth = 0; depth = number of edges between root and target node
    def getDepth(self, root, k):
        if not root:
            return -1
        depth = -1
        if root.val == k:
            return depth + 1
        depth =  self.getDepth(root.left, k)
        if depth >= 0:
            return depth + 1
        depth = self.getDepth(root.right, k)
        if depth >= 0:
            return depth + 1
        return depth

    # # of nodes on the longest path between any two leaf nodes
    def getDiameter(self, root):
        if not root:
            return 0
        left = self.getDiameter(root.left)
        right = self.getDiameter(root.right)
        self.max_diameter = max(self.max_diameter, left + right + 1) # updates the diameter at each node
        return max(left, right) + 1 # but here it includes only maximum of both left or right subtree

    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        lst.append(root.val)
        self.inorder(root.right)
    
    def preorder(self, root):
        if not root:
            return 
        lst.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

'''
          50
    30          60
20     40   55      70
          52  56  67   80

'''
node_values = [30, 60, 20, 40, 55, 52, 56, 70, 80, 67]

root = TreeNode(50)
bst = ConstructBST()
for value in node_values:
    bst.insert(root, value)

# bst.inorder(root)
lst = []
bst.inorder(root)
print(f'Before: {lst}')

bst.delete(root, 60)

lst = []
bst.inorder(root)
print(f'After Deleting node 60: {lst}')

height = bst.getHeight(root)
depth = bst.getDepth(root, 80)
diameter = bst.getDiameter(root)
print(f'Height of the tree: {height}')
print(f'Depth of the tree: {depth}')
print(f'Diameter of the tree: {bst.max_diameter}')
