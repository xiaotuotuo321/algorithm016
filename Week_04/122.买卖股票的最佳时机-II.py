# -*- coding: utf-8 -*-
"""
122.买卖股票的最佳时机-II

思路: 只要第二天的股价大于第一天的股价 就进行一次买入卖出
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        total = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total += prices[i + 1] - prices[i]

        return total
