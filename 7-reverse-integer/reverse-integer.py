class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            s = str(x)
        else:
            s = str(x * -1) + "-"
        otp = int(s[::-1])
        if otp < -2147483648 or otp > 2147483647:
            return 0
        return otp