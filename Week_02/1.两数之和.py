"""
两数之和
更快的是用字典
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if not nums:
        #     return []
        #
        # for i in range(len(nums) - 1):
        #     if target - nums[i] in nums[i + 1:]:
        #         return [i, i + 1 + nums[i + 1:].index(target - nums[i])]
        # else:
        #     return []
        if not nums: return []

        num_dict = dict()
        for i in nums:
            if i in num_dict:
                num_dict[i] = 2
            else:
                num_dict[i] = 1
        print(num_dict)
        for i in nums:
            if target == 2 * i and num_dict[i] == 2:
                c = nums.index(i)
                return [c, c + 1 + nums[c + 1:].index(i)]
            elif (num_dict.get(target - i) == 1) and target != 2 * i:
                return [nums.index(i), nums.index(target - i)]
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 5, 5, 11]
    target = 10
    print(s.twoSum(nums, target))