class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        max_count = 0
        result = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1
            if count[s[right]] > max_count:
                max_count = count[s[right]]

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            current_window_length = right - left + 1
            if current_window_length > result:
                result = current_window_length

        return result
