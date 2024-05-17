class Solution(object):
    def BuyAndSell(sell, prices):
        buying_price = prices[0]
        max_profit = 0
      
        for price in prices[1:]:
            max_profit = max(max_profit,price - buying_price)
            buying_price = min(buying_price,price)
        
        return max_profit



mySoln = Solution()
print(mySoln.BuyAndSell([7,1,5,3,6,4]))
print(mySoln.BuyAndSell([7,6,4,3,1]))