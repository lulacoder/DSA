class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned =""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        reversed_str= cleaned[::-1]

        return cleaned == reversed_str