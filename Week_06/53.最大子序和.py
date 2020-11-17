#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 8:22 下午
# @Author  : whp
# @File    : 53.最大子序和.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return

        m = len(nums)

        dp = [0 for _ in range(m)]
        dp[0] = nums[0]
        for i in range(1, m):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)

