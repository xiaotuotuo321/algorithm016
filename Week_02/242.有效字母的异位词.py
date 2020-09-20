"""
有效字母的异位词
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 第一种：字符串排序
        # if s and not t:
        #     return False
        # if not t and s:
        #     return False

        # def sort_str(x: str):
        #     x_list = list(x)
        #     x_num_list = [ord(i) for i in x_list]
        #     x_num_list.sort()

        #     return "".join([chr(j) for j in x_num_list])

        # return sort_str(s) == sort_str(t)

        # 第二种： 直接sort()
        # return sorted(s) == sorted(t)

        # 第三种: 使用set()减少循环规模，如果发现count(i)的值相等的话: 提前终止
        result = True
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                result = result and (s.count(i) == t.count(i))
                if result == False:
                    return result
        else:
            result = False

        return result
