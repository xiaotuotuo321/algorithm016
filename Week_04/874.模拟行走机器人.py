"""
874.模拟行走机器人

在国际站看到，还有一种找规律的方式，我觉得更好理解：

左转:-2时 dx, dy = -dy, dx
右转：-1时 dx, dy = dy, -dx
这种方式比上面的计算%4后的余数更好懂，可能只是对我而言更好理解：
最开始是面北而行，x,y方向的速度肯定是（0，1），dx,dy的初始值就为0， 1
然后画图把每个方向的速度标出来，找规律，就很容易发现了。
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx, dy, x, y = 0, 1, 0, 0
        distance = 0
        obs_dict = {}

        for obs in obstacles:
            obs_dict[tuple(obs)] = 0

        for com in commands:
            if com == -2:
                dx, dy = -dy, dx
            elif com == -1:
                dx, dy = dy, -dx
            else:
                for j in range(com):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y

                    distance = max(distance, x*x + y*y)
        return distance
