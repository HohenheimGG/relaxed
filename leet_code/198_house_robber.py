# coding: utf-8

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
# Also thanks to @ts for adding additional test cases.

# 这题的考点是动态规划。
# 动态规划一定要找递推公式！！！
# 1. 对这题来说，对每一家房子，在其前一家房子偷不偷的前提下，有两种可能的情况。
# 2. 前一家房子被偷了，它就不能再偷了。前一家房子没被偷，它可以被偷也可以选择不偷。
# 3. 可看出，每一个子问题都依赖于前一个子问题，同时每一个子问题都会产生至少一种情况（之多两种情况）。
# 4. 根据上述分析，得到递推公式：
# money[i][0] = max(money[i - 1][0], money[i - 1][1])
# 上述公式表示，不偷第 i 家房子，当前最大收益就是前一家房子的最大收益，前一家房子可能被偷了，也可能没有被偷。
# money[i][1] = money[i - 1][0] + nums[i]
# 上述公式表示，要偷第 i 家的房子，必须在不偷第 i-1 家房子的前提下，才能加上偷第 i 家获得的收益。
#


class HouseRobber(object):
    def solution1(self, nums):
        if not nums:
            return 0
        money = [0, nums[0]]
        for index in range(1, len(nums)):
            temp = money[0]
            money[0] = max(money[0], money[1])
            money[1] = temp + nums[index]
        return money[0] if money[0] > money[1] else money[1]