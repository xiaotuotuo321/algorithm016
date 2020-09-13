"""
88.合并两个有序数组
将nums2合并到nums1中,nums1不能是一个新的对象,要在原来列表上修改
"""
from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()

        return nums1
