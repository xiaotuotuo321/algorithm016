"""
二叉树的中序遍历

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        queue = []

        def helper(root):
            if root == None:
                return

            helper(root.left)
            queue.append(root.val)
            helper(root.right)

        helper(root)
        return queue
