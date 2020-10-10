# -*- coding: utf-8 -*-

"""
860. 柠檬水找零

把各种情况都分析清楚就ok
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change_dict = {
            5: 0,
            10: 0
        }

        for bill in bills:
            if bill == 5:
                change_dict[bill] += 1
            elif bill == 10:
                if change_dict[5] > 0:
                    change_dict[5] -= 1
                    change_dict[bill] += 1
                else:
                    return False
            else:
                if change_dict[5] > 0 and change_dict[10] > 0:
                    change_dict[5] -= 1
                    change_dict[10] -= 1
                elif change_dict[5] > 3:
                    change_dict[5] -= 3
                else:
                    return False

        return True
