"""
127.单词接龙

beginWord和endWord一起走, 什么意思呢?就是说beginWord找endWord,endWord找beginWord,直接看代码也很好理解的!
"""
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 双向查找

        if endWord not in wordList:
            return 0

        wordict = set(wordList)

        s1 = {beginWord}
        s2 = {endWord}
        n = len(beginWord)
        step = 0

        wordict.remove(endWord)

        while s1 and s2:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return step + 1
                    if w not in wordict: continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
        return 0

