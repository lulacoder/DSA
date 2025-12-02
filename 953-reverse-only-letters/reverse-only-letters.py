class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert to list for mutability
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        # Two pointer approach
        while left < right:
            # Find letter from left
            while left < right and not s_list[left].isalpha():
                left += 1
            # Find letter from right
            while left < right and not s_list[right].isalpha():
                right -= 1
            # Swap the letters
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return ''.join(s_list)