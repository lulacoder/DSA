class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        
        # 'xrange' is used in Python 2 for memory efficient iteration (returns generator)
        for i in xrange(n):
            # Fill smaller elements from the start
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
                
            # Fill larger elements from the end (reverse iteration)
            if nums[n - 1 - i] > pivot:
                ans[right] = nums[n - 1 - i]
                right -= 1
        
        # Fill the remaining middle gap with the pivot value
        while left <= right:
            ans[left] = pivot
            left += 1
            
        return ans
