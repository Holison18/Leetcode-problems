class Solution(object):
    def longestWorkingEmployee(self, n, logs):
        employeeNDtime = {}
        for log in logs:
            employee, time = log[0], log[1]
            if employee in employeeNDtime:
                employeeNDtime[employee] += time
            else:
                employeeNDtime[employee] = time
        print(employeeNDtime)

mySoln = Solution()
mySoln.longestWorkingEmployee(10,[[0,3],[2,5],[0,9],[1,15]])