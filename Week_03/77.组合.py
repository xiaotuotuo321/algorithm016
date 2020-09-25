# -*- coding: utf-8 -*-
"""
77.组合
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 借鉴思路
        """
        从1~n个数里选出k个数:
        1.组合中不包括n:从1~n-1个中选k个数
        2.组合中包括n:从1~n-1个数，然后在把n添加进每个组合中
        """

        if n < k or n < 1:
            return []

        if k == 0:
            return [[]]

        if n == k:
            return [[i for i in range(1, n + 1)]]

        ans1 = self.combine(n - 1, k - 1)
        ans2 = self.combine(n - 1, k)

        if ans1:
            for i in ans1:
                i.append(n)

        return ans1 + ans2


