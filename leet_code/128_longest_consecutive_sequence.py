# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#

class LongestConsecutiveSequence:
    def solution1(self, nums):
        if not nums:
            return -1
        length = len(nums)
        if length < 2:
            return length
        nums.sort()
        count = 1
        max = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
                if(max < count):
                    max = count
            else:
                count = 1
        return max

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 2, 5, 9, 20, 21, 22, 23]
    result = LongestConsecutiveSequence().solution1(nums)
    print result