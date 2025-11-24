class Solution(object):
    def reverse(self, x):
        # 32-bit signed integer limits
        INT_MIN = -2147483648   # -2^31
        INT_MAX = 2147483647    #  2^31 - 1

        # Check if the number is negative
        neg = False
        if x < 0:
            neg = True
            x = -x   # Make it positive for easier processing

        rev = 0

        # Extract digits until x becomes 0
        while x != 0:
            digit = x % 10      # Get the last digit
            x = x / 10          # Remove the last digit (Python 2 integer division)

            # Before doing rev * 10 + digit, we must check for overflow
            # If rev is already bigger than INT_MAX/10, multiplying by 10 will overflow
            # If rev == INT_MAX/10, then we can only add <= 7 (max last digit for INT_MAX)
            if rev > INT_MAX / 10 or (rev == INT_MAX / 10 and digit > 7):
                return 0        # Overflow → return 0

            # Append digit to reversed number
            rev = rev * 10 + digit

        # Add the negative sign back if original number was negative
        if neg:
            rev = -rev

        # Final safety check (not really necessary, but good practice)
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev
