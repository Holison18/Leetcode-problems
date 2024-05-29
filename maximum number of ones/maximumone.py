class Solution(object):
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """Find maximum consecutive ones"""
        max_consecutive = [] 
        count = 0
        for number in nums:
            if number == 1:
                count += 1
            max_consecutive.append(count)
            if number != 1:
                count = 0
                continue
        return max(max_consecutive)

mySoln = Solution()
print(mySoln.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(mySoln.findMaxConsecutiveOnes([1,0,1,1,0,1]))
