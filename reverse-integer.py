class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = int(str(abs(x))[::-1])
        if temp > 2147483647 or temp < -2147483648 :
            return 0
        if (x > 0):
            return temp
        else:
            return -temp
