# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

import math

class SpiralMatrix:
    def solution1(self, nums):
        if not nums:
            return []
        result = []

        row = 0
        rows = len(nums)
        columns = len(nums[0])

        while row <= math.floor(rows / 2):

            # top
            for index in range(row, columns - row):
                result.append(nums[row][index])

            # right
            for index in range(row + 1, rows - 1 - row):
                result.append(nums[index][columns - 1 - row])

            # bottom
            for index in range(columns - 1 - row, row - 1, -1):
                if rows - 1 - row == row:
                    break
                result.append(nums[rows - 1 - row][index])

            # left
            for index in range(rows - 2 - row, row, -1):
                result.append(nums[index][row])
            row += 1

        return result

if __name__ == '__main__':
    nums = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    result = SpiralMatrix().solution1(nums)
    print result
