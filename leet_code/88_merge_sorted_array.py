# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution(object):
    def mergeSortArray(self, nums1, m, nums2, n):
        """
        
        :param nums1: 
        :param m: 
        :param nums2: 
        :param n: 
        :return: 
        """
        if(m == 0 and n == 0):
            return [];
        i = m - 1;
        j = n - 1;
        while True:
            sum = i + j + 1;
            if(i < 0 and j < 0):
                break;
            elif(i < 0):
                nums1[sum] = nums2[j];
                j -= 1;
            elif(j < 0):
                nums1[sum] = nums1[i];
                i -= 1;
            elif(nums1[i] < nums2[j]):
                nums1[sum] = nums2[j];
                j -= 1;
            elif(nums1[i] > nums2[j]):
                nums1[sum] = nums1[i];
                i -= 1;
            elif(nums1[i] == nums2[j]):
                nums1[sum] = nums1[i];
                nums1[sum - 1] = nums1[j];
                i -= 1;
                j -= 1;

        return nums1;
