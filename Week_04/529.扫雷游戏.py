# -*- coding: utf-8 -*-
"""
529.扫雷游戏

dfs
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        row, col = len(board), len(board[0])

        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白块周围的
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < row and 0 <= j + y < col and board[i + x][j + y] == "M": res += 1

            return res

        def dfs(i, j):
            num = cal(i, j)
            if num > 0:
                board[i][j] = str(num)
                return
            board[i][j] = "B"
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    nxt_i, nxt_j = i + x, j + y
                    if 0 <= nxt_i < row and 0 <= nxt_j < col and board[nxt_i][nxt_j] == "E": dfs(nxt_i, nxt_j)

        dfs(i, j)

        return board
