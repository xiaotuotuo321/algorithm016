# -*- coding: utf-8 -*-
"""
33.搜索旋转排序数组

不仅比较单侧，要左右都比较
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找
        l, r = 0, len(nums) - 1
        # while 循环中有等于判断
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
