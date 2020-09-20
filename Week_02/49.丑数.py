"""
丑数
关键是如何定义下一个丑数
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        list1 = [1]
        i = 0
        j = 0
        k = 0
        temp = 0
        for l in range(n - 1):

            temp = min(list1[i] * 2, list1[j] * 3, list1[k] * 5)
            list1.append(temp)
            # print(list1)
            if temp == list1[i] * 2:
                i += 1
            if temp == list1[j] * 3:
                j += 1
            if temp == list1[k] * 5:
                k += 1
        return list1[-1]
