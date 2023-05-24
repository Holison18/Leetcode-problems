class Solution:
    def average(self,salary) -> float:
        sum = 0
        for i in range(1,len(salary)-1):
            sum += salary[i]
        average = sum / len(salary)
        return average
    



mysoln = Solution()
print(mysoln.average([4000,3000,1000,2000]))
print(mysoln.average([1000,2000,3000]))
print(mysoln.average([6000,5000,4000,3000,2000,1000]))