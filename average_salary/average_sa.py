class Solution:
    def average(self,salary) -> float:
        sum = 0
        maximum = max(salary)
        minimum = min(salary)
        for i in range(len(salary)):
            if salary[i] != maximum and salary[i] != minimum:
                sum += salary[i]
        return sum/(len(salary)-2)
    
    

mysoln = Solution()
print(mysoln.average([4000,3000,1000,2000]))
print(mysoln.average([1000,2000,3000]))
print(mysoln.average([6000,5000,4000,3000,2000,1000]))