class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result=[]

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr1[j])

        leftovers= [num for num in arr1 if num not in arr2]
        leftovers.sort()

        result.extend(leftovers)
        return result

        
        
        
        