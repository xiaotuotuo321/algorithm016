"""
字母异位词分组
利用字典key的唯一性
"""


class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        return list(dic.values())
