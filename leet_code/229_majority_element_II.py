# coding: utf-8
# Given an integer array of size n,
# find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.
# 第一想法是用map, 键是数, 值是次数, 遍历一次就可以完成. 但是对于空间来说是不合格的
# 第二想法是排序, 排序完毕后再遍历一次即可
# 一个想法: n / 3代表了最多两个.

class MajorityElementII(object):
    def solution1(self, nums):
        size = len(nums)
        result = []

        if size == 0:
            return []
        elif size == 1:
            return [nums[0]]
        elif size == 2:
            return [nums[0], nums[1]]

        first = nums[0]
        fCount = 1
        second = nums[1]
        sCount = 1

        for i in range(2, size):
            if nums[i] == first:
                fCount += 1
            elif nums[i] == second:
                sCount += 1
            elif fCount == 0:
                first = nums[i]
                fCount = 1
            elif second == nums[i]:
                second = nums[i]
                sCount = 1
            else:
                fCount -= 1
                sCount -= 1

        fCount = 0
        sCount = 0
        for i in range(0, size):
            if nums[i] == first:
                fCount += 1
            elif nums[i] == second:
                sCount += 1
        if fCount > size / 3:
            result.append(first)
        if sCount > size / 3:
            result.append(second)

if __name__ == '__main__':
    pass