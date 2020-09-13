"""
283.零移动问题
i 负责遍历列表
j 负责移动0
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return []

        j = 0
        for i in range(len(nums)):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
            else:
                j += 1

        return nums
