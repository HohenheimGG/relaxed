# -*- coding: utf-8 -*-
# Given an array of integers A and let n to be its length.
#
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise,
# we define a “rotation function” F on A as follow:
#
# F(k) = 0 * Bk[0] + 1 * Bk[1] + … + (n-1) * Bk[n-1].
#
# Calculate the maximum value of F(0), F(1), …, F(n-1).
#
# Note:
# n is guaranteed to be less than 105.
#
# Example:
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

class RotateFunction(object):
    def solution1(self, nums):
        size = len(nums)
        index = 0
        max = 0
        while size > index:
            cur = 0
            sum = 0
            for i in range(index, size):
                sum += nums[i] * cur
                cur += 1
            for j in range(0, index):
                sum += nums[j] * cur
                cur += 1
            if max < sum:
                max = sum
            index += 1
        return max

    def solution2(self, nums):
        sum = 0
        F = 0
        size = len(nums)
        for index in range(0, size):
            sum += nums[index]
            F += index * nums[index]

        maxValue = F
        for index in range(size - 1, -1, -1):
            F += sum - size * nums[index]
            maxValue = max(F, maxValue)
        return maxValue

if __name__ == '__main__':
    nums = [4, 3, 2, 6]
    result = RotateFunction().solution2(nums)
    print result
