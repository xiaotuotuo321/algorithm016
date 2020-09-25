# -*- coding: utf-8 -*-
"""
46.全排列
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        递归解法： 思路
        取出一个值，取剩下值的全排列再加上取出的值
        """

        if len(nums) == 1:
            return [nums]

        result = []
        for n in nums:
            sub = nums.copy()
            sub.remove(n)
            subresult = self.permute(sub)
            for subres in subresult:
                subres.insert(0, n)
                result.append(subres)

        return result
