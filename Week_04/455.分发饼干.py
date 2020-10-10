# -*- coding: utf-8 -*-
"""
455.分发饼干

思路：先将两个列表排序
然后优先满足
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g = sorted(g)
        s = sorted(s)

        con = 0
        while s:
            if not g:
                break
            if s[0] >= g[0]:
                del s[0]
                del g[0]
                con += 1
            else:
                del s[0]

        return con
