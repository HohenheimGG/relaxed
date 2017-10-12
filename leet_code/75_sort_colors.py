# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.

class SortColors:

    def solution1(self, nums):
        if not nums:
            return
        lo, hi, index = 0, len(nums) - 1, 1
        while index <= hi:
            if nums[index] == 0:
                self.exchange(nums, index, lo)
                index += 1
                lo += 1
            elif nums[index] == 1:
                index += 1
            else:
                self.exchange(nums, index, hi)
                hi -= 1

    def solution2(self, nums):
        if not nums:
            return
        lo, hi, index = 0, len(nums) - 1, 0
        while index <= hi:
            while nums[index] == 2 and index < hi:
                self.exchange(nums, index, hi)
                hi -= 1
            while nums[index] == 0 and index > lo:
                self.exchange(nums, index, lo)
                lo += 1
            index += 1

    def exchange(self, nums, i, j):
        nums[i] ^= nums[j]
        nums[j] ^= nums[i]
        nums[i] ^= nums[j]

if __name__ == '__main__':
    nums = [0, 1, 2, 1, 0, 2, 1, 0, 2, 1, 0, 0, 1]
    SortColors().solution2(nums)
    print nums

