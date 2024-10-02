import sys
def buy_stock(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, (prices[j] - prices[i]))
    return max_profit
def buy_stock2(prices):
    min = sys.maxsize
    profit  = 0
    for i in prices:
        if min > i:
            min = i
        if profit < i - min:
            profit = i - min
    return profit
prices = [7,1,5,3,6,4]
print(buy_stock(prices))
print(buy_stock2(prices))
prices = [7,6,4,3,1]
print(buy_stock(prices))
print(buy_stock2(prices))
prices = [7, 10, 1, 3, 6, 9, 2]
print(buy_stock(prices))
print(buy_stock2(prices))
prices = [1, 3, 6, 9, 11]
print(buy_stock(prices))
print(buy_stock2(prices))