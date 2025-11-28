class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        root = int(num ** 0.5)
        return root * root == num
        