"""
1.两数之和
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []

        # 第一中方法: 太慢了
        # for m in nums[:-1]:
        #     print(m)
        #     n = target - m
        #     if n in nums[nums.index(m) + 1:]:
        #         return [nums.index(m), nums.index(m) + nums[nums.index(m) + 1:].index(n) + 1]
        #     else:
        #         continue
        # else:
        #     return []

        # 第二种 借助字典
        num_dict = dict()
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            else:
                num_dict[num] = i


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3]
    target = 6
    print(s.twoSum(nums, target))


