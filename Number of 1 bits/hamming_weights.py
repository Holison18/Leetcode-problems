class Solution(object):
    def number_of_set_bit(self, digit):
        # convert the decimal number into a binary number
        binary = bin(digit).replace("0b","")
        # convert binary into a string
        binstr = str(binary)
        # declare a variable count to store the number of 1 bits
        count = 0

        for value in binstr:
            if value == "1":
                count += 1
        return count


mySoln = Solution()
print(mySoln.number_of_set_bit(25))
print(mySoln.number_of_set_bit(11))
print(mySoln.number_of_set_bit(2147483645))