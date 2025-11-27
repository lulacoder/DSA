class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(arr1)
        result = []
        
        # Place elements in arr2 order
        for val in arr2:
            result.extend([val] * count[val])
            del count[val]
        
        # Place remaining elements sorted
        leftovers = []
        for val in sorted(count.keys()):
            result.extend([val] * count[val])
        
        return result

        
        
        
        