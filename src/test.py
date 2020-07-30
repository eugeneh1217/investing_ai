import data
from comp_pe import compare_pe
from stock_market_env import StockMarketEnv
from csv_parse import SECTOR_DICT
import datetime as dt

print(SECTOR_DICT["Basic_Materials_Sector"])


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def has_leap_year(start_year, end_year):
    leap_years = 0
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years += 1
    return leap_years


# list of strategy method references
strategies = []

histories = []

# list with days in each month
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# constant and average_period ranges in days (inclusive)
CONSTANT_RANGE = (0, 20)
AVE_PERIOD_RANGE = (1, 100)

# starting money
PRINCIPLE = 1500

# initializing instance of environment
env = StockMarketEnv(PRINCIPLE)

# hyperparameter, how many years strategies are tested over
N = 5

# currently tests with investing daily
for strategy in strategies:
    for constant in range(CONSTANT_RANGE[0]. CONSTANT_RANGE[1] + 1):
        for ave_period in range(AVE_PERIOD_RANGE[0], AVE_PERIOD_RANGE[1] + 1):
            for testing_period in range(N):
                today = dt.date.today()
                day = today - dt.timedelta(days=N * 365)
                while day != today:
                    day += dt.timedelta(days=1)
                    buy_list, sell_list = strategy(day - dt.timedelta(days=ave_period), day)
                    env.step(buy_list, sell_list)
                histories.append(env.history)
                env.reset()
