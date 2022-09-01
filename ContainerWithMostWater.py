class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0
        while right != left:
            maxArea = max(maxArea, (right - left) * min(height[right], height[left]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return maxArea
        """
        :type height: List[int]
        :rtype: int
        """