# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
#
class Solution(object):

    def firstMissionPositive(self, nums):
        """
        
        :param nums: 
        :return: 
        """
        length = len(nums)
        if(length == 0):
            return 1;

        min = nums[0];

        total = 0;
        for num in nums:
            total += num;
            if(min > num):
                min = num;
        sum = min * length  + length * (length - 1) / 2;
        if(sum - total > 0):
            return sum - total;
        else:
            if(min - 1 <= 0):
                return min + length;
            else:
                return min - 1;

