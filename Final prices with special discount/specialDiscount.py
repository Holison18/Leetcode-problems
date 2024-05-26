class Solution(object):
     def finalPrices(self, prices: list[int]) -> list[int]:
          """returns the final price discount list"""
          final_prices = []
          for price in prices:
               if price == prices[-1]:
                    final_prices.append(price)
               else:
                    pass
                    
