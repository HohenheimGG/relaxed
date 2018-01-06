# 219. Contains Duplicate II
#
# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

class ContainsDuplicateII(object):

    def solution1(self, nums, k):
        for index in range(0, len(nums)):
            element = nums[index]
            for j in range(index + 1, max(len(nums), index + k)):
                if element == nums[j]:
                    return True
        return False

    def solution2(self, nums, k):
        temp = {}
        for index, element in enumerate(nums):
            if element in temp and index - nums[element] <= k:
                return True
            temp[element] = index


if __name__ == '__main__':
    pass