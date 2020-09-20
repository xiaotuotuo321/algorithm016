"""
N叉树的层序遍历
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        ret = []
        while level:
            ret.append([node.val for node in level])
            level = [child for node in level for child in node.children]
        return ret
