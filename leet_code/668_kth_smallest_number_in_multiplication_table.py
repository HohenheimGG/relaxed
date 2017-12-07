# Nearly every one have used the Multiplication Table.
# But could you find out the k-th smallest number quickly from the multiplication table?
#
# Given the height m and the length n of a m * n Multiplication Table,
# and a positive integer k, you need to return the k-th smallest number in this table.
#
# Example 1:
# Input: m = 3, n = 3, k = 5
# Output:
# Explanation:
# The Multiplication Table:
# 1 2 3
# 2 4 6
# 3 6 9
#
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# Example 2:
# Input: m = 2, n = 3, k = 6
# Output:
# Explanation:
# The Multiplication Table:
# 1 2 3
# 2 4 6
#
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# Note:
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]

import math


class Solution(object):

    def KthSmallestNumber(self, n, m, k):

        lo, hi = 1, k
        while lo <= hi:
            mid = (lo + hi) / 2
            size = self.recursive(n, m, mid)
            if size >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def recursive(self, n, m, k):
        cur = 0
        size = 0
        while cur < n:
            # k 小于当前列表第一个数
            if k < cur:
                break
            size += min(m, math.floor(k / n))
            cur += 1
        return size


if __name__ == '__main__':
    pass
