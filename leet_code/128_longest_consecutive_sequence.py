# -*- coding: UTF-8 -*-
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#

class LongestConsecutiveSequence:
    def solution1(self, nums):
        if not nums:
            return -1
        length = len(nums)
        if length < 2:
            return length
        nums.sort()
        count = 1
        max = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
                if max < count:
                    max = count
            else:
                count = 1
        return max

    def solution2(self, nums):
        if not nums:
            return -1
        map = {}
        res = 1
        for n in nums:
            if n in map:
                continue
            left = map[n - 1] if n - 1 in map else 0
            right = map[n + 1] if n + 1 in map else 0
            sum = left + right + 1
            map[n] = sum

            res = max(sum, res)

            map[n - left] = sum
            map[n + right] = sum
        return res

    def solution3(self, nums):
        if not nums:
            return -1
        nums = set(nums)
        max = 0
        for n in nums:
            if n - 1 in nums:
                continue
            y = n + 1
            while y in nums:
                y += 1
            max = max(y - x, max)
        return max

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 2, 3, 5, 9, 20, 21, 22, 23]
    result = LongestConsecutiveSequence().solution2(nums)
    print result