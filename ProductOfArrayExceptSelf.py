class Solution(object):
    def productExceptSelf(self, nums):
        
        front = 1; #tracker from front
        final = [1] * len(nums) #set length
        #idea: orginal: [1,2,3,4] front: [1,1,2,6] back: [24,12,4,1]
        for i in range(len(nums)): #i moves through range
            final[i] = front #product lst from from... lagging 1 behind
            front *= nums[i]
        
        back = 1 # same idea but from back
                
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= back
            back *= nums[i]
        
        return final