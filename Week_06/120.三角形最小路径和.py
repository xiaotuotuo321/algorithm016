#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 7:59 下午
# @Author  : whp
# @File    : 120.三角形最小路径和.py

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                res[j] = triangle[i][j] + min(res[j], res[j + 1])

        return res[0]
