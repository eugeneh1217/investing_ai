import data
from comp_pe import compare_pe
from stock_market_env import StockMarketEnv
from csv_parse import SECTOR_DICT
import datetime as dt

# list of strategy method references
strategies = []

# list of histories from testing loops:
histories = []

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
for strategy_index in range(len(strategies)):
    for testing_period in range(N):

        # reference to today bc it is used multiple times
        today = dt.date.today()

        for constant in range(CONSTANT_RANGE[0]. CONSTANT_RANGE[1] + 1):

            for ave_period in range(AVE_PERIOD_RANGE[0], AVE_PERIOD_RANGE[1] + 1):

                # reset day before running testing loop
                day = today - dt.timedelta(days=N * 365)

                # testing loop
                while day != today:

                    # increment day
                    day += dt.timedelta(days=1)

                    # impliment current strategy
                    buy_list, sell_list = strategies[strategy_index](day - dt.timedelta(days=ave_period), day)

                    # carry out transactions specified by strategy
                    env.step(buy_list, sell_list)

                # record history
                histories.append(dict(strategy=strategies[strategy_index].__name__, testing_period=testing_period,
                                      constant=constant, ave_period=ave_period, history=env.history))
                env.reset()


# list to hold best strategy with best hyper parameters
best_three = [histories[0], histories[1], histories[2]]

# evaluate different hyperparameters for different strategies
for trial_index in range(3, len(histories)):
    last_networth = histories[trial_index]["history"][0][len(histories[trial_index]["history"]) - 1]
    for x in range(len(best_three)):
        if last_networth > best_three[x]:
            best_three.insert(histories[trial_index])
    best_three = best_three[:4]

for trial in best_three:
    print("strategy: {}".format(trial["strategy"]))
    print("testing_period: {}".format(trial["testing_period"]))
    print("constant: {}".format(trial["constant"]))
    print("ave_period: {}".format(trial["ave_period"]))
    print("end networth: {}".format(trial["history"][0][len(trial["history"][0]) - 1]))

