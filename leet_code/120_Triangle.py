# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.

class Triangle:
    def solution1(self, nums):
        if not nums:
            return None
        total = 0
        for rows in nums:
            min = rows[0]
            for column in rows:
                if min > column:
                    min = column
            total += min
        return total

if __name__ == '__main__':
    nums = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    result = Triangle().solution1(nums)
    print result
