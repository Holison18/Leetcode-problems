class Solution(object):
    def finalPrices(self, prices: list[int]) -> list[int]:
        """returns the final price discount list"""
        final_prices = []
        for price in prices:
            if price == prices[-1]:
                final_prices.append(price)
            if prices[price + 1] <= prices[price + 2]:
                discount = prices[price] - prices[price + 1]
                final_prices.append(discount)
            else:
                discount = prices[price] - prices[price + 2]
                final_prices.append(discount)
        return final_prices
