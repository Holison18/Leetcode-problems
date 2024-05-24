class Solution(object):
    def ConvertToBase7(self, num):
        """convert to base 7"""
        if num == 0:
            return "0"
        n = ""
        if num < 0:
            num *= -1
            n = "-"
        result = []
        while num > 0:
            result.append(str(num % 7))
            num = num // 7
        return n + ''.join(result[::-1])


mySoln = Solution()
print(mySoln.ConvertToBase7(100))
print(mySoln.ConvertToBase7(-7))


    