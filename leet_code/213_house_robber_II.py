# After robbing those houses on that street,
# the thief has found himself a new place for his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile,
# the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases


class HouseRobberII(object):
    def solution1(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # For example, 1 -> 2 -> 3 -> 1 becomes 2 -> 3 if 1 is not robbed.
        return max(self.rob(nums, 0, len(nums) - 2), self.rob(nums, 1, len(nums) - 1))

    # 0: not rob  1: rob
    def rob(self, nums, lo, hi):
        money = [0, nums[lo]]
        for index in range(lo, hi + 1):
            temp = money[0]
            money[0] = max(money[0], money[1])
            money[1] = temp + nums[index]

        return max(money[0], money[1])
