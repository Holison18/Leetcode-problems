class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    return None      

mysoln = Solution()
My_array = [1,2,3,4,10,7,2]
target = 20
print(f"The indices of the two numbers that sum up t0 {target}:{mysoln.twoSum(My_array,target)}")

