
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class ThreeSum:
    def solution1(self, nums):
        """
        
        :type nums: List[int] 
        :return: 
        """
        if(not nums or len(nums) < 3):
            print "input error"
            return
        result = []
        filter = set()
        length = len(nums)
        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if(nums[i] + nums[j] + nums[k] == 0 and str(nums[i]) + str(nums[j]) + str(nums[k]) not in filter):
                        result.append([nums[i], nums[j], nums[k]])
                        filter.add(str(nums[i]) + str(nums[j]) + str(nums[k]))
                        filter.add(str(nums[i]) + str(nums[k]) + str(nums[j]))
                        filter.add(str(nums[j]) + str(nums[i]) + str(nums[k]))
                        filter.add(str(nums[j]) + str(nums[k]) + str(nums[i]))
                        filter.add(str(nums[k]) + str(nums[i]) + str(nums[j]))
                        filter.add(str(nums[k]) + str(nums[j]) + str(nums[i]))
                    else:
                        continue

        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = ThreeSum().solution1(nums)
    print result

