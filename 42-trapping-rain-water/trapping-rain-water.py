class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        total_water = 0
        
        # Pre-compute max heights to the left of each index
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        # Pre-compute max heights to the right of each index
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        # Calculate trapped water
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            total_water += water_level - height[i]
        
        return total_water