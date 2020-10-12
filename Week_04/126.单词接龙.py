# -*- coding: utf-8 -*-
"""
126.单词接龙

最短路径问题 BFS
"""
from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 最短路径 BFS
        wordList = set(wordList)
        dic = collections.defaultdict(list)

        n = len(beginWord)

        for w in wordList:
            for i in range(n):
                dic[w[:i] + "*" + w[i + 1:]].append(w)
        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen, res = set(), []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + "*" + w[i + 1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: return res
            q, s = s, q

        return []
