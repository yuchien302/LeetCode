class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # results = []
        resultsSet = set()
        nums.sort()
    
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1
                
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]
    
                    if sum4 > target:
                        r -= 1
                    elif sum4 < target:
                        l += 1
                    else:
                        # if (nums[i], nums[j], nums[l], nums[r]) not in resultsSet:
                            # results.append([nums[i], nums[j], nums[l], nums[r]])
                        resultsSet.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
        return list(resultsSet)