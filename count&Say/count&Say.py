class Solution:
    def countAndSay(self, n: int) -> str:
        # convert the number to string
        if n == 1:
            return "1"
        else:
            number_str = str(n)

            digit_count = {}

            # store the values and their counts in the digit_count dictionary
            for digit in number_str:
                if digit in digit_count:
                    digit_count[digit] += 1
                else:
                    digit_count[digit] = 1

            newDigit = ""
            # now concatenate the digit and it's count
            for digit,count in digit_count.items():
                newDigit += str(count) + str(digit)
            return newDigit


mySoln = Solution()
print(mySoln.countAndSay(1))  # 1
print(mySoln.countAndSay(2))  # 11
print(mySoln.countAndSay(333221))  # 331221