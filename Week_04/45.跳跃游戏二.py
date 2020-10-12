# -*- coding: utf-8 -*-
"""
45.跳跃游戏二

贪心算法，每次找到能跳最远的位置,出现越过最后或者能到最后的情况时返回跳跃次数
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 还是贪心
        if nums.count(1) == len(nums): return len(nums) - 1

        def fun(n):
            if not n: return 0
            for k, v in enumerate(n):
                if v >= len(n) - k: return fun(n[:k]) + 1

        return fun(nums[:-1])
