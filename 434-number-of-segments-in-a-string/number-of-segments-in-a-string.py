class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        num =0

        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1]== " "):
                num+=1
            
        return num

        