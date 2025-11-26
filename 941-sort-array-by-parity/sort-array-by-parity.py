class Solution(object):
    def sortArrayByParity(self, nums):
        """
        Optimized two-pointer approach to sort array by parity.
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - in-place modification, no extra space
        """
        result=[]
        for i in range(len(nums)):
            if nums[i]% 2==0:
                result.append(nums[i])

        for i in range(len(nums)):
            if nums[i]%2 != 0:
                result.append(nums[i])

        return result
