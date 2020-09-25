# -*- coding: utf-8 -*-
"""
47.全排列2
先将数组进行排序操作
nums[i] == nums[i - 1] 进行去重操作
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 将数组进行排序

        self.res = []
        self.recur(nums, [])
        return self.res

    def recur(self, nums, temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.recur(nums[:i] + nums[i + 1:], temp + [nums[i]])
