"""
26.删除排序数组中的重复项
"""

"""
思路：最大值 + 1 代替所有重复值
最后删除 最大值 + 1 之后的数值
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.reverse()
        x = nums[0]
        d = x
        for i in range(1, len(nums)):
            if nums[i] == x:
                nums[i] = d + 1
            else:
                x = nums[i]
        nums.sort()
        if (d + 1) in nums:
            return len(nums[:nums.index(d + 1)])
        else:
            return len(nums)
