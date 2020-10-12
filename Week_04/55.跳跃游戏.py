# -*- coding: utf-8 -*-

"""
55.跳跃游戏

贪心
如果能到达某一位置，一定能到达它前面的所有位置
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心
        if nums == [0]: return True

        maxDist = 0
        end_index = len(nums) - 1
        for i, jump in enumerate(nums):
            if maxDist >= i and i + jump > maxDist:
                maxDist = i + jump
                if maxDist >= end_index:
                    return True

        return False
