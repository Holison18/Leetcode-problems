class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            reversed_value = int(str(x)[1:][::-1]) * -1
            if reversed_value not in range(-2**31, 2**31 - 1):
                return 0
            else:
                return reversed_value
        else:
            reversed_value = int(str(x)[::-1])
            if reversed_value not in range(-2**31, 2**31 - 1):
                return 0
            else:
                return reversed_value
        
mysoln = Solution()
print(mysoln.reverse(123))
print(mysoln.reverse(-123))
print(mysoln.reverse(120))
print(mysoln.reverse(0))
print(mysoln.reverse(1534236469))
print(mysoln.reverse(-2147483648))
print(mysoln.reverse(2147483647))