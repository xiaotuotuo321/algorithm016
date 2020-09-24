# -*- coding: utf-8 -*-

"""
二叉树的最近公共祖先

解体思路：
如果root两边各有一个p或q，那么答案应该直接是根节点root
如果都在左，则答案是left;
如果都在右,则答案是right
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if root.val == q.val or root.val == p.val: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: return root
        if l: return l
        if r: return r
