# -*- coding: UTF-8 -*-
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.


import sys

class IncreasingTripletSubsequence(object):
    def solution1(self, nums):
        size = len(nums)
        if size < 3:
            return False

        first = sys.maxint
        second = sys.maxint
        for num in nums:
            if num < first:
                first = num
            elif num < second:
                second = num
            else:
                return True
        return False