# -*- coding: utf-8 -*-
"""
70.爬楼梯
斐波那契数列
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 第一种
        # if n <= 2:
        #     return n

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # 第二种
        # res_list = {}
        # res_list[1] = 1
        # res_list[2] = 2

        # for i in range(3, n+1):
        #     res_list[i] = res_list[i - 1] + res_list[i - 2]

        # return res_list[n]

        # 第三种
        fst = 1
        scd = 2
        res = 0

        for i in range(2, n):
            res = fst + scd

            fst = scd
            scd = res

        return max(res, n)