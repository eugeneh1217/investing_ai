import src.data
from src.comp_pe import compare_pe
from src.stock_market_env import StockMarketEnv
from src.csv_parse import SECTOR_DICT


strategies = []

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

N = 5

# runs tests for periods of 1 year, 2 years... n years from most recent data
# currently tests with investing daily
# for testing_periods in range(1, N + 1):
#     for month in range(12):
#         for day in range()


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
