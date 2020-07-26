

STOCKS_BY_INDUSTRY = dict(basic_materials_sector=[["asix", "advansix inc"], ["aem", "agnico eagle mines limited"],
                                                  ["apd", "air products and chemicals, inc"]])

GROWTH_SEARCH_MARGIN = 4


def find_price(stock_abbr):
    """returns most recent price of given stock"""
    pass


def find_price(stock_abbr, date):
    """returns most recent price of given stock by given date"""
    pass


def find_earnings(stock_abbr):
    """returns latest earnings per share of given stock"""
    pass


def find_earnings(stock_abbr, date):
    """returns most recent earnings per share of given stock by given date"""
    return 7.80


def find_earnings_list(stock_abbr, start_date, end_date):
    """returns list of earnings from given date to present"""
    return [1.80, 2.65, 5.43, 2.67, 7.80]


def _linear_average_growth(stock_abbr, start_date, end_date):
    """returns linear average growth (slope of line from starting earnings/share to current earnings/share"""

    average_growth = (find_earnings(stock_abbr, end_date) - find_earnings(stock_abbr, start_date)) / \
                     (end_date - start_date)

    return average_growth


def _percent_average_growth(stock_abbr, start_date, end_date):
    """returns the average growth in percent per day"""

    earnings_list = find_earnings_list(stock_abbr, start_date, end_date)
    average_growth = 0

    for x in range(1, len(earnings_list)):
        average_growth += (earnings_list(x - 1) - earnings_list(x)) / earnings_list(x - 1)

    # num of growths is 1 less than number of earnings data points, bc growth is between points
    average_growth / (len(earnings_list) - 1)

    return average_growth


def compare_pe(stock_abbr, industry, start_date, end_date, average_growth_type):
    """
        returns difference between multiple points of given stock and average for stocks in same industry with similar growth
    """

    average_growth = 0

    if average_growth == "LINEAR":
        average_growth = _linear_average_growth()
    elif average_growth == "PERCENT":
        average_growth = _percent_average_growth()
    else:
        print("ERROR: specified average growth type not supported")
        return 0

    stock_average_growth = average_growth(stock_abbr, start_date, end_date)

    stock_price_earnings_ratio = find_price(stock_abbr) / find_earnings(stock_abbr)

    industry_average_price_earnings_ratio = 0

    matching_stocks_count = 0

    for industry_stock in STOCKS_BY_INDUSTRY[industry]:
        if abs(stock_average_growth - average_growth(industry_stock, start_date, end_date)) <= GROWTH_SEARCH_MARGIN:
            industry_average_price_earnings_ratio += find_price(stock_abbr) / find_earnings(stock_abbr)
            matching_stocks_count += 1
    industry_average_price_earnings_ratio /= matching_stocks_count

    return stock_price_earnings_ratio - industry_average_price_earnings_ratio

