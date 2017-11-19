# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

import sys

class BestTimeToBuyAndSell(object):
    def solution1(self, nums):
        if not nums:
            return 0
        min = nums[0]
        minIndex = 0
        for index in range(0, len(nums)):
            if nums[index] < min:
                min = nums[index]
                minIndex = index
        max = 0
        for index in range(minIndex, len(nums)):
            if max < nums[index]:
                max = nums[index]

        if max > min:
            return max - min
        return 0

    def solution2(self, nums):
        if not nums:
            return 0
        min = nums[0]
        max = 0
        for item in nums:
            if item < min:
                min = item
                max = 0
            elif item == min:
                continue
            elif item > min and max < item:
                max = item
        return max if max == 0 else max - min

if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]
    # nums = [7, 6, 4, 3, 1]
    result = BestTimeToBuyAndSell().solution2(nums)
    print result
