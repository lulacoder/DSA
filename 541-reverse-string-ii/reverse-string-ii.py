class Solution:
    def reverseStr(self, s, k):
        # Convert string to list because strings are immutable in Python
        s_list = list(s)
        n = len(s_list)
        
        # Step by 2*k to process every 2k block
        for i in range(0, n, 2 * k):
            # Reverse the first k characters in the current block
            # The slice handling automatically manages the "fewer than k" case
            s_list[i : i + k] = reversed(s_list[i : i + k])
            
        return "".join(s_list)
