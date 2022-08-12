#12th August, 2022
#Ayush S Bhatt

#235. Lowest Common Ancestor of a Binary Search Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if (p.val == node.val or q.val == node.val) or (p.val < node.val < q.val) or (q.val < node.val < p.val):
                return node
            return lca(node.left) if p.val < node.val else lca(node.right)

        return lca(root)


if __name__ == "__main__":
    root = TreeNode(5)
    p = root.left = TreeNode(2)
    q = root.right = TreeNode(8)
    
    lca = Solution().lowestCommonAncestor(root, p, q)
    print(lca.val)