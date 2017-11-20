# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

import math


class CoinChange(object):

    def solution1(self, nums, amount):
        if not nums:
            return -1
        nums.sort()
        # dic = {}
        # for item in nums:
        #     dic[item] = item

        return self.circle(nums, amount, -1)

    def circle(self, nums, reminder, start):
        if start < -(len(nums)):
            return -1
        for index in range(len(nums) + start, -1, -1):
            item = nums[index]
            if reminder < start:
                return -1

            re = reminder % item
            times = math.floor(reminder / item)
            if re == 0:
                return reminder / item
            next = self.circle(nums, re, start - 1)
            if next == -1:
                return -1
            else:
                return times + next

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    result = CoinChange().solution1(nums, 11)
    print result
