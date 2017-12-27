# -*- coding: utf-8 -*-
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class BestTimeToBuyAndSellII(object):
    def solution1(self, nums):
        if not nums:
            return 0
        sum = 0
        min = nums[0]
        for item in nums:
            if item > min:
                sum += (item - min)
                min = item
            elif item < min:
                min = item
        return sum


if __name__ == '__main__':
    # nums = [7, 1, 5, 3, 6, 4]
    nums = [7, 6, 4, 3, 1]
    result = BestTimeToBuyAndSellII().solution1(nums)
    print result

