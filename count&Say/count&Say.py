class Solution:
    def countAndSay(self, n: int) -> str:
        # convert the number to string
        number_str = str(n)

        digit_count = {}

        for digit in number_str:
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
