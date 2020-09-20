"""
N叉树的前序遍历

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # if not root: return []
        # res = [root.val]
        #
        # for node in root.children:
        #     res.extend(self.preorder(node))
        #
        # return res

        if not root: return []
        res = []

        def helper(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    helper(i)

        helper(root)
        return res
