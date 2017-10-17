# coding: utf-8
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
# excluding [11,22,33,44,55,66,77,88,99])
#
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.
#

class CountNumbers:
    def solution1(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        if n == 1:
            return 10
        total, val = 10, 9
        available = 9
        for num in range(2, n + 1):
            if available < 0:
                break
            val *= (9 - num + 2)
            total += val
            available -= 1
        return total


if __name__ == '__main__':
    result = CountNumbers().solution1(12)
    print result
