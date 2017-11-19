# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.

import sys

class MinimumPath(object):
    def solution1(self, nums):
        if not nums:
            return None
        rows = len(nums)
        columns = len(nums[0])
        min = sys.maxint
        queue = []
        queue.append([0, 0, nums[0][0]])
        tempSize = len(queue)
        while tempSize >= 0:
            item = queue.pop()
            x = item[0]
            y = item[1]
            sum = item[2]
            if x < rows - 1:
                xSum = sum + nums[x + 1][y]
                queue.append([x + 1, y, xSum])
            elif x == rows - 1:
                min = min(min, sum)

            if y < columns - 1:
                ySum = sum + nums[x][y + 1]
                queue.append([x, y + 1, ySum])
            elif y == columns - 1:
                min = min(min, sum)

            if len(temp) == tempSize:
                continue

            temp = temp[:len(temp)]
            tempSize = len(temp)