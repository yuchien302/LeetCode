class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        resultsSet = set()
        nums.sort()
    
        for i in range(0, len(nums)-2):
            num = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                sum3 = num + nums[l] + nums[r]

                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    if (num, nums[l], nums[r]) not in resultsSet:
                        results.append([num, nums[l], nums[r]])
                        resultsSet.add((num, nums[l], nums[r]))
                    l += 1
        return results
