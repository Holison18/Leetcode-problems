class Solution(object):
    def number_of_set_bit(self, digit):
        binary = bin(digit).replace("0b","")
        print(binary)

mySoln = Solution()
mySoln.number_of_set_bit(25)