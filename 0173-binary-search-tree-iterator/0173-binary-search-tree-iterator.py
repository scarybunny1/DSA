# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.res = []
        self.inorder(root)

    def next(self) -> int:
        self.index += 1
        return self.res[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.res) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()