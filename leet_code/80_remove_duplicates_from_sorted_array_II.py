# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.

class RemoveDuplicate:
    def solution1(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length < 3:
            return length
        count = 2
        for index in range(2, length):
            if nums[index] == nums[index - 1] and nums[index - 1] == nums[index - 2]:
                continue
            count += 1
        return count

    def solution2(self, nums):
        if not nums:
            return 0
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        print nums
        return i

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7, 7]
    result = RemoveDuplicate().solution2(nums)
    print result