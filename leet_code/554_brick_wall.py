# There is a brick wall in front of you.
# The wall is rectangular and has several rows of bricks.
# The bricks have the same height but different width.
# You want to draw a vertical line from the top to the bottom and cross the least bricks.
#
# The brick wall is represented by a list of rows.
# Each row is a list of integers representing the width of each brick in this row from left to right.
#
# If your line go through the edge of a brick, then the brick is not considered as crossed.
# You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
#
# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks.

import sys
import collections

class brick_wall(object):
    def solution1(self, nums):
        size = len(nums)
        totalCount = 0
        for i in range(0, len(nums[0])):
            totalCount += nums[0][i]

        min = totalCount
        for i in range(0, totalCount - 1):
            cur = 0
            for j in range(0, size):
                cur += self.findIndex(nums[j], i)
            if min > cur:
                min = cur
        return min


    def findIndex(self, list, index):
        cur = 0
        for i in range(0, len(list) - 1):
            cur += list[i]
            if cur == index:
                return 0
            elif cur < index:
                continue
            else:
                return 1
        return 1

    def solution2(self, nums):
        temp = collections.Counter()
        for brick in nums:
            sum = 0
            for b in brick:
                if sum:
                    temp[sum] += 1
                sum += b

        return len(nums) - max(temp.values() or [0])


if __name__ == '__main__':
    nums = [
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]
    ]
    result = brick_wall().solution2(nums)
    print result
    pass