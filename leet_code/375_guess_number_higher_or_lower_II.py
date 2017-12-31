# -*- coding: utf-8 -*-

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I’ll tell you whether the number I picked is higher or lower.
# However, when you guess a particular number x, and you guess wrong, you pay $x.
# You win the game when you guess the number I picked.
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it’s higher. You pay $5.
# Second round: You guess 7, I tell you that it’s higher. You pay $7.
# Third round:  You guess 9, I tell you that it’s lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
# Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

import sys
import math

class GuessNumberHigherOrLowerII(object):
    def solution1(self, n):
        ans = [] * (n + 1)



    def DP(self, ans, start, end):
        if start > end:
            return 0
        if ans[start][end]:
            return ans[start][end]
        ans[start][end] = sys.minint

        # 现在要从[from, to] 中猜数字
        # 假设先猜i，i可以是[from, to] 中的任何数字，遍历之
        for i in range(start, end + 1):
            # left为从[from, i - 1] 猜对数字至少需要花费的money
             left = self.DP(start, i - 1)
            # right为从[i + 1, end] 猜对数字至少需要花费的money
             right = self.DP(i + 1, end)

             temp = math.max(left, right)
             ans[start][end] = math.min(temp, ans[start][end])
        return ans[start][end]