# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,1,2,2,2,2,3],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

class RemoveDuplicate:
    def solution1(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length < 2:
            return length
        count = 1
        for index in range(1, length):
            if nums[index] != nums[index - 1]:
                count += 1
        return count

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 3]
    count = RemoveDuplicate().solution1(nums)
    print count