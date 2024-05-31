class Solution(object):
    def findNumbers(self, nums: list[int]) -> int:
        """Find the maximum number of integers with even number of digits"""
        maximum_num_even = 0
        for number in nums:
            string_number = str(number)
            if len(string_number) % 2 == 0:
                maximum_num_even += 1
        return maximum_num_even

mySoln = Solution()
print(mySoln.findNumbers([12,345,2,6,7896]))
print(mySoln.findNumbers([555,901,482,1771]))