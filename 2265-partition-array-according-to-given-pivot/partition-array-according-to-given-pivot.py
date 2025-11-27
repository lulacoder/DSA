class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result =[]
        greater =[num for num in nums if num > pivot]
        less = [num for num in nums if num < pivot]
        pivot1= [num for num in nums if num == pivot ]

        result.extend(less)
        result.extend(pivot1)
        result.extend(greater)
        
        return result