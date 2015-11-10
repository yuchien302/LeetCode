class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.left_sum = [0]
        self.right_sum = [0]
        for n in nums:
            self.left_sum.append(n+self.left_sum[-1])
        
        for i in range(len(nums)-1, -1, -1):
            self.right_sum.append(nums[i] + self.right_sum[-1])
        
        self.sums = sum(nums)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums - self.left_sum[i] - self.right_sum[len(self.right_sum)-2-j]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)