# -*- coding: utf-8 -*-
"""
153.寻找旋转排序数组中的最小值

二分法
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分法

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[high]
