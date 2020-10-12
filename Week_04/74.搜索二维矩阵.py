# -*- coding: utf-8 -*-
"""
74.搜索二维矩阵

从右上角开始
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角开始
        h = len(matrix)
        if h == 0:
            return False

        w = len(matrix[0])
        if w == 0:
            return False
        m = 0
        n = w - 1
        while m < h and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False
