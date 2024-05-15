class Solution(object):
    def find_dissapeered(self, nums):
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return result
            
    
mySoln = Solution()
print (mySoln.find_dissapeered([4,3,2,7,8,2,3,1]))
print (mySoln.find_dissapeered([1,1]))
print (mySoln.find_dissapeered([2,2]))
            

