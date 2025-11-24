class Solution:
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            # Extract the last bit
            bit = n & 1
            # Shift result left and add the bit
            result = (result << 1) | bit
            # Shift n right to process next bit
            n >>= 1
        return result
