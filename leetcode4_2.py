class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2 == 0:
            return 0.5 * (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1])
        else:
            return nums3[len(nums3) // 2]
        