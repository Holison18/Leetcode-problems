class Solution(object):
    def largestOddNumber(self, num: str) -> str:
        # Traverse the string from the end to the beginning
        for i in range(len(num) - 1, -1, -1):
            # Check if the character at the current position is an odd digit
            if num[i] in '13579':
                # Return the substring from the start to the current position (inclusive)
                return num[:i + 1]
        # If no odd digit is found, return an empty string
        return ""

mySoln = Solution()
print(mySoln.largestOddNumber("52"))
print(mySoln.largestOddNumber("4206"))
print(mySoln.largestOddNumber("35427"))