class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter =0
        for i in range(len(nums)):
            if nums[i] %3 ==0:
                continue
            elif nums[i] %3 ==1:
                counter +=1
            else:
                counter +=1

        return counter
        