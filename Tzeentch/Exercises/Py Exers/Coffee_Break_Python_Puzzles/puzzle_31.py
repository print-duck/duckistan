#############################
## id 36
## Puzzle Elo 1407
## Correctly solved 65 %
#############################


def maximum_profit(prices):
    '''Maximum profit of a single buying low and selling high'''

    profit = 0
    for i, buy_price in enumerate(prices):
        sell_price = max(prices[i:])
        profit = max(profit, sell_price - buy_price)
    return profit

# Ethereum daily prices in Dec 2017 ($)
eth_prices = [455, 460, 465, 451, 414, 415, 441]
print(maximum_profit(prices=eth_prices))
