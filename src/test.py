import src.data
from src.comp_pe import compare_pe
from src.stock_market_env import StockMarketEnv
from src.csv_parse import SECTOR_DICT

print(SECTOR_DICT["Basic_Materials_Sector"])


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


# list of strategy method references
strategies = []

# list with days in each month
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# starting money
PRINCIPLE = 10000

# initializing instance of environment
env = StockMarketEnv(PRINCIPLE)

# hyperparameter, how many years strategies are tested over
N = 5

# currently tests with investing daily
for strategy in strategies:
    for year in range(1, N + 1):
        for month in range(1, 12):
            for day in range(days_per_month[month] + 1 if is_leap_year(year) and month == 2 else 0):
                # strategy("" + )
                pass
