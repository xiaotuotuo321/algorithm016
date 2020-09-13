"""
66.加一
一行式
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in list(str(int(''.join([str(i) for i in digits])) + 1))]
