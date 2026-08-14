class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        dv, dr = abs(dividend), abs(divisor)
        quotient = 0
        while dv >= dr:
            temp_dr, count = dr, 1
            while dv >= (temp_dr << 1):
                temp_dr <<= 1
                count <<= 1
            dv -= temp_dr
            quotient += count
        return -quotient if negative else quotient
