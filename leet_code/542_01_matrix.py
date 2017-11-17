# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

class Matrix(object):
    def solution1(self, nums):
        if not nums:
            return []
        rows = len(nums)
        columns = len(nums[0])
        for rowIndex in range(0, rows):
            for columnIndex in range(0, columns):
                item = nums[rowIndex][columnIndex]
                if item == 0:
                    continue
                temp = []
                temp.append([rowIndex, columnIndex])
                dis = 1
                while True:
                    tempSize = len(temp)
                    for index in range(0, tempSize):
                        coord = temp[index]
                        x = coord[0]
                        y = coord[1]
                        if x > 0:
                            if nums[x - 1][y] == 0:
                                nums[rowIndex][columnIndex] = dis
                                break
                            else:
                                temp.append([x - 1, y])

                        if x < rows - 1:
                            if nums[x + 1][y] == 0:
                                nums[rowIndex][columnIndex] = dis
                                break
                            else:
                                temp.append([x + 1, y])

                        if y > 0:
                            if nums[x][y - 1] == 0:
                                nums[rowIndex][columnIndex] = dis
                                break
                            else:
                                temp.append([x, y - 1])

                        if y < columns - 1:
                            if nums[x][y + 1] == 0:
                                nums[rowIndex][columnIndex] = dis
                                break
                            else:
                                temp.append([x, y + 1])

                        #查找不到0
                        if len(temp) == tempSize:
                            nums[rowIndex][columnIndex] = -1
                            break
                        dis += 1
                        temp = temp[tempSize:len(temp)]

        return nums

if __name__ == '__main__':
    pass