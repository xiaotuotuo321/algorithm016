# -*- coding: utf-8 -*-
"""
22.有效括号
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def helper(ans, r, l):
            if r == 0 and l == 0:
                self.res.append(ans)

            if l > 0:
                helper(ans + "(", r, l - 1)
            if l < r:
                helper(ans + ")", r - 1, l)

        helper("", n, n)

        return self.res
