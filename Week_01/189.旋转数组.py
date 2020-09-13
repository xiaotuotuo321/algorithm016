"""
旋转数组 只能写出两种 剩下的参考题解
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        # 第一种 切片法
        # nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

        # 第二种 插入法
        # for i in range(k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()

        # 第三种 三次反转
        # 防止移动的k的值大于列表的长度, 需要进行取余操作
        # 将数据分为两段 [0: n-k-1] [n-k: n-1]
        # 其实这个reverse可以使用列表自带的reversed进行操作
        """
        先翻转第一段
        翻转第二段
        反转整个列表
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        x = len(nums)
        k = k % x

        reverse(0, x-k-1)
        reverse(x-k, x-1)
        reverse(0, x-1)






