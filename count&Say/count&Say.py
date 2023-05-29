class Solution:
    def countAndSay(self, n: int) -> str:
        # convert the number to string
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
            newDigit += str(digit_count[digit]) + str(digit_count[count])

