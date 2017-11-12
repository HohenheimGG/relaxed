# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.

import math

class ValidSudoku(object):
    def solution1(self, nums):
        if not nums:
            return False
        rowNum = len(nums)
        for rowIndex in rowNum:
            for columnIndex in len(nums[rowIndex]):
                target = nums[rowIndex][columnIndex]
                if target == '.':
                    continue
                #横向比较
                columnNum = len(nums[rowIndex])
                for index in columnNum:
                    if index != columnIndex and nums[rowIndex][index] == target:
                        return False

                #竖向比较
                for index in rowNum:
                    if index != rowIndex and nums[index][columnIndex] == target:
                        return False

                #九格
                start, end = 0, 0
                if 0 <= rowIndex <= 2:
                    start = 0
                elif 3 <= rowIndex <= 5:
                    start = 3
                elif 6 <= rowIndex <= 8:
                    start = 6

                if 0<= columnIndex <= 2:
                    end = 0
                elif 3 <= columnIndex <= 5:
                    end = 3
                elif 6 <= columnIndex <= 8:
                    end = 6

                for i in range(start, start + 3):
                    for j in range(end, end + 3):
                        if i != rowIndex and j != columnIndex and nums[i][j] == target:
                            return False
        return True

    def solution2(self, nums):
        if not nums:
            return False
        rowSize = len(nums)
        temp = set()
        for rowIndex in rowSize:
            for columnIndex in len(nums[rowIndex]):
                s = '(' + nums[rowIndex][columnIndex] + ')'
                if s + rowIndex in temp \
                        or columnIndex + s in temp \
                        or math.floor(rowIndex / 3) + s + math.floor(columnIndex / 3) in  temp:
                    return False
                set.add(s + rowIndex)
                set.add(columnIndex + s)
                set.add(math.floor(rowIndex / 3) + s + math.floor(columnIndex / 3))
        return True



if __name__ == '__main__':
    pass