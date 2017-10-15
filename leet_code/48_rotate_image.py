# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

import math

class RotateImage:
    def solution1(self, nums):
        if not nums:
            return []

        rows = len(nums)
        columns = len(nums[0])
        for row in range(0, int(math.floor(rows / 2))):
            for column in range(row, columns - 1):
                temp = nums[column][columns - row- 1]
                nums[column][columns - row - 1] = nums[row][column]#top | right

                temp ^= nums[rows - row - 1][columns - column - 1]
                nums[rows - row - 1][columns - column - 1] ^= temp
                temp ^= nums[rows - row - 1][columns - column - 1]

                temp ^= nums[columns - column - 1][row]
                nums[columns - column - 1][row] ^= temp
                temp ^= nums[columns - column - 1][row]

                temp ^= nums[row][column]
                nums[row][column] ^= temp
                temp ^= nums[row][column]

if __name__ == '__main__':
    nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    RotateImage().solution1(nums)
    print nums