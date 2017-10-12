# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.

class SortColors:

    def solution1(self, nums):
        result = []
        if not nums:
            return result
        lo, hi, index = 0, len(nums) - 1, 1
        while index <= hi:
            if nums[index] == 0:
                nums[index] ^= nums[lo]
                nums[lo] ^= nums[index]
                nums[index] ^= nums[lo]
                index += 1
                lo += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index] ^= nums[hi]
                nums[hi] ^= nums[index]
                nums[index] ^= nums[hi]
                hi -= 1

if __name__ == '__main__':
    nums = [0, 1, 2, 1, 0, 2, 1, 0, 2, 1, 0, 0, 1]
    SortColors().solution1(nums)
    print nums

