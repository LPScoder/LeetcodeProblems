class Solution(object):
    def productExceptSelf(self, nums):
        
        front = 1;
        final = [1] * len(nums)
        
        for i in range(len(nums)):
            final[i] = front
            front *= nums[i]
        
        back = 1
        
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= back
            back *= nums[i]
        
        return final