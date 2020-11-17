#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 9:00 下午
# @Author  : whp
# @File    : 152.乘积最大子数组.py
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")

        imax, imin = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            res = max(imax, res)

        return res

