class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
    
        for i in range(len(nums)):
            num = target - nums[i]
            if num in dic.keys():
                return [i, dic[num]]
            dic[nums[i]] = i