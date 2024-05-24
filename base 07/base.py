class Solution(object):
    def ConvertToBase7(self,num):
        """convert to base 7"""
        # declare a variable to store the result
        result = ""
        n = ""
        if num == 0:
            result = "0"
        elif num < 0:
            num *= -1
            n = "-"
        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num = num//7
        return n + result


mySoln = Solution()
print(mySoln.ConvertToBase7(100))
print(mySoln.ConvertToBase7(-7))


    