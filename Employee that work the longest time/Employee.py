class Solution(object):
    def longestWorkingEmployee(self, n, logs):
        best_time = best_id = start_time = 0
        for emp_id,emp_time in logs:
            time_taken = emp_time - start_time
            if (time_taken > best_time) or (time_taken == best_time and emp_id < best_id):
                best_id = emp_id
                best_time = time_taken
            start_time = emp_time
        return best_id
    
mySoln = Solution()
print(mySoln.longestWorkingEmployee(10,[[0,3],[2,5],[0,9],[1,15]]))
print(mySoln.longestWorkingEmployee(26,[[1,1],[3,7],[2,12],[7,17]]))
print(mySoln.longestWorkingEmployee(26,[[0,10],[1,20]]))
print(mySoln.longestWorkingEmployee(70,[[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))
