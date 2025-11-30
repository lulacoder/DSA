class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [""]*len(s)

        for i, ch in enumerate(s):
            res[indices[i]]= ch
        return "".join(res)