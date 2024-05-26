class Solution(object):
    def finalPrices(self, prices: list[int]) -> list[int]:
        """Returns the final price discount list"""
        final_prices = []
        n = len(prices)
        for i in range(n):
            discount = 0
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            final_prices.append(prices[i] - discount)
        return final_prices
    
mySoln = Solution()
print(mySoln.finalPrices([8,4,6,2,3]))
print(mySoln.finalPrices([1,2,3,4,5]))
print(mySoln.finalPrices([10,1,1,6]))
