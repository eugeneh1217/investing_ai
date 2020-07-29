class StockMarketEnv:
    """simple environment to simulate the stock market to test different strategies"""

    def __init__(self, principle):
        self.buying_power = principle
        self.networth = 0
        # list of tuples of format (symbol, shares)
        self.owned_stocks = []
        self.elapsed_time = 0
        # list of lists of format:
        # [[networth_over_time], [dict(buy=[(symbol, shares)], sell=[(symbol, shares)])]]
        self.history = [[], []]

    def buy(self, symbol, shares):
        """buy given number of shares of given stock"""

        self.buying_power -= find_price(symbol) * shares

        # if not enough buying_power
        if self.buying_power < 0:
            return symbol, 0

        # if some shares of stock are already owned
        for stock in self.owned_stocks:
            if stock[0] == symbol:
                stock[1] += shares
                return symbol, shares

        # if no shares of stock are owned
        self.owned_stocks.append((symbol, shares))

        return symbol, shares

    def sell(self, symbol, shares):
        """sell given number of shares of given stock"""

        stock_index = -1

        # find index within owned_stocks
        for x in range(len(self.owned_stocks)):
            if self.owned_stocks[x][0] == symbol:
                stock_index = x

        # could not find stock within owned_stocks
        if stock_index == -1:
            return symbol, 0

        # check if enough shares are owned
        if self.owned_stocks[stock_index][1] < shares:
            self.owned_stocks[stock_index][1] = 0
            return symbol, 0

        # sell stock normally
        self.owned_stocks[stock_index][1] -= shares
        return symbol, shares

    def step(self, buy_list, sell_list):
        """
            Steps environment forward one time step
            Makes transactions in buy and sell list (lists of tuples of format (symbol, shares))
        """

        self.elapsed_time += 1

        # buy and sell given orders and record in self.history
        self.history[0].append(0)
        self.history[1].append(dict(buy=[], sell=[]))

        for buy_order in buy_list:
            order_symbol, order_shares = self.buy(buy_order[0], buy_order[1])
            self.history[1][len[self.history[1]] - 1]["buy"].append((order_symbol, order_shares))

        for sell_order in sell_list:
            order_symbol, order_shares = self.sell(sell_order[0], sell_order[1])
            self.history[1][len[self.history[1]] - 1]["sell"].append((order_symbol, order_shares))

        # recalculate networth
        self.networth = self.buying_power
        for stock in self.owned_stocks:
            self.networth += stock[1] * find_price(stock[0])

        # record networth
        self.history[0][len[self.history[1]] - 1] = self.networth

        return self.history[0][len[self.history[1]] - 1], self.history[1][len[self.history[1]] - 1]
