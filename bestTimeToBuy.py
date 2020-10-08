

# def maxProfit(prices): 
#     if all(prices) >= prices[0]:
#         return 0

#     profit = 0 
#     count = 1
#     for i in range(len(prices)-1):
#         for j in range(count, len(prices)):
#             potential_profit = prices[j] - prices[i]
#             if potential_profit > profit:
#                 profit = potential_profit
#         count += 1
#     return profit 



# majorly improve runtime... 
def maxProfit(prices):
    length = len(prices)
    if length < 2:
        return 0
    max_profit = 0 
    min_stock = prices[0]
    for price in prices: 
        min_stock = min(min_stock, price)
        max_profit = max(max_profit, (price - min_stock))
    return max_profit

print(maxProfit([7,1,5,3,6,4]))

print(maxProfit([7,6,4,3,1]))

print(maxProfit([[7]]))

