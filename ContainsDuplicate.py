class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i, num in enumerate(nums):
            if dic.has_key(num):
                return True
            else:
                dic[num] = i
        return False