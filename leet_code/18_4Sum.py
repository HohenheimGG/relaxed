#
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class FourSum:
    def solution1(self, nums, target):
        """
        
        :param nums: List[int] 
        :param target: 
        :return: 
        """

        length = len(nums)
        result = []
        if not nums or length < 4:
            print 'input error'
            return result

        nums.sort()
        max = nums[length - 1]
        if 4 * nums[0] > target or max * 4 < target:
            return result

        for index in range(0, length):
            z = nums[index]
            if index != 0 and nums[index] == nums[index - 1]:
                continue
            if z + max * 3 < target:
                continue
            if 4 * z > target:
                break
            if 4 * z == target and index + 3 < length and nums[index + 3] == z:
                result.append([z, z, z, z])
                break
            self.solution1ThreeSum(index + 1, length - 1, nums, target - z, result, z)

        return result

    def solution1ThreeSum(self, start, length, nums, target, result, z):

        if start + 1 >= length:
            return
        max = nums[length]
        if 3 * nums[start] > target or 3 * max < target:
            return

        for index in range(start, length):
            z1 = nums[index]
            if index != start and z1 == nums[index - 1]:
                continue
            if 3 * z1 < target:
                continue
            if z1 + max * 2 > target:
                break
            if 3 * z1 == target and index + 2 < length and nums[index + 2] == z1:
                result.append([z, z1, z1, z1])
                break
            self.solution1TwoSum(index, length, nums, target - z1, z, z1)

    def solution1TwoSum(self, start, length, nums, target, result, z, z1):

        if start >= length:
            return
        max = nums[length]
        if nums[start] * 2 > target or max * 2 < target:
            return
        i, j = start, length
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                result.append(z, z1, nums[i], nums[j])
                while i + 1 < j and nums[i] == nums[i + 1]:
                    i += 1
                while j - 1 > i and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif sum < target:
                i += 1
            else:
                j -= 1


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    result = FourSum().solution1(nums, 0)
    print result