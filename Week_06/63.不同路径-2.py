#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 7:34 下午
# @Author  : whp
# @File    : 63.不同路径-2.py

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        height, width = len(obstacleGrid), len(obstacleGrid[0])

        for m in range(height):
            for n in range(width):
                # 如果这一格有值，则将值赋为0
                if obstacleGrid[m][n]:
                    obstacleGrid[m][n] = 0
                else:
                    if m == n == 0:
                        obstacleGrid[m][n] = 1
                    else:
                        a = obstacleGrid[m - 1][n] if m != 0 else 0  # 上方的格子
                        b = obstacleGrid[m][n - 1] if n != 0 else 0  # 左面的格子
                        obstacleGrid[m][n] = a + b

        return obstacleGrid[m][n]



