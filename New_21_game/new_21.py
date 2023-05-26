class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (k + maxPts)  # Create a dynamic programming array
        
        for i in range(k, min(n, k + maxPts - 1) + 1):
            dp[i] = 1.0  # Initialize the probabilities for points between k and min(n, k + maxPts - 1) to 1.0
            
        dp[k - 1] = min(n - k + 1, maxPts) / maxPts  # Calculate the probability for k - 1
        
        for i in range(k - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts  # Calculate the probabilities for points from k - 2 to 0
        
        return dp[0]  # Return the probability of having 0 or fewer points



mySoln = Solution()
print(mySoln.new21Game(10, 1, 10))  # 1.0
print(mySoln.new21Game(6, 1, 10))  # 0.6
print(mySoln.new21Game(21, 17, 10))  # 0.73278



