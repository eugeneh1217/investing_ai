import data as data

STOCKS_BY_INDUSTRY = dict(BASIC_MATERIALS_SECTOR=[["asix", "advansix inc"], ["aem", "agnico eagle mines limited"],
                                                  ["apd", "air products and chemicals, inc"]])


def _linear_average_growth(stock_abbr, start_date, end_date):
    """returns linear average growth (slope of line from starting earnings/share to current earnings/share"""

    average_growth = (data.find_earnings(stock_abbr, end_date) - data.find_earnings(stock_abbr, start_date)) / \
                     (end_date - start_date)

    return average_growth


def _percent_average_growth(stock_abbr, start_date, end_date):
    """returns the average growth in percent per day"""

    earnings_list = data.find_earnings_list(stock_abbr, start_date, end_date)
    average_growth = 0

    for x in range(1, len(earnings_list)):
        average_growth += (earnings_list(x - 1) - earnings_list(x)) / earnings_list(x - 1)

    # num of growths is 1 less than number of earnings data points, bc growth is between points
    average_growth /= (len(earnings_list) - 1)

    return average_growth


def compare_pe(stock_abbr, industry, start_date, end_date, average_growth_type):
    """
        returns difference between multiple points of given stock and average for stocks in same industry with similar growth
    """

    average_growth = None

    if average_growth_type == "LINEAR":
        average_growth = _linear_average_growth()
    elif average_growth_type == "PERCENT":
        average_growth = _percent_average_growth()
    else:
        print("ERROR: specified average growth type not supported")
        return 0

    stock_average_growth = average_growth(stock_abbr, start_date, end_date)

    stock_price_earnings_ratio = data.find_price(stock_abbr) / data.find_earnings(stock_abbr)

    industry_average_price_earnings_ratio = 0

    industry_average_growth = 0

    for industry_stock in STOCKS_BY_INDUSTRY[industry]:
        industry_average_price_earnings_ratio += data.find_price(industry_stock[0]) / data.find_earnings(industry_stock[0])
        industry_average_growth += average_growth(industry_stock[0], start_date, end_date)

    industry_average_price_earnings_ratio /= len(STOCKS_BY_INDUSTRY[industry])

    industry_average_growth /= len(STOCKS_BY_INDUSTRY[industry]) - 1

    return (stock_price_earnings_ratio / stock_average_growth) - (industry_average_price_earnings_ratio /
                                                                  industry_average_growth)

